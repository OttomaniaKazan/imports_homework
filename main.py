from application.salary import print_salary_by_name
from application.db.people import print_employee_name
from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    formatted_date = now.strftime("%A, %d %B %Y, %H:%M")
    print(f'Текущая дата и время: {formatted_date}\n')

    print_employee_name()
    print_salary_by_name()