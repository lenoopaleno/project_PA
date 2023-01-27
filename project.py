import colorama
from colorama import Fore, Style, init
import os

init(autoreset=True)
clear = lambda: os.system('clear')


lista = []

def menu():
    print(Fore.YELLOW + "KATALOG DAŃ by Jan Czapski")
    print()
    print("1. Wyświetl katalog")
    print("2. Dodaj do katalogu")
    print("3. Usuń z katalogu")
    print("4. Znajdź i wyświetl danie")
    print("5. Znajdź i wyświetl dania po kaloryczności")
    print("6. Zamknij aplikacje")
    print()
    return wybor()

    

def wybor():
    wybor = input(Fore.CYAN + "Na klawiaturze wybierz numer interesującej Cie opcji: ")
    try: 
        int(wybor)
        if int(wybor) > 0 and int(wybor) < 7:
            return wybor
        else: 
            clear()
            print(Fore.RED + "Nie ma opcji o takim numerze.")
            print()
            print("Sprobuj jeszcze raz!")
            main()
    except:
        clear()
        print(Fore.RED + "Wybierz liczbę całkowitą, która znajduje się na liście!")
        print()
        print("Sprobuj jeszcze raz!")
        main()


def wyswietl_dania():
    clear()
    print(Fore.YELLOW + "KATALOG DAŃ")
    for i in katalog:
        print(Fore.GREEN + f"Danie: {i}    Kalorie: {katalog[i]}")

    print(Fore.LIGHTBLACK_EX + "Naciśnij '6', aby wyłączyć program.")
    print(Fore.LIGHTBLACK_EX + "Naciśnij dowolnym klawisz, aby wrócić, aby wyłączyć program.")
    wybor = input()
    
    if wybor == '6':
        zamknij()
    else:
        clear()
        main()
    

def dodaj_danie():
    print(Fore.YELLOW + "DODAJ DANIE DO KATALOGU")
    print()
    nazwa_dania = input("Nazwa dania: ")
    for i in katalog:
        if nazwa_dania == i:
            clear()
            print(Fore.RED + "Takie danie juz jest w katalogu")
            dodaj_danie()
    kcal = dodaj_kalorycznosc()
    katalog[nazwa_dania] = kcal
    clear()
    print(Fore.GREEN + "Pomyślnie dodałeś danie do katalogu")
    main()



def dodaj_kalorycznosc():
    kalorycznosc = input("Podaj kalorycznosc w 100g: ")
    try: 
        int(kalorycznosc)
        return int(kalorycznosc)
    except:
        clear()
        print(Fore.RED + "Wartość musi być podana w kcal")
        return dodaj_kalorycznosc()

def usun_danie():
    print(Fore.YELLOW + "USUŃ DANIE Z KATALOGU")
    print()
    danie = input("Podaj nazwę dania, które chcesz usunąć: ")
    for i in katalog:
        if danie == i:
            del katalog[danie]
            clear()
            print(Fore.GREEN + "Danie usunięto pomyślnie")
            main()
 
    clear()
    print(Fore.RED + f"Danie '{danie}' nie istnieje")
    usun_danie()


def znajdz_kcal():
    print(Fore.YELLOW + "ZNAJDŹ DANIE Z KATALOGU")
    print()
    danie = input("Podaj nazwę dania, które chcesz znaleźć: ")
    for i in list(katalog):
        if danie == i:
            print(f"Nazwa dania: {i}  Kaloryczność/100g: {katalog[i]}")
            print(Fore.LIGHTBLACK_EX + "Naciśnij dowolnym klawisz, aby wrócić, aby wyłączyć program.")
            wybor = input()    
            clear()
            main()
    clear()
    print(Fore.RED + f"Danie '{danie}' nie istnieje")
    znajdz_kcal()

def znajdz_dania():
    print(Fore.YELLOW + "ZNAJDŹ DANIA PO KALORYCZNOSCI")
    print()
    kcal = input("Podaj kaloryczność dania, które chcesz znaleźć: ")
    found = False
    for dania, dania_kcal in katalog.items():
        if str(dania_kcal) == kcal:
            print(Fore.GREEN + f"Danie: {dania}    Kalorie: {dania_kcal}")
            found = True
    if found:
        print(Fore.LIGHTBLACK_EX + "Naciśnij dowolnym klawisz, aby wrócić, aby wyłączyć program.")
        wybor = input()    
        clear()
        main()
    else:
        clear()
        print(Fore.RED + f"Nie znaleziono dania o kaloryczności {kcal}")
        znajdz_dania()


def zamknij():
    quit()




katalog = {
    "Kotlet schabowy": "300",
    "Zupa pomidorowa": "120",
}


def main():
    
    wybor = menu()
    if wybor == '1':
        clear()
        wyswietl_dania()
    elif wybor == '2':
        clear()
        dodaj_danie()
    elif wybor == '3':
        clear()
        usun_danie()
    elif wybor == '4':
        clear()
        znajdz_kcal()
    elif wybor == '5':
        clear()
        znajdz_dania()
    elif wybor == '6':
        zamknij()


clear()
main()
