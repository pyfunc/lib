from pyfunc2.file.dir_list import dir_list

if __name__ == "__main__":
    # Przykład: wypisz podkatalogi w katalogu
    path = "."
    dirs = dir_list(path)
    print(f"dir_list: {dirs}")
