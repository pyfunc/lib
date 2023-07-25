import sys
sys.path.append('../')

from pyfunc.email.download_attachments_in_email import download_attachments_in_email

# Download all the attachment files for all emails in the inbox.
def download_all_attachments_in_inbox(server, user, password, outputdir, remote_folder="inbox"):
    m = connect(server, user, password, remote_folder)
    resp, items = m.search(None, "(ALL)")
    #resp, items = m.search(None, 'ALL')
    #resp, items = m.search(None, "(UNSEEN)")
    xx=0
    items = items[0].split()
    for emailid in items:
        download_attachments_in_email(m, emailid, outputdir)
        print(emailid, outputdir)
        xx=xx+1
        #if xx>40: exit()
