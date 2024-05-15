import gspread
from google.oauth2.service_account import Credentials

credentials_file = 'credentials.json'

def authenticate():
   
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    creds = Credentials.from_service_account_file(credentials_file, scopes=scope)
    
    client = gspread.authorize(creds)
    return client
