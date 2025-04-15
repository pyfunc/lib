from pyfunc2.ocr.get_company_from_pdf import get_company_from_pdf

if __name__ == "__main__":
    # Przykład użycia - wymaga pliku PDF oraz listy firm
    file_path = "example_invoice.pdf"  # Podmień na istniejący plik PDF
    company_list = ["OpenAI", "Google", "Microsoft", "Amazon"]
    try:
        companies_found = get_company_from_pdf(file_path, company_list=company_list)
        print(f"Znalezione firmy: {companies_found}")
    except Exception as e:
        print(f"Błąd podczas przetwarzania PDF: {e}")
