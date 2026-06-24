# Dummy student records: student_id -> name
STUDENTS = {
    "S001": "Alice Johnson",
    "S002": "Bob Smith",
    "S003": "Carol Davis",
    "S004": "David Lee",
    "S005": "Emma Wilson",
}


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


def main():
    print("All students:")
    for name in get_all_student_names():
        print(f"  - {name}")

    print("\nResolve name -> ID:")
    print(f"  Alice Johnson -> {get_student_id('Alice Johnson')}")

    print("\nResolve ID -> name:")
    print(f"  S003 -> {get_student_name('S003')}")


if __name__ == "__main__":
    main()
