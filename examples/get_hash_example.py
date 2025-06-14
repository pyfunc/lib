from pyfunc2.file.get_hash import get_hash

if __name__ == "__main__":
    # Przykład: oblicz hash pliku
    path = "./test_folder/example.txt"  # Upewnij się, że plik istnieje
    try:
        h = get_hash(path)
        print(f"get_hash: {h}")
    except Exception as e:
        print(f"Błąd podczas obliczania hash: {e}")
