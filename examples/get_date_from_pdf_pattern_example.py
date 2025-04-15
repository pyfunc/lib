from pyfunc2.ocr.get_date_from_pdf_pattern import get_date_from_pdf_pattern

if __name__ == "__main__":
    # Przykład: użycie klasy do rozpoznawania wzorców dat w tekście
    text = "Faktura z dnia 15.04.2025"
    pattern_finder = get_date_from_pdf_pattern()
    result = pattern_finder.find_date(text)
    print(f"get_date_from_pdf_pattern: znalezione daty: {result}")
