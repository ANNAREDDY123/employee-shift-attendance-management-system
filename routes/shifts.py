from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.shift import Shift
from schemas.shift import ShiftCreate

router = APIRouter(
    prefix="/shifts",
    tags=["Shifts"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_shift(
    shift: ShiftCreate,
    db: Session = Depends(get_db)
):

    if shift.end_time <= shift.start_time:

        raise HTTPException(
            status_code=400,
            detail="Shift end time must be greater than start time."
        )

    new_shift = Shift(
        shift_name=shift.shift_name,
        start_time=shift.start_time,
        end_time=shift.end_time,
        shift_type=shift.shift_type
    )

    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)

    return new_shift


@router.get("/")
def get_shifts(
    db: Session = Depends(get_db)
):

    return db.query(Shift).all()


@router.put("/{shift_id}")
def update_shift(
    shift_id: int,
    shift: ShiftCreate,
    db: Session = Depends(get_db)
):

    db_shift = db.query(Shift).filter(
        Shift.id == shift_id
    ).first()

    if not db_shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not found."
        )

    db_shift.shift_name = shift.shift_name
    db_shift.start_time = shift.start_time
    db_shift.end_time = shift.end_time
    db_shift.shift_type = shift.shift_type

    db.commit()

    return {
        "message": "Shift updated successfully."
    }
