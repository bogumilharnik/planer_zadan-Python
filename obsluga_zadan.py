import os
import csv

def utworz_folder(sciezka):
    
    directory = os.path.dirname(sciezka)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Utworzono ścieżkę '{directory}'.")
        except OSError as error:
            print(f"Błąd tworzenia ścieżki '{directory}': {error}")
            return False
        return True
    
def wczytaj_liste_zadan():
    
    path_file = input("Podaj ścieżkę do pliku CSV lub nazwę pliku: ")
    lista_zadan = []
    try:
        with open(path_file, 'r', newline='', encoding='utf-8') as plik_csv_f:
            reader = csv.reader(plik_csv_f)
            next(reader)
            for row in reader:
                opis_zadania = row[0]
                kategoria = row[1]
                status = row[2].strip().lower() == 'true'
                lista_zadan.append({"opis": opis_zadania, "kategoria": kategoria, "status": status})
                if lista_zadan:
                    print(f"Lista zadań została wczytana z pliku '{path_file}'.")
                else:
                    print(f"Brak zadań do wczytania z pliku '{path_file}'.")
    except FileNotFoundError as error:
        print(f"Błąd odczytu pliku: {error}")
    except ValueError as error:
        print(f"Błąd danych w pliku: {error}")
    except csv.Error as error:
        print(f"Błąd formatu pliku CSV")
    return lista_zadan

def dodaj_zadania(lista_zadan):
    while True:
        insert = input("Wpisz zadanie w postaci 'Opis, Kategoria, Status' np.: 'Zrobić zakupy, dom, True'. Wpisanie 'stop' kończy: ")
        if insert.strip().lower() == 'stop':
            break
        if not insert.strip():
            print("Nie podano żadnych danych, spróbuj ponownie.")
            continue
        
        czesc = insert.split(", ")
        if len(czesc) != 3:
            print("Niepoprawny format. Podaj dane w formacie: 'Opis, Kategoria, Status'.")
            continue

        opis_zadania = czesc[0]
        kategoria = czesc[1]
        status = czesc[2].strip().lower() == 'true'

        lista_zadan.append({"opis": opis_zadania, "kategoria": kategoria, "status": status})
    

def edytuj_liste_zadan(lista_zadan):
    
    if len(lista_zadan) == 0:
        print("Lista zadań jest pusta.")
        return

    for i, zadanie in enumerate(lista_zadan):
        print(f"{i + 1}. {zadanie['opis']} - {zadanie['kategoria']} - {'Wykonane' if zadanie['status'] else 'Niewykonane'}")

    try:
        numer = int(input("Podaj numer zadania do edycji: ")) - 1

        if numer < 0 or numer >= len(lista_zadan):
            print("Błąd: Nie ma takiego numeru.")
            return

        nowy_opis = input("Podaj nowy opis: ").strip()
        if not nowy_opis:
            print("Błąd: Opis nie może być pusty.")
            return
        nowa_kategoria = input("Podaj nową kategorię: ").strip()
        if not nowa_kategoria:
            print("Błąd: Kategoria nie może być pusta.")
            return
        nowy_status = input("Podaj nowy status: ").strip().lower() == 'true'
        if nowy_status not in ['true', 'false']:
            print("Błąd: Status musi być 'True' lub 'False'.")
            return
        
        lista_zadan[numer] = {"opis": nowy_opis,"kategoria": nowa_kategoria,"status": nowy_status}
        print("Zadanie zostało zaktualizowane.")

    except ValueError:
        print("Błąd: Nieprawidłowy numer zadania.")
        
def usun_zadanie(lista_zadan):
   
    if not lista_zadan:
        print("Lista zadań jest pusta.")
        return

    for i, zadanie in enumerate(lista_zadan):
        print(f"{i + 1}. {zadanie['opis']} - {zadanie['kategoria']} - {'Wykonane' if zadanie['status'] else 'Niewykonane'}")

    try:
        numer = int(input("Podaj numer zadania do usunięcia: ")) - 1

        if numer < 0 or numer >= len(lista_zadan):
            print("Błąd: Nie ma takiego numeru.")
            return

        usuniety = lista_zadan.pop(numer)
        print(f"Usunięto zadanie: {usuniety['opis']} - {usuniety['kategoria']} - {'Wykonane' if usuniety['status'] else 'Niewykonane'}")

    except ValueError:
        print("Błąd: Nieprawidłowy numer.")
        
def save_to_txt(plik_txt, lista_zadan):
    
    if not utworz_folder(plik_txt):
        return

    try:
        with open(plik_txt, 'w', encoding='utf-8') as plik:
            for zadanie in lista_zadan:
                plik.write(f"{zadanie['opis']} - {zadanie['kategoria']} - {'Wykonane' if zadanie['status'] else 'Niewykonane'}\n")
            
        print(f"Zapisano raport do pliku '{plik_txt}'.")
    except IOError as error:
        print(f"Błąd zapisu pliku: {error}")


def save_to_csv(plik_csv, lista_zadan):
    
    if not utworz_folder(plik_csv):
        return

    try:
        with open(plik_csv, 'w', newline='', encoding='utf-8') as plik_csv_f:
            writer = csv.writer(plik_csv_f)
            writer.writerow(['opis', 'kategoria', 'status'])

            for zadanie in lista_zadan:
                writer.writerow([zadanie['opis'], zadanie['kategoria'], zadanie['status']])

        print(f"Zapisano dane do pliku '{plik_csv}'.")
    except IOError as error:
        print(f"Błąd zapisu pliku: {error}")