

# Student Attendance Management System


total_students = int(input("Enter total number of students: "))

all_students = set()

for i in range(total_students):
    name = input(f"Enter name of student {i+1}: ")
    all_students.add(name)

# Step 2: Take present students
present_count = int(input("\nEnter number of present students: "))

present_students = set()

for i in range(present_count):
    name = input(f"Enter name of present student {i+1}: ")
    present_students.add(name)

# Step 3: Find absent students
absent_students = all_students - present_students

# Step 4: Display result
print("\n--- Attendance Report ---")
print("Total Students:", all_students)
print("Present Students:", present_students)
print("Absent Students:", absent_students)
