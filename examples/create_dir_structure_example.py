from pyfunc2.markdown.create_dir_structure import create_dir_structure

if __name__ == "__main__":
    # Przykład: utwórz strukturę katalogów na podstawie listy ścieżek
    paths = ["docs/intro", "docs/usage", "docs/api"]
    create_dir_structure(paths)
    print(f"create_dir_structure: utworzono katalogi {paths}")
