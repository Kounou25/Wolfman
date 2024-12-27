import imapclient
from email import message_from_bytes

#import pyzmail

#function for connection to the email account
def mail_connection(email,password):
    server = imapclient.IMAPClient('imap.gmail.com',ssl=True)
    server.login(email,password)
    print('connextion etablie avec succes !')
    return server

#function that count emails from a document
def count_mails(label,filter):
    fetch= server.select_folder(label)
    emails = server.search([filter])
    return emails

#folders lists

def folders_list():
    folders = server.list_folders()
    for folder in folders:
        print(folder[-1])

#function that fetch mails object ans date
def fetch_mails():
    for email_id in emails:
        #on recupere l'email brut d'abord
        brut_email_data = server.fetch(email_id, ['BODY.PEEK[]'])[email_id][b'BODY[]']
        #convertir les donnees brut des emails en objets
        processed_email_data = message_from_bytes(brut_email_data)

        #maintenant je recupere les données souhaité des emails exemple: objets,contenu etc...
        email_subject = processed_email_data["subject"]
        receive_date = processed_email_data["date"]
        sender= processed_email_data["from"]
        print(f"objet : {email_subject}")
        print(f"expediteur : {sender}")
        print(f"objet : {receive_date}\n\n")


    


    

email = "kounougilbert288@gmail.com"
password = "wacp viuy kqdj cdyx"
filter_list =['ALL','SINCE','01-oct-2024']
server = mail_connection(email,password)
emails = count_mails('[Gmail]/Spam',filter_list)
print('nombre d\'email trouvé',len(emails))
fetch_mails()
#folders_list()