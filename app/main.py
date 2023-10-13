import os.path

from dotenv import load_dotenv

from GoogleSheet import GoogleSheet

load_dotenv()

SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
sheet = GoogleSheet(spreadsheet_id=SPREADSHEET_ID, scopes=SCOPES)
