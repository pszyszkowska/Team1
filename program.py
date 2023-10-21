from datetime import date

birth_year = int(input('Podaj rok urodzenia:'))
birth_month = int(input('Podaj miesiąc urodzenia:'))
birth_day = int(input('Podaj dzień urodzenia:'))
birth_date = date(birth_year,birth_month,birth_day)
birthday = date(birth_year + 18,birth_month,birth_day)
today_date = date.today()
if today_date >= birthday:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni!")