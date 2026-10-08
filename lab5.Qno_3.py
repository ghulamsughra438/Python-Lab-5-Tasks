# Question 3
employees = []

for i in range(3):
    print("\nEnter information for Employee", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\nEmployee Information:")
for employee in employees:
    print(employee)