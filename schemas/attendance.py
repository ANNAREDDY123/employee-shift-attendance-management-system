from pydantic import BaseModel

from datetime import (
    date,
    time
)


class AttendanceCreate(BaseModel):

    employee_id: int

    shift_id: int

    date: date

    check_in: time

    check_out: time

    attendance_status: str
