from pyfunc2.file.check_and_create_path import check_and_create_path

if __name__ == "__main__":
    # Przykład: tworzenie nowego katalogu
    dest_path = "./test_folder"
    check_and_create_path(dest_path)
    print(f"check_and_create_path: sprawdzono/stworzono {dest_path}")
