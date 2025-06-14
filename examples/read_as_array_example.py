from pyfunc2.file.read_as_array import read_as_array

if __name__ == "__main__":
    # Przykład: czytanie pliku jako tablica linii
    path = "./test_folder/example.txt"  # Upewnij się, że plik istnieje
    try:
        lines = read_as_array(path)
        print(f"read_as_array: {lines}")
    except Exception as e:
        print(f"Błąd podczas czytania pliku: {e}")
