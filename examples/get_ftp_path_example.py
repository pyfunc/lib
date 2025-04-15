from pyfunc2.config.get_ftp_path import get_ftp_path

if __name__ == "__main__":
    # Przykład: pobierz ścieżkę FTP
    ftp = "ftp.example.com"
    storage_root = "/home/tom/storage"
    result = get_ftp_path(ftp, storage_root)
    print(f"get_ftp_path: {result}")
