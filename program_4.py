# Programmer: Alethea Lo
# Date: 3/31/25
# Title: Employee Class

class Employee:
    def __init__(self, name, id_number, department, job_title):
        """Initialize the employee with name, ID number, department, and job title."""
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        """Return the employee's name."""
        return self.__name

    def get_id_number(self):
        """Return the employee's ID number."""
        return self.__id_number

    def get_department(self):
        """Return the employee's department."""
        return self.__department

    def get_job_title(self):
        """Return the employee's job title."""
        return self.__job_title

    def display_info(self):
        """Display employee details."""
        print(f"Name: {self.__name}")
        print(f"ID Number: {self.__id_number}")
        print(f"Department: {self.__department}")
        print(f"Job Title: {self.__job_title}")
        print("-" * 30)

def main():

    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    employees = [emp1, emp2, emp3]

    print("\nEmployee Details:\n" + "=" * 30)
    for emp in employees:
        emp.display_info()

if __name__ == "__main__":
    main()
