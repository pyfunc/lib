import os
from pyfunc.email_update import email_update
from pyfunc.config.ftp_update import ftp_update

def lasts(image_path, limit=3, emails=[], ftps=[], storage_root=""):
    #email_brama()
    #email_office()
    email_update(emails, storage_root, limit)
    ftp_update(ftps, storage_root, limit)
    images = os.listdir(image_path)
    images.sort(key=lambda x: os.path.getmtime(os.path.join(image_path, x)))
    images.reverse()
    return images[:int(limit)]
