from pyfunc2.file.check_and_create_path_from_filepath import check_and_create_path_from_filepath

if __name__ == "__main__":
    # Przykład: tworzenie katalogu na podstawie ścieżki do pliku
    dest_path = "./test_folder/example.txt"
    check_and_create_path_from_filepath(dest_path)
    print(f"check_and_create_path_from_filepath: sprawdzono/stworzono katalog dla {dest_path}")
