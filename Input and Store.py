students = []
for i in range(2):
    name = input("Enter the name of student {}: ".format(i+1))
    regno = input("Enter the registration number of student {}: ".format(i+1))
    cgpa = float(input("Enter the CGPA of student {}: ".format(i+1)))
    students.append((name, regno, cgpa))
def display_students(students):
    for student in students:
        print("Name: {}, RegNo: {}, CGPA: {}".format(*student))
while True:
    print("\n1. Sort by name\n2. Sort by regno\n3. Sort by CGPA\n4. Display students\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        students.sort(key=lambda x: x[0])
    elif choice == 2:
        students.sort(key=lambda x: x[1])
    elif choice == 3:
        students.sort(key=lambda x: x[2], reverse=True)
    elif choice == 4:
        display_students(students)
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")