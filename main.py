from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    formatted_date = now.strftime("%A, %d %B %Y, %H:%M")
    print(f'Текущая дата и время: {formatted_date}\n')

    get_employees()
    calculate_salary()