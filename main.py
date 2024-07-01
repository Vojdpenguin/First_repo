from datetime import datetime


start_date = string_to_date("2024.03.26")  # Перетворення рядка на дату
next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
print(next_monday)
next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(next_friday)

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday):
    day_of_week = start_date.weekday()



print(None)
    
        