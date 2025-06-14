from pyfunc2.file.find_duplicates import find_duplicates

if __name__ == "__main__":
    # Przykład: znajdź duplikaty w katalogu
    directory = "./example_dir"
    duplicates = find_duplicates(directory)
    print(f"find_duplicates: {duplicates}")
