from fastapi import FastAPI


# Dummy student records: student_id -> name
STUDENTS = {
    "S001": "Alice Johnson",
    "S002": "Bob Smith",
    "S003": "Carol Davis",
    "S004": "David Lee",
    "S005": "Emma Wilson",
}

# Dummy cricketer records: cricketer_id -> name
CRICKETERS = {
    "C001": "Sachin Tendulkar",
    "C002": "Virat Kohli",
    "C003": "MS Dhoni",
    "C004": "Rohit Sharma",
    "C005": "Jasprit Bumrah",
}

app = FastAPI()


def get_all_student_names() -> list[str]:
    """Return all student names."""
    return list(STUDENTS.values())


def get_student_id(name: str) -> str | None:
    """Resolve a student name to their ID. Returns None if not found."""
    name_lower = name.strip().lower()
    for student_id, student_name in STUDENTS.items():
        if student_name.lower() == name_lower:
            return student_id
    return None


def get_student_name(student_id: str) -> str | None:
    """Resolve a student ID to their name. Returns None if not found."""
    return STUDENTS.get(student_id.strip().upper())


def get_all_cricketer_names() -> list[str]:
    """Return all cricketer names."""
    return list(CRICKETERS.values())


def get_cricketer_id(name: str) -> str | None:
    """Resolve a cricketer name to their ID. Returns None if not found."""
    name_lower = name.strip().lower()
    for cricketer_id, cricketer_name in CRICKETERS.items():
        if cricketer_name.lower() == name_lower:
            return cricketer_id
    return None


def get_cricketer_name(cricketer_id: str) -> str | None:
    """Resolve a cricketer ID to their name. Returns None if not found."""
    return CRICKETERS.get(cricketer_id.strip().upper())


@app.get("/students")
def students() -> list[str]:
    return get_all_student_names()


@app.get("/cricketers")
def cricketers() -> list[str]:
    return get_all_cricketer_names()


def main():
    print("All students:")
    for name in get_all_student_names():
        print(f"  - {name}")

    print("\nResolve name -> ID:")
    print(f"  Alice Johnson -> {get_student_id('Alice Johnson')}")

    print("\nResolve ID -> name:")
    print(f"  S003 -> {get_student_name('S003')}")

    print("\nAll cricketers:")
    for name in get_all_cricketer_names():
        print(f"  - {name}")

    print("\nResolve cricketer name -> ID:")
    print(f"  Virat Kohli -> {get_cricketer_id('Virat Kohli')}")

    print("\nResolve cricketer ID -> name:")
    print(f"  C003 -> {get_cricketer_name('C003')}")


if __name__ == "__main__":
    main()
