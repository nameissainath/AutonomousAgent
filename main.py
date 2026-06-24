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
CRICKETERS {
    "C001": "Sachin Tendulkar",
    "C002": "Virat Kohli",
    "C003": "MS Dhoni",
    "C004": "Rohit Sharma",
    "C005": "Jasprit Bumrah",
}

app = FastAPI()


def get_all_student_names() -> list[str]:
    return list(STUDENTS.values())


def get_student_id(name: str) -> str | None:
    name_lower = name.strip().lower()
    for student_id, student_name in STUDENTS.items():
        if student_name.lower() == name_lower:
            return student_id
    return None


def get_student_name(student_id: str) -> str | None:
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


@app.get("/students/names")
def list_student_names():
    """Return all student names."""
    return {"names": get_all_student_names()}


@app.get("/students/{student_id}")
def get_student_by_id(student_id: str):
    """Resolve a student ID to their name."""
    name = get_student_name(student_id)
    if name is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student_id.strip().upper(), "name": name}


@app.get("/students/lookup/by-name")
def lookup_student_by_name(name: str = Query(..., description="Full student name")):
    """Resolve a student name to their ID."""
    student_id = get_student_id(name)
    if student_id is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student_id, "name": name.strip()}

    print("\nAll cricketers:")
    for name in get_all_cricketer_names():
        print(f"  - {name}")

    print("\nResolve cricketer name -> ID:")
    print(f"  Virat Kohli -> {get_cricketer_id('Virat Kohli')}")

    print("\nResolve cricketer ID -> name:")
    print(f"  C003 -> {get_cricketer_name('C003')}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
