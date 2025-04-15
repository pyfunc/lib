from pyfunc2.text.multiple_search import multiple_search

if __name__ == "__main__":
    # Przykład: wyszukiwanie wielu fraz w tekście
    text = "OpenAI tworzy narzędzia AI. Microsoft także rozwija AI."
    patterns = ["OpenAI", "Microsoft", "Google"]
    result = multiple_search(text, patterns)
    print(f"multiple_search: znalezione wzorce: {result}")
