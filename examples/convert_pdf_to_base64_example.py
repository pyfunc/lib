from pyfunc2.file.convert_pdf_to_base64 import convert_pdf_to_base64

if __name__ == "__main__":
    # Przykład: konwersja PDF do base64
    pdf_path = "./example_invoice.pdf"  # Podmień na istniejący plik PDF
    try:
        base64_str = convert_pdf_to_base64(pdf_path)
        print(f"convert_pdf_to_base64: wynik base64 (skrócony): {base64_str[:60]}...")
    except Exception as e:
        print(f"Błąd podczas konwersji PDF: {e}")
