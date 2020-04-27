class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.salary = int(salary)

    @classmethod
    def from_str(cls, string):
        first_name, last_name, salary = string.split(",")
        return cls(first_name, last_name, salary)

    @property
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}_{self.last_name.lower()}@example.com"

    @full_name.setter
    def full_name(self, full_name):
        first_name, last_name = full_name.split(", ")
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

class DevOps(Employee):
    def __init__(self, first_name, last_name, salary, skills=[]):
        super().__init__(first_name, last_name, salary)
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill.capitalize())

    def remove_skill(self, skill):
        try:
            self.skills.remove(skill.capitalize())
        except:
            pass


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, subordinates=[]):
        super().__init__(first_name, last_name, salary)
        self.subordinates = subordinates

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        if subordinate in self.subordinates:
            return self.subordinates.remove(subordinate)
        else:
            try:
                for emp in self.subordinates:
                    if emp.email == subordinate:
                        self.subordinates.remove(emp)
            except ValueError as e:
                pass
