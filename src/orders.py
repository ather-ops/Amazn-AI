import os

import gspread
import streamlit as st

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials


load_dotenv()


def get_google_credentials():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    # Try Streamlit Secrets first.
    try:
        service_account = st.secrets["gcp_service_account"]

        return Credentials.from_service_account_info(
            dict(service_account),
            scopes=scopes,
        )

    except st.errors.StreamlitSecretNotFoundError:
        # No local secrets.toml
        pass

    except KeyError:
        # secrets.toml exists, but gcp_service_account is missing
        pass

    # Local development
    credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")

    if not credentials_path:
        raise ValueError(
            "Google credentials not found. "
            "Set GOOGLE_CREDENTIALS_PATH in .env "
            "or configure gcp_service_account in Streamlit Secrets."
        )

    return Credentials.from_service_account_file(
        credentials_path,
        scopes=scopes,
    )


credentials = get_google_credentials()

client = gspread.authorize(credentials)

# Streamlit Cloud
try:
    spreadsheet_id = st.secrets["GOOGLE_SHEET_ID"]
except (st.errors.StreamlitSecretNotFoundError, KeyError):
    # Local
    spreadsheet_id = os.getenv("GOOGLE_SHEET_ID")

if not spreadsheet_id:
    raise ValueError("GOOGLE_SHEET_ID not found.")

spreadsheet = client.open_by_key(spreadsheet_id)

worksheet = spreadsheet.worksheet("Orders")

print("Google Sheets connected successfully!")

orders = worksheet.get_all_records()


def get_order(order_id: str):
    for order in orders:
        if order["order_id"] == order_id:
            return order

    return f"Order {order_id} was not found."

print("All works perfectly!")
