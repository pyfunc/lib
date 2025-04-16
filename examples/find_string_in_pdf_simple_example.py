from pyfunc2.ocr.find_string_in_pdf import find_string_in_pdf

if __name__ == "__main__":
    # Przykład: wyszukiwanie tekstu w PDF
    pdf_path = "./example_invoice.pdf"  # Podmień na istniejący plik PDF
    search_text = "faktura"  # Podmień na szukany tekst
    try:
        results = find_string_in_pdf(pdf_path, find_text=search_text)
        print(f"find_string_in_pdf: znalezione fragmenty: {results}")
    except Exception as e:
        print(f"Błąd podczas wyszukiwania tekstu w PDF: {e}")
