class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)



e1 = Employee("Arun", "Staff")
t1 = Trainer("Rahul", "Fitness Trainer", "Weight Training")
y1 = YogaInstructor("Anu", "Yoga Instructor", "Hatha Yoga")
m1 = MultiTrainer("Vishnu", "Fitness and Yoga Trainer", "Strength Training", "Vinyasa Yoga")


print("Employee Details")
e1.display()

print("\nTrainer Details")
t1.display()

print("\nYoga Instructor Details")
y1.display()

print("\nMultiTrainer Details")
m1.display()