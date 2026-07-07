CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    department VARCHAR(100),
    designation VARCHAR(100),
    is_active BOOLEAN
);

CREATE TABLE shifts(
    id INTEGER PRIMARY KEY,
    shift_name VARCHAR(100),
    start_time TIME,
    end_time TIME,
    shift_type VARCHAR(50)
);

CREATE TABLE attendance(
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    shift_id INTEGER,
    date DATE,
    check_in TIME,
    check_out TIME,
    attendance_status VARCHAR(50)
);
