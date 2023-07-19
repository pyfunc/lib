import sys
sys.path.append('../')

from pyfunc.lasts import lasts
from pyfunc.get_email_path import get_email_path
from pyfunc.get_ftp_path import get_ftp_path

def all_lasts(lines, emails=[], ftps=[]):
    for email in emails:
        images = images + lasts(get_email_path(email), int(lines), emails, ftps)

    for ftp in ftps:
        images = images + lasts(get_ftp_path(ftp), int(lines), emails, ftps)
