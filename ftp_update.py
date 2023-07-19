from pyfunc.ftp_download import ftp_download
from pyfunc.get_ftp_path import get_ftp_path

def ftp_update(ftps):
    for ftp in ftps:
        data_path = get_ftp_path(ftp)
        ftp_download(ftp["server"], ftp["username"], ftp["password"], data_path, ftp["source"])

