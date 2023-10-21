from datetime import date

wiek = input('Podaj swój wiek:')
while not wiek.strip().isdigit():
    try:
        wiek = input("Liczba nie rozpoznana.\n Podaj swój wiek: ")
    except ValueError:
        print("Fatal Error Crash")
plec = input('Podaj swoja plec: K/M')
while not ((plec == "K") or (plec == "M")):
    try:
        plec = input("Płeć nie rozpoznana.\n Proszę wybrać jedną z opcji K lub M \n")
    except ValueError:
        print("Fatal Error Crash")
region = input("Czy jestes z regionu EUR czy z USA \n")
while not ((region == "EUR") or (region == "USA")):
    try:
        region = input("Kraj nie rozpoznany, Prosze wybrac jedna z opcji EUR albo USA \n")
    except ValueError:
        print("Fatal Error Crash")
if plec == 'M' and wiek >= 40 and region == 'USA':
    print("Pierwsza paczka Marboro gratis!")
else:
    exit()
while wiek >= 120:
    print("Jestes duchem? Wprowadz swoj wiek ponownie.")
    wiek = int(input("Podaj jeszcze raz swoj wiek: "))
    continue
if int(wiek) >= 30 and plec == "K":
    print("Darmowy drink")
else:
    exit()