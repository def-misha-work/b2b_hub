from datetime import datetime


def validate_date(date_str):
    try:
        # Проверяем формат даты для двузначного года
        date = datetime.strptime(date_str, '%d.%m.%y')
    except ValueError as e:
        print(f"Ошибка 2х {e}")
        try:
            # Проверяем формат даты для четырехзначного года
            date = datetime.strptime(date_str, '%d.%m.%Y')
        except ValueError as e:
            print(f"Ошибка 4х {e}")
            return False

    # Проверяем, что дата не раньше сегодняшнего дня
    if date.date() >= datetime.now().date():
        return True

    return False
