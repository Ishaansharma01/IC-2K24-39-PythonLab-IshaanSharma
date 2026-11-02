
students = {
    101: {"name": "Asha", "marks": {
        "Math": 88, "Physics": 76, "Chem": 92
    }},
    102: {"name": "Ravi", "marks": {
        "Math": 35, "Physics": 58, "Chem": 64
    }},
    103: {"name": "Meena", "marks": {
        "Math": 72, "Physics": 81, "Chem": 69
    }}
}


def get_marks():
    while True:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            return marks
        else:
            print("Marks must be between 0 and 100.")


def add_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("Duplicate roll number!")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = {}
    n = int(input("How many subjects? "))

    for i in range(n):
        subject = input("Enter subject name: ").strip()

        if subject:
            marks[subject] = get_marks()
        else:
            print("Subject name cannot be empty.")

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")


def update_marks():
    roll = int(input("Enter roll number: "))

    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject: ").strip()
    score = get_marks()

    students[roll]["marks"][subject] = score
    print("Marks added/updated successfully.")


def delete_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def show_record():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("Roll Number:", roll)
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found.")


def reports():
    # Average marks of each student
    averages = {
        roll: round(sum(s["marks"].values()) / len(s["marks"]), 2)
        for roll, s in students.items()
        if s["marks"]
    }

    print("\n1. Average marks:")
    for roll, avg in averages.items():
        print(roll, "->", avg)

    # Topper
    if averages:
        topper_roll = max(averages, key=averages.get)
        print("\n2. Topper:", students[topper_roll]["name"],
              "with average", averages[topper_roll])
    else:
        print("\n2. No students with marks available.")

    # Highest scorer in each subject
    subject_scores = {}

    for roll, s in students.items():
        for subject, score in s["marks"].items():
            if (subject not in subject_scores or
                    score > subject_scores[subject][1]):
                subject_scores[subject] = (s["name"], score)

    print("\n3. Highest scorer in each subject:")
    for subject, (name, score) in subject_scores.items():
        print(subject, "->", name, "(", score, ")")

    # Students scoring below 40
    print("\n4. Students scoring below 40:")

    below_40 = {
        s["name"]: {
            sub: score for sub, score in s["marks"].items()
            if score < 40
        }
        for s in students.values()
        if any(score < 40 for score in s["marks"].values())
    }

    if below_40:
        for name, subjects in below_40.items():
            print(name, "->", subjects)
    else:
        print("None")

    # Grade-wise grouping
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for roll, avg in averages.items():
        name = students[roll]["name"]

        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("\n5. Grade-wise grouping:")
    print(grades)


while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Add student")
    print("2. Update subject marks")
    print("3. Delete student")
    print("4. Show student record")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_record()
    elif choice == "5":
        reports()
    elif choice == "6":
        print("Exiting Student Database.")
        break
    else:
        print("Invalid choice. Try again.")
