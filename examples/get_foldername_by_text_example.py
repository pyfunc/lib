from pyfunc2.ml.get_foldername_by_text import get_foldername_by_text

if __name__ == "__main__":
    # Przykład: generowanie nazwy folderu na podstawie tekstu
    text = "dokumenty księgowe 2025"
    foldername = get_foldername_by_text(text)
    print(f"get_foldername_by_text: {foldername}")
