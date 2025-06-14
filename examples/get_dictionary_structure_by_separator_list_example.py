from pyfunc2.markdown.get_dictionary_structure_by_separator_list import get_dictionary_structure_by_separator_list

if __name__ == "__main__":
    # Przykład: zamiana listy ścieżek na strukturę słownikową
    paths = ["docs/intro.md", "docs/usage.md", "src/main.py"]
    structure = get_dictionary_structure_by_separator_list(paths)
    print(f"get_dictionary_structure_by_separator_list: {structure}")
