
def valid_input_int():
    '''Прозводит валидацию ввода, если буден введено
    не целое число, то будет ждать правильного ввода'''
    while True:
        try:
            day = int(input('Enter total amount days: '))
        except ValueError:
            print('Enter an integer')
        else:
            return day


def days_to_ywd(day: int) -> tuple:
    '''Функция принимаяет общее количество дней
    и возвращает кортеж с количеством: года, недели и дней'''
    day_ = day  # не будем изменять входные данные
    year = day_ // 365
    day_ = day_ % 365
    week = day_ // 7
    day_ = day_ % 7
    return year, week, day_


def main():
    '''Основная программа'''
    day = valid_input_int()
    year, week, day_ = days_to_ywd(day)
    print('----------------------------------------')
    print(f"Years: {year}\nWeeks: {week}\nDays: {day_}")


main()
