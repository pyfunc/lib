from pyfunc2.file.file_list import file_list

if __name__ == "__main__":
    # Przykład: wypisz pliki w katalogu
    path = "."
    files = file_list(path)
    print(f"file_list: {files}")
