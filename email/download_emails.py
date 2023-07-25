import sys

sys.path.append('../')
import os
import logging
import imaplib
import email
from pyfunc.email.download_attachments_in_email import download_attachments_in_email
from pyfunc.email.download_all_attachments_in_inbox import download_all_attachments_in_inbox


def download_emails(server, user, password, local_folder, remote_folder="inbox", limit=0):
    logging.basicConfig(level=logging.DEBUG)
    try:
        m = imaplib.IMAP4_SSL(server)
        m.login(user, password)
    except imaplib.IMAP4.error as ex:
        print(ex)
        logging.debug(ex)
        exit(1)
    print("download_emails:", local_folder, remote_folder)
    # m.select(remote_folder, readonly=False)
    # m.select(remote_folder)
    # m.select()
    # resp, items = m.search(None, 'ALL')
    # items = items[0].split()

    response, data = m.list()
    # print(response)
    # print(data[0])
    # print(data[1:3])
    # response, data = m.select('INBOX.transactions')
    # response, data = m.select('INBOX.estonia')
    # response, data = m.select('INBOX')
    response, data = m.select(remote_folder)
    # response, data = m.select('INBOX.pay')
    print("response:", response)
    print("data:", data)
    # m.select("pay")
    # response, items = m.search(None, "(ALL)")
    response, items = m.search(None, 'ALL')
    print("response search:", response)

    xx = 0
    items = items[0].split()
    for emailid in items:
        download_attachments_in_email(m, emailid, local_folder, xx)
        print(emailid, local_folder)
        xx = xx + 1
        if limit > 0:
            if xx > 40:
                exit()
