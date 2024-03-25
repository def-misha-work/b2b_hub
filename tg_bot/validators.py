from datetime import datetime


def validate_date(date_str):
    try:
        # Проверяем формат даты
        datetime.strptime(date_str, '%y.%m.%d')
        # Проверяем, что дата начинается не раньше сегодняшнего дня
        date = datetime.strptime(date_str, '%y.%m.%d')
        if date.date() >= datetime.now().date():
            return True
    except ValueError:
        pass
    return False
