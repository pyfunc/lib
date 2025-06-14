from pyfunc2.ml.get_filename_by_text import get_filename_by_text

if __name__ == "__main__":
    # Przykład: generowanie nazwy pliku na podstawie tekstu
    text = "raport sprzedaży za kwiecień 2025"
    filename = get_filename_by_text(text)
    print(f"get_filename_by_text: {filename}")
