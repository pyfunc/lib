from pyfunc2.file.is_file_hidden import is_file_hidden

if __name__ == "__main__":
    # Przykład: sprawdzenie czy plik jest ukryty
    filepath = ".hidden_file"
    result = is_file_hidden(filepath)
    print(f"is_file_hidden('{filepath}') = {result}")
