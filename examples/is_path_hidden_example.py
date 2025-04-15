from pyfunc2.file.is_path_hidden import is_path_hidden

if __name__ == "__main__":
    # Przykład: sprawdzenie czy ścieżka jest ukryta
    filepath = "./.hidden_folder/visible_file.txt"
    result = is_path_hidden(filepath)
    print(f"is_path_hidden('{filepath}') = {result}")
