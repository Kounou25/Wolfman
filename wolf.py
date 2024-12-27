import imapclient
from email import message_from_bytes

#import pyzmail

#function for connection to the email account
def mail_connection(email,password):
    server = imapclient.IMAPClient('imap.gmail.com',ssl=True)
    server.login(email,password)
    print('connextion etablie avec succes !')
    return server

#function that count emails 
def count_mails(label,filter):
    fetch= server.select_folder(label)
    emails = server.search([filter])
    return emails

#folders lists

def folders_list():
    folders = server.list_folders()
    for folder in folders:
        print(folder[-1])

#function that fetch emails informations
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
        reveiver =processed_email_data["To"]
        print(f"objet : {email_subject}")
        print(f"expediteur : {sender}")
        print(f"destinataire : {reveiver}")
        print(f"date : {receive_date}\n\n")


#function that delete emails
def delete_emails():
    delete_them = server.delete_messages(emails)
    if delete_them :
        print(f"{len(emails)} ont été ajouter a la liste de suppression !")

#funtion that purge email deninitively
def purge_emails():
    purge_them = server.expunge()
    if purge_them:
        print(f"{len(emails)} ont été definitivement supprimés !")

    


    

email = "your email here"
password = "your gmail application password"
filter_list =['ALL','SUBJECT','failed']
server = mail_connection(email,password)
emails = count_mails('INBOX',filter_list)
print('nombre d\'email trouvé',len(emails))
#fetch_mails()
#folders_list()
#delete_emails()
#purge_emails()