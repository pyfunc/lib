from pyfunc2.markdown.get_dictionary_structure_from_headers_content import get_dictionary_structure_from_headers_content

if __name__ == "__main__":
    # Przykład: zamiana nagłówków i treści na strukturę słownikową
    headers = ["# Wstęp", "## Instalacja", "## Użycie", "# API"]
    contents = ["Opis", "Jak zainstalować", "Jak używać", "Opis API"]
    structure = get_dictionary_structure_from_headers_content(headers, contents)
    print(f"get_dictionary_structure_from_headers_content: {structure}")
