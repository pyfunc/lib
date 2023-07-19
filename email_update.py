from pyfunc.mail import downloadAllAttachmentsInInbox
from pyfunc.get_email_path import get_email_path

def email_update(emails):
    for email in emails:
        data_path = get_email_path(email)
        downloadAllAttachmentsInInbox(email["server"], email["username"], email["password"], data_path)
