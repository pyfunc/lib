from pyfunc2.ml.create_functions_based_on_csv import create_functions_based_on_csv

if __name__ == "__main__":
    # Przykład: generowanie funkcji na podstawie CSV
    csv_path = "./example_functions.csv"  # Podmień na istniejący plik CSV
    try:
        result = create_functions_based_on_csv(csv_path)
        print(f"create_functions_based_on_csv: {result}")
    except Exception as e:
        print(f"Błąd podczas generowania funkcji na podstawie CSV: {e}")
