from datetime import date

def podaj_wiek():
    while True:
        try:
            wiek = input('Podaj swój wiek: ')
            wiek = int(wiek)
            if wiek < 0 or wiek >= 120:
                print("Jesteś duchem? Podany wiek jest nieprawidłowy. Wprowadź go ponownie.")
            else:
                return wiek
        except ValueError:
            print("Podana wartość nie jest liczbą.")

def podaj_plec():
    while True:
        plec = input('Podaj swoją płeć (K/M): ')
        if plec.upper() in ['K', 'M']:
            return plec
        else:
            print("Płeć nie rozpoznana. Proszę wybrać jedną z opcji K lub M.")

def podaj_region():
    while True:
        region = input("Czy jesteś z regionu EUR czy z USA (EUR/USA): ")
        if region.upper() in ['EUR', 'USA']:
            return region
        else:
            print("Kraj nie rozpoznany. Proszę wybrać jedną z opcji EUR albo USA.")

def main():
    wiek = podaj_wiek()
    plec = podaj_plec()
    region = podaj_region()

    if plec == 'M' and wiek >= 40 and region == 'USA':
        print("Pierwsza paczka Marboro gratis!")
    elif wiek >= 30 and plec == "K":
        print("Darmowy drink")
    else:
        print("Nie spełniasz warunków, aby skorzystać z promocji.")

if __name__ == "__main__":
    main()
