
# Python Lab — Lab 4: Dictionary

**Subject:** Python Programming Lab  
**Lab:** 4  
**Topic:** Python Dictionaries  
**Author:** Ishaan Sharma

---

## 📌 Overview

This lab explores Python dictionaries and their applications in solving real-world problems. It covers nested dictionaries, dictionary methods, comprehensions, aggregation, sorting, searching, data validation, output prediction, and conceptual reasoning.

The assignment is divided into three parts:

- **Part A:** Five practical Python programs.
- **Part B:** Predicting the output of dictionary-based Python code.
- **Part C:** Short reasoning questions about dictionary behavior and implementation choices.

## 🎯 Objectives

- Understand dictionary creation, access, modification, and deletion.
- Implement nested dictionaries and dictionaries containing lists.
- Build menu-driven applications using dictionaries.
- Apply dictionary comprehensions and list comprehensions.
- Perform grouping, filtering, sorting, and aggregation.
- Validate user input and handle missing records.
- Understand aliasing, shallow copying, deep copying, and hashable keys.
- Analyze dictionary operations and their time complexity.

---

# Part A: Programs

## Q1. Student Database

**Concepts:** Nested dictionaries, validation, averages, grades, and reports.

Store student records using the structure:

`roll_no -> {"name": ..., "marks": {subject: score}}`

### Features
- Add a student and reject duplicate roll numbers.
- Validate marks between 0 and 100.
- Update marks for an existing or new subject.
- Delete a student.
- Display a student's complete record.
- Calculate average marks for every student.
- Identify the topper and highest scorer in each subject.
- Find students scoring below 40 in any subject.
- Group students by grades A, B, C, D, and F.

### Sample Data

| Roll No. | Name | Math | Physics | Chemistry |
|---|---|---:|---:|---:|
| 101 | Asha | 88 | 76 | 92 |
| 102 | Ravi | 35 | 58 | 64 |
| 103 | Meena | 72 | 81 | 69 |

### Expected Results
- Asha's average: 85.33
- Ravi's average: 52.33
- Meena's average: 74.00
- Topper: Asha
- Highest Math scorer: Asha (88)
- Highest Physics scorer: Meena (81)
- Highest Chemistry scorer: Asha (92)
- Student scoring below 40: Ravi

## Q2. Employee Database

**Concepts:** Dictionary operations, aggregation, grouping, sorting, and comprehensions.

Store employees using:

`emp_id -> {"name": ..., "dept": ..., "salary": ...}`

### Features
- Add, update, delete, and search employee records.
- Calculate department-wise total payroll and headcount in one pass.
- Identify the highest-paid employee in each department.
- Sort employees by salary in descending order.
- Create a new dictionary applying a 10% raise to employees earning below ₹50,000.
- Find the department with the highest average salary.
- Display a friendly message when an employee does not exist.

### Sample Data

| Employee ID | Name | Department | Salary |
|---|---|---|---:|
| E1 | Kiran | IT | 60000 |
| E2 | Sara | HR | 45000 |
| E3 | Dev | IT | 75000 |
| E4 | Nina | Finance | 52000 |
| E5 | Omar | HR | 48000 |

### Expected Results
- IT payroll: ₹135,000
- HR payroll: ₹93,000
- Finance payroll: ₹52,000
- Highest-paid IT employee: Dev
- Highest-paid HR employee: Omar
- Highest-paid Finance employee: Nina
- Highest average salary: IT (₹67,500)
- Sara's revised salary: ₹49,500
- Omar's revised salary: ₹52,800

The original employee dictionary must remain unchanged after generating the revised salary dictionary.

## Q3. Library Record System

**Concepts:** Nested dictionaries, lists, state management, and validation.

Store books using:

`isbn -> {"title": ..., "author": ..., "copies": ..., "issued_to": [...]}`

### Features
- Add a book or increase copies for an existing ISBN.
- Issue and return books.
- Search for books.
- Allow a member to hold a maximum of two books.
- Prevent issuing unavailable books.
- Prevent the same member from borrowing the same book twice.
- Reject returns when the member does not hold the book.
- Generate reports for books by author, unavailable books, never-issued books, and members holding multiple books.

### Sample Data

| Book ID | Title | Author | Copies |
|---|---|---|---:|
| B1 | Python Basics | Rao | 2 |
| B2 | Data Structures | Iyer | 1 |
| B3 | Algorithms | Rao | 1 |

### Important Test Cases
- Issue B1 to M1: success.
- Issue B1 to M2: success; available copies become zero.
- Issue B1 to M3: rejected because no copies remain.
- Issue B1 to M1 again: rejected because M1 already holds it.
- Return B1 by M9: rejected because M9 does not hold it.
- Return B1 by M1: success.
- Enforce the two-book limit per member.

## Q4. Word Frequency Counter

**Concepts:** String processing, dictionaries as counters, sorting, and comprehensions.

### Features
- Accept a paragraph from the user.
- Convert text to lowercase and remove punctuation without using a library for punctuation removal.
- Count each word using `.get()`.
- Display the top N words, breaking ties alphabetically.
- Find words appearing exactly once.
- Invert the frequency dictionary into `{frequency: [words]}`.
- Group unique words by length.
- Search for a word and display its count.
- Handle empty input gracefully.

