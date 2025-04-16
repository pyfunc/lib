from pyfunc2.markdown.get_header_list import get_header_list

if __name__ == "__main__":
    # Przykład: pobierz listę nagłówków z tekstu markdown
    markdown_text = """# Wstęp\n## Instalacja\n## Użycie\n# API"""
    headers = get_header_list(markdown_text)
    print(f"get_header_list: {headers}")
