class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"имя: {self.name}, id: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} руководит проектом в отделе {self.department}"

class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"специалист {self.name} выполняет тех обслуживание в области {self.specialization}."

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        
        Employee.__init__(self, name, id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return "\n".join([emp.get_info() for emp in self.team])

a = input().split()
emp1 = Employee(a[0], int(a[1]))
man = Manager("волк", 2, "продаж")
tech = Technician("Василиса", 3, "электротехника")
tech_man = TechManager("кот ученый", 4, "IT", "разработка по")

print(emp1.get_info())
print(man.manage_project())
print(tech.perform_maintenance())
print(tech_man.manage_project())
print(tech_man.perform_maintenance())


tech_man.add_employee(emp1)
tech_man.add_employee(man)
tech_man.add_employee(tech)

print("команда:")
print(tech_man.get_team_info())