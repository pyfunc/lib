from pyfunc2.config.get_email_path import get_email_path

if __name__ == "__main__":
    # Przykład: pobierz ścieżkę e-maila
    email = "user@example.com"
    storage_root = "/home/tom/storage"
    result = get_email_path(email, storage_root)
    print(f"get_email_path: {result}")
