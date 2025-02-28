from obsluga_zadan import utworz_folder, dodaj_zadania, edytuj_liste_zadan, usun_zadanie, save_to_txt, save_to_csv, save_to_json, wczytaj_liste_zadan
import json
import os

lista_zadan = []


while True:  
    print("1. Wczytaj listę zadań z pliku\n")
    print("2. Dodaj zadanie\n")
    print("3. Edytuj zadanie\n")
    print("4. Usuń zadanie\n")
    print("5. Pokaż raport\n")
    print("6. Zapisz raport do TXT\n")
    print("7. Zapisz wydatki do CSV\n")
    print("0. Wyjście")

    wybor = input("Wybierz opcję: ")
    
    if wybor == '1':
        # wywołaj funkcję do wczytania pliku
        nowe_zadania = wczytaj_liste_zadan()
        if nowe_zadania:
            lista_zadan.extend(nowe_zadania)
        
    elif wybor == '2':
        # wywołaj funkcję do dodawania zadania
        dodaj_zadania(lista_zadan)
    
    elif wybor == '3':
        # wywołaj funkcję do edycji zadania
        edytuj_liste_zadan(lista_zadan)
    
    elif wybor == '4':
        # wywołaj funkcję do usunięcia zadania
        usun_zadanie(lista_zadan)
    
    elif wybor == '5':
        if not lista_zadan:
            print("***********************")
            print("\nLista zadań jest pusta.\n")
            print("***********************\n")
        else:
            for zadanie in lista_zadan:
                print(f" - {zadanie['opis']} ({zadanie['kategoria']}) – {'Wykonane' if zadanie['status'] else 'Niewykonane'}")

    elif wybor == '6':
        plik_txt = input("Podaj pełną ścieżkę do pliku TXT (z rozszerzeniem .txt): ")
        save_to_txt(plik_txt, lista_zadan)        
    
    elif wybor == '7':
        # zapisz zadania do csv
        plik_csv = input("Podaj pełną ścieżkę do pliku CSV (z rozszerzeniem .csv): ")
        save_to_csv(plik_csv, lista_zadan)

    elif wybor == '8':
        # zapisz zadania do txt
        plik_json = input("Podaj pełną ścieżkę do pliku JSON (z rozszerzeniem .json): ")
        save_to_json(plik_json, lista_zadan)

    elif wybor == '0':  # Wyjście – kończymy pętlę
        print("Kończę program.")
        
        if lista_zadan:
            decyzja = input("Czy chcesz zapisać zmiany w pliku przed wyjściem? (tak/nie): ").strip().lower()
            if decyzja == "tak":
                plik_csv = input("Podaj pełną ścieżkę do pliku CSV (z rozszerzeniem .csv): ")
                save_to_csv(plik_csv, lista_zadan)
        
        break

    else:
        print("Nie ma takiej opcji, spróbuj ponownie.")
        


