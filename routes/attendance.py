from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.attendance import Attendance
from models.employee import Employee
from models.shift import Shift

from schemas.attendance import AttendanceCreate

from services.attendance_service import (
    valid_attendance_status,
    valid_checkout
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == attendance.employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    shift = db.query(Shift).filter(
        Shift.id == attendance.shift_id
    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not found."
        )

    existing = db.query(Attendance).filter(
        Attendance.employee_id == attendance.employee_id,
        Attendance.date == attendance.date
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this employee on this date."
        )

    if not valid_attendance_status(
        attendance.attendance_status
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid attendance status."
        )

    if not valid_checkout(
        attendance.check_in,
        attendance.check_out
    ):

        raise HTTPException(
            status_code=400,
            detail="Check-out time must be greater than check-in time."
        )

    new_attendance = Attendance(
        employee_id=attendance.employee_id,
        shift_id=attendance.shift_id,
        date=attendance.date,
        check_in=attendance.check_in,
        check_out=attendance.check_out,
        attendance_status=attendance.attendance_status
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


@router.get("/")
def get_attendance(
    employee_id: int = None,
    date: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Attendance)

    if employee_id:
        query = query.filter(
            Attendance.employee_id == employee_id
        )

    if date:
        query = query.filter(
            Attendance.date == date
        )

    total = query.count()

    records = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": records
    }


@router.get("/{employee_id}")
def employee_attendance(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()


@router.put("/{attendance_id}")
def update_attendance(
    attendance_id: int,
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):

    record = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not record:

        raise HTTPException(
            status_code=404,
            detail="Attendance record not found."
        )

    record.check_in = attendance.check_in
    record.check_out = attendance.check_out
    record.attendance_status = attendance.attendance_status

    db.commit()

    return {
        "message": "Attendance updated successfully."
    }


@router.get("/reports/monthly/{employee_id}")
def monthly_report(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()
