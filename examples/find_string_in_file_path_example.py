from pyfunc2.ocr.find_string_in_file_path import find_string_in_file_path

if __name__ == "__main__":
    # Przykład: wyszukiwanie tekstu w plikach PDF w folderze
    paths = "./example_dir"
    find_text = "OpenAI"
    extension_list = [".pdf"]
    results = find_string_in_file_path(paths, find_text, extension_list)
    print(f"find_string_in_file_path: znaleziono w plikach: {results}")
