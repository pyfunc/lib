from pyfunc2.ocr.from_month_to_company import from_month_to_company

if __name__ == "__main__":
    # Przykład: wyszukiwanie firm w plikach PDF w folderze dla danego miesiąca
    path = "./example_dir"
    result = from_month_to_company(path)
    print(f"from_month_to_company: znalezione firmy: {result}")
