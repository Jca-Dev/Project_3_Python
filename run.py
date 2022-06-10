import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Car-manufacturer-survey')


def get_survey_data():
    """
    Get survey results input from the user.
    
    """
    while True:
        print("Enter results from the most recent survey.")
        print("Data should be ten numbers separated by commas.")
        print("Data must be entered from TOP to BOTTOM of the survey.")
        print("The top number is Audi and the bottom is Pugeot.")
        print("Example: 1,2,0,0,6,1,5,7,0,1\n")

        data_in = input("Enter survey results here:\n")

        survey_data = data_in.split(",")

        print(survey_data)
        break
    return survey_data


def update_scoreboard(data, scoreboard):
    """
    Prints user input to scoreboard.
    """
    print(f"Updating {scoreboard}...\n")
    scoreboard_to_update = SHEET.worksheet(scoreboard)
    scoreboard_to_update.append_row(data)
    print(f"{scoreboard} updated successfully\n")


data = get_survey_data()
survey_data = [int(num) for num in data]
update_scoreboard(survey_data, "scoreboard")
