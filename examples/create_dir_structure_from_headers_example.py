from pyfunc2.markdown.create_dir_structure_from_headers import create_dir_structure_from_headers

if __name__ == "__main__":
    # Przykład: utwórz strukturę katalogów na podstawie nagłówków markdown
    headers = ["# Wstęp", "## Instalacja", "## Użycie", "# API"]
    create_dir_structure_from_headers(headers)
    print(f"create_dir_structure_from_headers: utworzono strukturę dla nagłówków: {headers}")
