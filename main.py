from application.salary import print_salary_by_name
from application.db.people import print_employee_name
from datetime import datetime

# Мой отдельный проект импортированный сюда.
# Это мое первое знакомство с парсингом
from parser import parser

if __name__ == '__main__':
    now = datetime.now()
    formatted_date = now.strftime("%A, %d %B %Y, %H:%M")
    print(f'Текущая дата и время: {formatted_date}\n')

    print_employee_name()
    print_salary_by_name()

    answer = input('Хотите увидеть работу моего парсера? y/n: ')
    if answer == 'y':
        print('Демонстрация работы парсера, написанного '
              'для итоговой работы по модулю Базы Данных')
        data = parser.full_parser()
        parser.save_to_json(data)
    else:
        print("Весь код парсера вы можете посмотреть в пакете 'parser' "
              "в корне проекта")