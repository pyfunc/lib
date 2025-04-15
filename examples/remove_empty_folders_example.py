from pyfunc2.file.remove_empty_folders import remove_empty_folders

if __name__ == "__main__":
    # Przykład: usuń puste katalogi w podanej ścieżce
    path_abs = "./example_dir"
    remove_empty_folders(path_abs)
    print(f"remove_empty_folders: sprawdzono/usunięto puste katalogi w {path_abs}")
