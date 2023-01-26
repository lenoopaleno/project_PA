import curses
from curses.textpad import Textbox

screen = curses.initscr()
screen.keypad(1)
katalog = {
    "Zupa pomidorowa": "120",
    "Schabowy": "300",
    "Hot-dog": "120",
    "Pizza": "300",
    "Owsianka": "120",
    "Kurczak": "300",
}





def wyswietl_katalog(ticker, maxY, maxX):
    screen.clear()
    screen.border('|', '|', '-', '-', '+', '+', '+', '+')
    screen.addstr(2, 50, "Katalog dań i ich kaloryczności:")
    for i in katalog:
        screen.addstr(ticker, 10, i + " " + katalog[i])
        ticker = ticker + 1
    screen.addstr(int(maxY - 2), int((maxX/2) - 25), "Naciśnij dowolny klawisz, aby wrócić do menu")
    key = screen.getch()
    if key:
        main()

def dodaj_danie():
    screen.clear()
    screen.border('|', '|', '-', '-', '+', '+', '+', '+')
    screen.addstr(2, 50, "Dodaj danie do katalogu")
    screen.addstr(4, 4, "Danie: ")
    win = curses.newwin(1,30,4,10)
    box = Textbox(win)
    screen.refresh()
    box.edit()
    screen.getch()

    text = box.gather()
    

    


def main():
    maxY, maxX = screen.getmaxyx()
    maxY = int(maxY)
    maxX = int(round(maxX))
    ticker = 3
    screen.clear()
    screen.border('|', '|', '-', '-', '+', '+', '+', '+')
    screen.addstr(2, 35, "Witaj w katalogu wyności, który przedstawi Ci potrawy i ich kalorie w 100g!")
    screen.addstr(3,50, "Poniej przedstawione są mozliwe opcje.")
    screen.addstr(6, 10, "1. Wyświetl zawartość katalogu")
    screen.addstr(7, 10, "2. Dodaj do katalogu")
    screen.addstr(8, 10, "3. Usuń z katalogu")
    screen.addstr(9, 10, "4. Znajdź i wyświetl dane danie")
    screen.addstr(10, 10, "5. Znajdź i wyświetl danie po wartości")
    screen.addstr(11, 10, "6. Zakończ działanie aplikacji")

    key = screen.getch()
    if key == ord("1"):
        wyswietl_katalog(ticker, maxY, maxX)
    elif key == ord("2"):
        dodaj_danie()

    screen.refresh()


main()