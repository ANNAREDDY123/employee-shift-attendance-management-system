from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    phone = Column(String)

    department = Column(String)

    designation = Column(String)

    is_active = Column(
        Boolean,
        default=True
    )
