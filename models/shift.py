from sqlalchemy import (
    Column,
    Integer,
    String,
    Time
)

from database import Base


class Shift(Base):

    __tablename__ = "shifts"

    id = Column(
        Integer,
        primary_key=True
    )

    shift_name = Column(String)

    start_time = Column(Time)

    end_time = Column(Time)

    shift_type = Column(String)
