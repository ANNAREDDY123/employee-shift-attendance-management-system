from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    ForeignKey
)

from database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(
        Integer,
        primary_key=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    shift_id = Column(
        Integer,
        ForeignKey("shifts.id")
    )

    date = Column(Date)

    check_in = Column(Time)

    check_out = Column(Time)

    attendance_status = Column(String)
