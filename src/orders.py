import os
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from smolagents import tool
load_dotenv()

# Google sheet credentials
def get_google_credentials():
    credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]
    return Credentials.from_service_account_file(
        credentials_path,
        scopes=scopes,
    )
# Connect once when the module loads
credentials = get_google_credentials()
client = gspread.authorize(credentials)
spreadsheet_id = os.getenv("GOOGLE_SHEET_ID")
spreadsheet = client.open_by_key(spreadsheet_id)
worksheet = spreadsheet.worksheet("Orders")
print("Google Sheets connected successfully!")

# Order info
def get_order(order_id: str):
    records = worksheet.get_all_records()
    for order in records:
        if order["order_id"] == order_id:
            return order

    return f"Order {order_id} was not found."
