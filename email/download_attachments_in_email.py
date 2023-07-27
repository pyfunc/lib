import email

def download_attachments_in_email(m, emailid="", outputdir="", xx=1):
    #m.store(emailid, '+FLAGS', '\Seen')
    print("download_attachments_in_email emailid:", emailid)
    print("download_attachments_in_email outputdir:", outputdir)
    print("download_attachments_in_email xx:", xx)

    resp, data = m.fetch(str(emailid), "(BODY.PEEK[])")
    print("mail emailid:", emailid)
    #resp, data = m.fetch(emailid, '(RFC822)')
    print("mail respo:", resp)

    email_body = data[0][1]
    mail = email.message_from_bytes(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            try:
                open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))
                #print(part.get_filename())
            except TypeError as ex:
                #open(outputdir + '/' + str(xx) + ".txt", 'wb').write(part.get_payload(decode=True))
                open(outputdir + '/' + str(xx) + ".html", 'wb').write(part.get_payload(decode=True))
            except FileNotFoundError as ex:
                filename = str(xx)
                for character in part.get_filename():
                    if character.isalnum():
                        filename += character
                open(outputdir + '/' + filename + ".txt", 'wb').write(part.get_payload(decode=True))
            #toLowerCase(string):

