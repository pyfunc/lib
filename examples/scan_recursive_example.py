from pyfunc2.file.sum_year_from_path_to_file import scan_recursive

if __name__ == "__main__":
    # Przykład: skanowanie katalogu po PDF-ach (lub innych rozszerzeniach)
    path = "./example_dir"
    extension_list = [".pdf"]
    path_out = "./example_report/"
    result = scan_recursive(path, extension_list, path_out)
    print(f"scan_recursive result: {result}")
