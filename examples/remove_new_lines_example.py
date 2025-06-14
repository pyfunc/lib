from pyfunc2.text.remove_new_lines import remove_new_lines

if __name__ == "__main__":
    # Przykład: usuń znaki nowej linii z tekstu
    text = "To jest tekst\nz nową linią\ni jeszcze jedną."
    result = remove_new_lines(text)
    print(f"remove_new_lines: '{result}'")
