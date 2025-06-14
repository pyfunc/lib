from pyfunc2.ml.create_function_by_text import create_function_by_text

if __name__ == "__main__":
    # Przykład: generowanie funkcji na podstawie tekstu
    text = "Zwróć sumę dwóch liczb."
    result = create_function_by_text(text)
    print(f"create_function_by_text: {result}")
