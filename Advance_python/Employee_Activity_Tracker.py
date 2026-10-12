import re
from datetime import datetime
from functools import wraps


def log_execution(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Function started:", function.__name__)

        result = function(*args, **kwargs)

        print("Function completed:", function.__name__)
        return result

    return wrapper


def generate_employees(names):
    for employee_id, name in enumerate(names, start=1):
        yield {
            "id": employee_id,
            "name": name,
            "created_at": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }


@log_execution
def process_employees(names):
    for employee in generate_employees(names):
        if re.fullmatch(r"[A-Za-z ]+", employee["name"]):
            print(employee)
        else:
            print("Invalid employee name:", employee["name"])


names = ["Ravi", "Sravani", "Priya123"]

process_employees(names)