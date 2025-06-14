from pyfunc2.email.delete_emails import delete_emails

if __name__ == "__main__":
    # UWAGA: Przykład wymaga prawdziwych danych logowania!
    email = "user@example.com"
    password = "your_password"
    mailserver = "imap.example.com"
    mailbox = "Inbox"
    mailtrash = "Trash"
    last_messages = 10
    # Funkcja usunie ostatnie 10 maili z podanej skrzynki!
    # Skorzystaj ostrożnie!
    # delete_emails(email, password, mailserver, mailbox, mailtrash, last_messages)
    print("delete_emails: przykład wywołania przygotowany, odkomentuj linię aby wykonać operację na prawdziwych danych.")
