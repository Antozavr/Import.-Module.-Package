class SalaryCalculator:
    def __init__(self):
        self.factor = 3.5
        self.salary = 15000

    def calculator(self):
        employee_salary = self.salary * self.factor
        print(f'Зарплата составляет:{int(employee_salary)} рублей')
