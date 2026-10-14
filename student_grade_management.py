"""
Task 2: Core Concepts and Skills
Project: Student Grade Management System

Demonstrates variables, input/output, data types, conditionals, loops,
functions, lists, dictionaries, and exception handling.
"""

def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks) if marks else 0


def get_grade(average):
    """Return a grade based on the average mark."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def read_mark(subject):
    """Read and validate a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=== Student Grade Management System ===")
    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    subjects = ["Python", "SQL", "Computer Networks"]
    marks = []

    for subject in subjects:
        marks.append(read_mark(subject))

    average = calculate_average(marks)
    total = sum(marks)
    grade = get_grade(average)
    result = "Pass" if all(mark >= 40 for mark in marks) else "Fail"

    student = {
        "name": name,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result,
    }

    print("\n=== Student Report ===")
    print(f"Student: {student['name']}")
    for subject, mark in zip(student["subjects"], student["marks"]):
        print(f"{subject}: {mark:.1f}")
    print(f"Total: {student['total']:.1f}/{len(subjects) * 100}")
    print(f"Average: {student['average']:.2f}%")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['result']}")


if __name__ == "__main__":
    main()
