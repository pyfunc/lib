from pyfunc2.csv.load_csv_pandas import load_csv_pandas

if __name__ == "__main__":
    # Przykład: wczytaj plik csv do pandas DataFrame
    filename = "./test_folder/example.csv"  # Upewnij się, że plik istnieje
    try:
        rows = list(load_csv_pandas(filename))
        print(f"load_csv_pandas: pierwsze 3 wiersze: {rows[:3]}")
    except Exception as e:
        print(f"Błąd podczas wczytywania CSV: {e}")
