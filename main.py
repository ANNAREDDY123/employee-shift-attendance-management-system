import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.employees import router as employees_router
from routes.shifts import router as shifts_router
from routes.attendance import router as attendance_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Shift & Attendance Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(employees_router)
app.include_router(shifts_router)
app.include_router(attendance_router)


@app.get("/")
def home():

    logger.info("Application Started Successfully")

    return {
        "message": "Employee Shift & Attendance Management System"
    }
