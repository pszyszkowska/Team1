from datetime import date

def get_age():
    while True:
        try:
            wiek = input('Podaj swój wiek: ')
            wiek = int(wiek)
            if wiek < 0 or wiek >= 120:
                print("Podany wiek jest nieprawidłowy. Wprowadź go ponownie.")
            else:
                return wiek
        except ValueError:
            print("Podana wartość nie jest liczbą.")

def get_gender():
    while True:
        plec = input('Podaj swoją płeć (K/M): ')
        if plec in ['K', 'M']:
            return plec
        else:
            print("Płeć nie rozpoznana. Proszę wybrać jedną z opcji K lub M.")

def get_region():
    while True:
        region = input("Czy jesteś z regionu EUR czy z USA (EUR/USA): ")
        if region in ['EUR', 'USA']:
            return region
        else:
            print("Kraj nie rozpoznany. Proszę wybrać jedną z opcji EUR albo USA.")

def main():
    wiek = get_age()
    plec = get_gender()
    region = get_region()

    if plec == 'M' and wiek >= 40 and region == 'USA':
        print("Pierwsza paczka Marboro gratis!")
    elif wiek >= 30 and plec == "K":
        print("Darmowy drink")
    else:
        print("Nie spełniasz warunków, aby otrzymać darmowe paczki Marboro lub drinka.")

if __name__ == "__main__":
    main()
