from pyfunc2.file.remove_duplicates_in_path import remove_duplicates_in_path

if __name__ == "__main__":
    # Przykład: znajdź i wypisz duplikaty w folderze 'source' względem folderu 'duplicated'
    source = "./example_source"
    duplicated = "./example_duplicated"
    remove_duplicates_in_path(source, duplicated)
    print(f"remove_duplicates_in_path: sprawdzono {source}, duplikaty względem {duplicated}")
