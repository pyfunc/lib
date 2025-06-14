from pyfunc2.csv.load_csv_with_comma_quotas import load_csv_with_comma_quotas

if __name__ == "__main__":
    # Przykład: wczytaj plik CSV z cudzysłowami i przecinkami
    filename = "./test_folder/example.csv"  # Upewnij się, że plik istnieje
    try:
        rows = load_csv_with_comma_quotas(filename)
        print(f"load_csv_with_comma_quotas: pierwsze 3 wiersze: {rows[:3]}")
    except Exception as e:
        print(f"Błąd podczas wczytywania CSV: {e}")
