import os
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

# Credentials
def get_google_credentials():
    credentials_path=os.getenv("GOOGLE_CREDENTIALS_PATH")
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
    ]
    credentials = Credentials.from_service_account_file(
    credentials_path,
    scopes=scopes
    )
    return credentials

print("Credentials loaded successfully!")

# Google sheet connection
def connect_to_sheets():
    credentials = get_google_credentials()
    client = gspread.authorize(credentials)
    spread_sheet_name = os.getenv("GOOGLE_SHEET_NAME")
    spread_sheat = client.open(spread_sheet_name)
    worksheet = spread_sheat.worksheet("orders")
    return worksheet

worksheet = connect_to_sheets()
print(f"Connected to worksheet: {worksheet.title}")
