
employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}


def add_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employees[emp_id] = {
        "name": name,
        "dept": dept,
        "salary": salary
    }

    print("Employee added successfully.")


def update_salary():
    emp_id = input("Enter employee ID: ")

    if emp_id not in employees:
        print("Employee not found.")
        return

    salary = float(input("Enter new salary: "))
    employees[emp_id]["salary"] = salary

    print("Salary updated successfully.")


def delete_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def search_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee ID:", emp_id)
        print("Name:", employees[emp_id]["name"])
        print("Department:", employees[emp_id]["dept"])
        print("Salary:", employees[emp_id]["salary"])
    else:
        print("Employee not found.")


def reports():
    # 1. Department-wise payroll and headcount in one pass
    departments = {}

    for emp in employees.values():
        dept = emp["dept"]

        if dept not in departments:
            departments[dept] = {"payroll": 0, "headcount": 0}

        departments[dept]["payroll"] += emp["salary"]
        departments[dept]["headcount"] += 1

    print("\n1. Department-wise Payroll and Headcount:")
    for dept, data in departments.items():
        print(dept, "Payroll:", data["payroll"],
              "Headcount:", data["headcount"])

    # 2. Highest-paid employee in each department
    highest_paid = {}

    for emp_id, emp in employees.items():
        dept = emp["dept"]

        if (dept not in highest_paid or
                emp["salary"] > highest_paid[dept]["salary"]):
            highest_paid[dept] = {
                "name": emp["name"],
                "salary": emp["salary"]
            }

    print("\n2. Highest-paid Employee in Each Department:")
    for dept, emp in highest_paid.items():
        print(dept, "->", emp["name"], emp["salary"])

    # 3. Employees sorted by salary, highest first
    sorted_employees = sorted(
        employees.items(),
        key=lambda item: item[1]["salary"],
        reverse=True
    )

    print("\n3. Employees Sorted by Salary:")
    for emp_id, emp in sorted_employees:
        print(emp_id, emp["name"], emp["salary"])

    # 4. Create a NEW dictionary with a 10% raise below 50000.
    # A comprehension creates a separate dictionary, so the original
    # employees and their salaries remain unchanged.
    raised_employees = {
        emp_id: {
            **emp,
            "salary": emp["salary"] * 1.10
        }
        for emp_id, emp in employees.items()
        if emp["salary"] < 50000
    }

    print("\n4. New Dictionary After 10% Raise:")
    for emp_id, emp in raised_employees.items():
        print(emp_id, emp["name"], emp["salary"])

    print("Original salaries remain unchanged:")
    for emp_id, emp in employees.items():
        print(emp_id, emp["name"], emp["salary"])

    # 5. Department with the highest average salary
    dept_salary = {}

    for emp in employees.values():
        dept = emp["dept"]

        if dept not in dept_salary:
            dept_salary[dept] = {"total": 0, "count": 0}

        dept_salary[dept]["total"] += emp["salary"]
        dept_salary[dept]["count"] += 1

    averages = {
        dept: data["total"] / data["count"]
        for dept, data in dept_salary.items()
    }

    if averages:
        best_dept = max(averages, key=averages.get)
        print("\n5. Highest Average Salary:")
        print(best_dept, "->", averages[best_dept])
    else:
        print("\n5. No employees available.")


while True:
    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search by ID")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_salary()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        reports()
    elif choice == "6":
        print("Exiting Employee Database.")
        break
    else:
        print("Invalid choice.")
