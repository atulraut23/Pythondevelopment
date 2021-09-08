class Student:

    university = 'SPPU'

    def __init__(self, nm, roll):
        self.name       = nm
        self.roll_num   = roll

    @classmethod
    def display(cls):
        print('Name of the university is ', cls.university )
        print()

    @staticmethod
    def addition(a,b):
        print('Addition of marks= ', a+b)

s1 = Student('Pavan', 10)

#Student.display()
Student.addition(25, 50)
#Hello i am checking
# Again I am checking
#Code is upadate by another user
