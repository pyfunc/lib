from pyfunc2.email.download_attachments_in_email import download_attachments_in_email

if __name__ == "__main__":
    # UWAGA: Przykład wymaga prawdziwych danych oraz obiektu email
    resp = None  # odpowiedź z IMAP
    data = None  # dane z IMAP
    emailid = ""
    outputdir = "./attachments/"
    xx = 0
    attachements = ["pdf", "jpg", "gif", "png"]
    # download_attachments_in_email(resp, data, emailid, outputdir, xx, attachements)
    print("download_attachments_in_email: przykład wywołania przygotowany, odkomentuj linię aby wykonać operację na prawdziwych danych.")
