def valid_phone(phone):

    return (
        phone.isdigit()
        and len(phone) == 10
    )


def valid_attendance_status(status):

    return status in [
        "Present",
        "Absent",
        "Half Day",
        "Work From Home"
    ]


def valid_checkout(check_in, check_out):

    return check_out > check_in
