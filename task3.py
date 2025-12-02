from abc import ABC, abstractmethod
from typing import List

# --- Component ---
class OrganizationUnit(ABC):
    @abstractmethod
    def get_total_salary(self) -> float:
        pass

    @abstractmethod
    def do_operation(self, task: str):
        pass

# --- Leaf ---
class Employee(OrganizationUnit):
    def __init__(self, name: str, role: str, salary: float):
        self.name = name
        self.role = role
        self.salary = salary

    def get_total_salary(self) -> float:
        return self.salary

    def do_operation(self, task: str):
        print(f"  - {self.role} {self.name} is working on: {task}")

# --- Composite ---
class Department(OrganizationUnit):
    def __init__(self, name: str):
        self.name = name
        self.sub_units: List[OrganizationUnit] = []

    def add(self, unit: OrganizationUnit):
        self.sub_units.append(unit)

    def remove(self, unit: OrganizationUnit):
        self.sub_units.remove(unit)

    def get_total_salary(self) -> float:
        total = 0
        for unit in self.sub_units:
            total += unit.get_total_salary()
        return total

    def do_operation(self, task: str):
        print(f"[{self.name}] received task: {task}")
        for unit in self.sub_units:
            unit.do_operation(task)

# --- Usage ---
if __name__ == "__main__":
    # Leafs
    dev1 = Employee("John", "Developer", 3000)
    dev2 = Employee("Jane", "Developer", 3200)
    manager = Employee("Mike", "Manager", 5000)
    
    # Composites
    dev_team = Department("Development Team")
    dev_team.add(dev1)
    dev_team.add(dev2)

    main_dept = Department("IT Department")
    main_dept.add(manager)
    main_dept.add(dev_team) # Adding a team (composite) to a department

    # 1. Calculate Salary recursively
    print(f"Total Salary for IT Department: ${main_dept.get_total_salary()}")

    # 2. Assign task uniformly
    print("\nAssigning Task:")
    main_dept.do_operation("System Migration")
