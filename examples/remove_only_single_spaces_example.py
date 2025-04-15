from pyfunc2.text.remove_only_single_spaces import remove_only_single_spaces

if __name__ == "__main__":
    # Przykład: usuń pojedyncze spacje z tekstu
    text = "To jest przykładowy tekst z pojedynczymi spacjami."
    result = remove_only_single_spaces(text)
    print(f"remove_only_single_spaces: '{result}'")
