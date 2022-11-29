import flake8
import datetime
from application.db.people import DataBase
from application.salary import SalaryCalculator

if __name__ == '__main__':
    print(datetime.datetime.today())
    func = DataBase()
    func.get_employees()
    sal = SalaryCalculator()
    sal.calculator()
