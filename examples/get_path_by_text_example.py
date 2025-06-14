from pyfunc2.ml.get_path_by_text import get_path_by_text

if __name__ == "__main__":
    # Przykład: generowanie ścieżki na podstawie tekstu
    text = "faktury 2025 kwiecień"
    path = get_path_by_text(text)
    print(f"get_path_by_text: {path}")
