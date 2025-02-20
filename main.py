from obsluga_zadan import utworz_folder, dodaj_zadania, edytuj_liste_zadan, usun_zadanie, save_to_txt, save_to_csv

plik_txt = input("Podaj pełną ścieżkę do pliku TXT (z rozszerzeniem .txt): ")
plik_csv = input("Podaj pełną ścieżkę do pliku CSV (z rozszerzeniem .csv): ")

save_to_txt(plik_txt, opis_zadania, kategoria, status)
save_to_csv(plik_csv, lista_wydatkow)

lista_zadan = lista_zadan()

while True:  
    print("1. Wczytaj listę zadań z pliku"\n)
    print("2. Dodaj zadanie"\n)
    print("3. Edytuj zadanie"\n)
    print("4. Usuń zadanie"\n)
    print("5. Pokaż raport"\n)
    print("6. Zapisz raport do TXT"\n)
    print("7. Zapisz wydatki do CSV"\n)
    print("0. Wyjście")

    wybor = input("Wybierz opcję: ")
    
    if wybor == '1':
        # wywołaj funkcję do wczytania pliku
 
        
    elif wybor == '2':
        # wywołaj funkcję do dodawania zadania
 
    
    elif wybor == '3':
        # wywołaj funkcję do edycji zadania
 
    
    elif wybor == '4':
        # wywołaj funkcję do usunięcia zadania
 
    
    elif wybor == '5':
 

    
    elif wybor == '6':
        
    
    elif wybor == '7':
        # zapisz zadania do csv

    elif wybor == '8':
        # zapisz zadania do txt

    elif wybor == '0':  # Wyjście – kończymy pętlę
        print("Kończę program.")
        break

    else:
        print("Nie ma takiej opcji, spróbuj ponownie.")