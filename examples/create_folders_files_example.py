from pyfunc2.markdown.create_folders_files import create_folders_files

if __name__ == "__main__":
    # Przykład: utwórz foldery i pliki na podstawie słownika
    structure = {
        "docs": ["intro.md", "usage.md"],
        "src": ["main.py", "utils.py"]
    }
    create_folders_files(structure)
    print(f"create_folders_files: utworzono strukturę {structure}")
