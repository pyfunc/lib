from pyfunc2.ocr.get_date_from_pdf import get_date_from_pdf

if __name__ == "__main__":
    # Przykład: wyciąganie daty z pliku PDF
    file_path = "./example_invoice.pdf"  # Podmień na istniejący plik PDF
    try:
        date = get_date_from_pdf(file_path)
        print(f"get_date_from_pdf: znaleziono datę: {date}")
    except Exception as e:
        print(f"Błąd podczas przetwarzania PDF: {e}")
