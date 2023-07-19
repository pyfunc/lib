import os
from pyfunc.email_update import email_update
from pyfunc.ftp_update import ftp_update

def lasts(image_path, limit=18, emails=[], ftps=[]):
    #email_brama()
    #email_office()
    email_update(emails)
    ftp_update(ftps)
    images = os.listdir(image_path)
    images.sort(key=lambda x: os.path.getmtime(os.path.join(image_path, x)))
    images.reverse()
    return images[:int(limit)]
