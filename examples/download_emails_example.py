from pyfunc2.email.download_emails import download_emails

if __name__ == "__main__":
    # UWAGA: Przykład wymaga prawdziwych danych logowania!
    server = "imap.example.com"
    user = "user@example.com"
    password = "your_password"
    local_folder = "./downloaded_emails"
    remote_folder = "Inbox"
    limit = 5
    # Funkcja pobierze do 5 maili z podanej skrzynki!
    # Skorzystaj ostrożnie!
    # download_emails(server, user, password, local_folder, remote_folder, limit)
    print("download_emails: przykład wywołania przygotowany, odkomentuj linię aby wykonać operację na prawdziwych danych.")
