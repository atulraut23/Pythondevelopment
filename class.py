class Employee:

    company_name = "Infosys"

    def __init__(self, ID, nm, Sl):
        print(ID, nm, Sl)
        print(self)
        self.name           = nm
        self.id             = ID
        self.Salary         = Sl

    def set_bonus(self, bonus):
        self.bonus = bonus
        print('This month total salary with Bonus = ', self.Salary + self.bonus)

e1 = Employee(101, 'Jay', 25000)
e1.set_bonus(500)
#Code added by Atul
e2=Employee(301, 'Nayan', 35000)
