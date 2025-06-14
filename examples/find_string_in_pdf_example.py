from pyfunc2.ocr.find_string_in_pdf import find_string_in_pdf

if __name__ == "__main__":
    # Przykład: wyszukiwanie tekstu w pojedynczym pliku PDF
    file_path = "./example_invoice.pdf"  # Podmień na istniejący plik PDF
    find_text = "OpenAI"
    try:
        found_text = find_string_in_pdf(file_path, find_text)
        print(f"find_string_in_pdf: znaleziono: {found_text}")
    except Exception as e:
        print(f"Błąd podczas przetwarzania PDF: {e}")
