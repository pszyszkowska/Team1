from datetime import date

wiek = int(input('Podaj swój wiek:'))
plec = input('Podaj swoja plec: K/M')
region = 'USA'
if plec == 'M' and wiek >= 40 and region == 'USA':
    print("Pierwsza paczka Marboro gratis!")
else:
    print("OK")