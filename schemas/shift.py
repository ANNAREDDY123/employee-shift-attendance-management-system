from pydantic import (
    BaseModel,
    Field
)

from datetime import time


class ShiftCreate(BaseModel):

    shift_name: str = Field(..., min_length=2)

    start_time: time

    end_time: time

    shift_type: str
