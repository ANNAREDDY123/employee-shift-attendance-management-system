from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.employee import Employee
from schemas.employee import EmployeeCreate

from services.attendance_service import valid_phone

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Employee email already exists."
        )

    if not valid_phone(employee.phone):

        raise HTTPException(
            status_code=400,
            detail="Phone number must contain exactly 10 digits."
        )

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        phone=employee.phone,
        department=employee.department,
        designation=employee.designation
    )

    db.add(new_employee)

    db.commit()

    db.refresh(new_employee)

    return new_employee


@router.get("/")
def get_employees(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Employee).filter(
        Employee.is_active == True
    )

    total = query.count()

    employees = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": employees
    }


@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id,
        Employee.is_active == True
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    return employee


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    db_employee = db.query(Employee).filter(
        Employee.id == employee_id,
        Employee.is_active == True
    ).first()

    if not db_employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.phone = employee.phone
    db_employee.department = employee.department
    db_employee.designation = employee.designation

    db.commit()

    return {
        "message": "Employee updated successfully."
    }


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    employee.is_active = False

    db.commit()

    return {
        "message": "Employee deactivated successfully."
    }
