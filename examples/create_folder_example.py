from pyfunc2.file.create import create_folder

if __name__ == "__main__":
    path = "./example_created_folder"
    create_folder(path)
    print(f"create_folder: sprawdzono/stworzono {path}")
