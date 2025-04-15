from pyfunc2.text.remove_extra_spaces import remove_extra_spaces

if __name__ == "__main__":
    # Przykład: usuń nadmiarowe spacje z tekstu
    text = "To   jest   przykładowy    tekst   z   wieloma   spacji."
    result = remove_extra_spaces(text)
    print(f"remove_extra_spaces: '{result}'")
