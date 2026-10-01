import os
import gspread
from google.oauth2.service_account import Credentials
def get_google_credentials():
    credentials_path=os.getenv("GOOGLE_CREDENTIALS_PATH")
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    credentials = Credentials.from_service_account_file(
    credentials_path,
    scopes=scopes
    )
    return credentials
print("Credentials loaded successfully!")
