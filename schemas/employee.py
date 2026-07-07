from pydantic import (
    BaseModel,
    EmailStr,
    Field
)


class EmployeeCreate(BaseModel):

    name: str = Field(..., min_length=3)

    email: EmailStr

    phone: str = Field(..., min_length=10, max_length=10)

    department: str

    designation: str
