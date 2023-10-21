from datetime import date

wiek = int(input('Podaj swój wiek:'))
plec = input('Podaj swoja plec: K/M')
region = input("Czy jestes z regionu EUR czy z USA \n")
if plec == 'M' and wiek >= 40 and region == 'USA':
    print("Pierwsza paczka Marboro gratis!")
else:
    print("OK")
while not ((region == "EUR") or (region == "USA")):
    try:
        region = input("Kraj nie rozpoznany, Prosze wybrac jedna z opcji EUR albo USA \n")
    except ValueError:
        print("Fatal Error Crash")
