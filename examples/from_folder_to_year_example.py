from pyfunc2.ocr.from_folder_to_year import from_folder_to_year

if __name__ == "__main__":
    # Przykład: wyszukiwanie dat w plikach PDF w folderze
    path = "./example_dir"
    result = from_folder_to_year(path)
    print(f"from_folder_to_year: znalezione daty: {result}")
