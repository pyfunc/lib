from pyfunc2.ocr.convert_pdf_to_string import convert_pdf_to_string

if __name__ == "__main__":
    # Przykład: konwersja PDF do tekstu
    pdf_path = "./example_invoice.pdf"  # Podmień na istniejący plik PDF
    try:
        text = convert_pdf_to_string(pdf_path)
        print(f"convert_pdf_to_string: {text[:100]}...")
    except Exception as e:
        print(f"Błąd podczas konwersji PDF do tekstu: {e}")
