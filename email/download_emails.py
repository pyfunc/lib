import sys

sys.path.append('../')
import os
import logging
import imaplib
import datetime
import email
from pyfunc.email.download_attachments_in_email import download_attachments_in_email


def download_emails(server, user, password, local_folder, remote_folder="inbox", limit=50, select_month=0, year=0):
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

    # date_to = datetime.date.today().month
    if year == 0:
        year = datetime.date.today().year

    if select_month > 0 and select_month < 13:
        year_from = year
        date_from_month = select_month - 1
        if select_month < 2:
            year_from = year - 1
            date_from_month = 12

        date_to = datetime.datetime(year, select_month, 1).strftime("%d-%b-%Y")
        date_from = datetime.datetime(year_from, date_from_month, 1).strftime("%d-%b-%Y")
        # date_from = (datetime.date.today() - datetime.timedelta(days)).strftime("%d-%b-%Y")
        print("date_from:", date_from)
        print("date_to:", date_to)
        # exit()
        # response, items = m.search(None, 'ALL', f'(SENTSINCE {datesince})')
        # response, items = m.search(None, f'(SINCE "{date_from}")')
        response, items = m.search(None, f'(SINCE "{date_from}" BEFORE "{date_to}")')
        print("response search:", response)
    else:
        response, items = m.search(None, 'ALL')

    xx = 0
    items = items[0].split()
    for emailid in items:
        resp, data = m.fetch(emailid, '(RFC822)')
        download_attachments_in_email(resp, data, emailid, local_folder)

        # print(emailid, local_folder)
        xx = xx + 1
        if limit > 0:
            if xx > limit:
                exit()
