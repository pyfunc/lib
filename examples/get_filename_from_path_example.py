from pyfunc2.file.get_filename_from_path import get_filename_from_path

if __name__ == "__main__":
    # Przykład: wyciąganie nazwy pliku z pełnej ścieżki
    path = "/home/tom/test_folder/example.txt"
    fname = get_filename_from_path(path)
    print(f"get_filename_from_path: {fname}")
