import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Desktop/secretKey.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("Story_Slips_(Responses)")
sheet = workbook.sheet1
 
print(sheet.row_values("2"))