### Example

**Input:**
`the cat and the hat and the bat`

**Expected frequency counts:**
- the: 3
- and: 2
- bat: 1
- cat: 1
- hat: 1

**Top 3 words:** the (3), and (2), bat (1)

**Inverted dictionary:**
`{3: ['the'], 2: ['and'], 1: ['bat', 'cat', 'hat']}`

## Q5. Phone Directory

**Concepts:** Dictionaries with list values, reverse lookup, searching, and validation.

Store contacts using:

`name -> {"phones": [...], "email": ..., "city": ...}`

### Features
- Add and delete contacts.
- Add another number to an existing contact.
- Update email or city.
- Search names using a case-insensitive partial match.
- Validate that phone numbers contain exactly 10 digits.
- Prevent a phone number from belonging to multiple contacts.
- Build a reverse lookup dictionary mapping numbers to names.
- Group contacts by city.
- Find contacts with multiple phone numbers.
- Display the directory alphabetically.

### Sample Data

| Name | Phone Numbers | Email | City |
|---|---|---|---|
| Anita | 9876543210 | anita@mail.com | Pune |
| Manoj | 9123456780, 9988776655 | manoj@mail.com | Delhi |
| Zara | 9000011111 | zara@mail.com | Pune |

### Expected Results
- Partial search `"an"`: Anita, Manoj
- Reverse lookup `9988776655`: Manoj
- Pune contacts: Anita, Zara
- Delhi contacts: Manoj
- Contact with multiple numbers: Manoj
- Duplicate phone number: rejected
- Invalid number such as `12345`: rejected

---

# Part B: Predict the Output

This section tests understanding of dictionary behavior and Python execution.

### Topics Covered
1. Dictionary aliasing.
2. Shallow copying of nested dictionaries.
3. Dictionary comprehensions with conditions.
4. The `.setdefault()` method.
5. Equal dictionary keys such as `1`, `1.0`, and `True`.
6. Deleting dictionary entries during iteration.
7. The `.pop()` and `.popitem()` methods.
8. Dictionary comprehensions with duplicate values.

### Instructions
- Predict the output before running each program.
- Execute the code to verify the answer.
- For every incorrect prediction, write one line explaining the mistake.

---

# Part C: Short Reasoning Questions

This section focuses on the reasoning behind Python dictionary operations.

### Topics Covered
1. Aliasing versus copying.
2. Shallow copy versus deep copy.
3. Hashable and unhashable dictionary keys.
4. Dictionary access using `d[key]` and `.get()`.
5. The `.update()` method versus direct assignment.
6. Creating new dictionaries using comprehensions.
7. Safe deletion of dictionary keys.
8. Inverting dictionaries containing multiple values.
9. Dictionary lookup complexity versus list searching.

### Learning Goal
Explain not only how dictionary operations work, but also why a particular approach is suitable for a given problem.

---

# 🛠️ Technologies Used

- **Programming Language:** Python 3.x
- **Data Structures:** Dictionaries, nested dictionaries, and lists
- **Core Concepts:** Functions, loops, conditional statements, comprehensions, sorting, searching, and input validation
- **Editor:** Visual Studio Code or any Python-compatible editor
- **Version Control:** Git and GitHub

# ▶️ How to Run

1. Install Python 3.x.
2. Clone or download this repository.
3. Open the project in Visual Studio Code.
4. Navigate to the folder containing the required Python program.
5. Open the terminal and run:

   ```bash
   python filename.py
   ```

6. Replace `filename.py` with the actual name of the program.

**Note:** The program filenames and folder paths may vary depending on the repository structure.

# 🧪 Testing Checklist

- [ ] Verify valid and invalid student marks.
- [ ] Test duplicate student and employee IDs.
- [ ] Check missing-record handling during search and deletion.
- [ ] Verify student averages, toppers, and grade groups.
- [ ] Check department-wise payroll and salary calculations.
- [ ] Verify that the original employee dictionary remains unchanged after the raise operation.
- [ ] Test library issue and return restrictions.
- [ ] Test empty text and word-frequency calculations.
- [ ] Verify alphabetical tie-breaking in the top N words.
- [ ] Test phone-number length and duplicate-number validation.
- [ ] Verify all reports against the supplied sample data.
- [ ] Predict and verify the output of all Part B snippets.

# 📚 Learning Outcomes

After completing this lab, students should be able to:

1. Design applications using nested dictionaries.
2. Implement menu-driven programs.
3. Perform CRUD operations on dictionary records.
4. Use comprehensions for filtering and transforming data.
5. Aggregate and group records efficiently.
6. Validate data and enforce application rules.
7. Explain dictionary copying, hashing, and key behavior.
8. Analyze the efficiency of dictionary lookups.
9. Debug and verify Python program output.

---

**Author:** Ishaan Sharma  
**Course:** Integrated MCA  
**Lab Assignment:** Python Dictionaries — Lab 4
