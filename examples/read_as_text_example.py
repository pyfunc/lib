from pyfunc2.file.read_as_text import read_as_text

if __name__ == "__main__":
    # Przykład: czytanie pliku jako tekst
    path = "./test_folder/example.txt"  # Upewnij się, że plik istnieje
    try:
        text = read_as_text(path)
        print(f"read_as_text: {text[:60]}...")
    except Exception as e:
        print(f"Błąd podczas czytania pliku: {e}")
