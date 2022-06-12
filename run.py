from webbrowser import get
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
        print("The first number is Audi and the last is Pugeot.")
        print("Example: 1,2,0,0,6,1,5,7,0,1\n")

        data_in = input("Enter survey results here:\n")

        survey_data = data_in.split(",")

        if validate_data(survey_data):
            print("Data Accepted")
            break

    return survey_data


def update_scoreboard(data, scoreboard):
    """
    Prints user input to scoreboard.
    """
    print(f"Updating {scoreboard}...\n")
    scoreboard_update = SHEET.worksheet(scoreboard)
    scoreboard_update.append_row(data)
    print(f"{scoreboard} updated successfully\n")


def validate_data(values):
    """
    Validate user input data to make sure its within
    set paramaters in order to align with google sheet.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"10 numbers required, You used {len(values)}"
            )
    except ValueError as e:
        print(f"Numbers only: {e}, please try again.\n")
        return False

    return True


def display_results():
    """
    Collects results from worksheet and places into a list.
    Displays list in a table format.
    """
    sheet_instance = SHEET.get_worksheet(0)
    brands = sheet_instance.row_values(1)
    total_numbers = sheet_instance.row_values(2)
    totals = {}
    keys = brands
    values = total_numbers

    for i in range(len(keys)):
        totals[keys[i]] = values[i]

    print('Below are the current totals.\n')

    print("{:<10} {:<15}".format('BRAND', 'TOTAL'))
    for k, value in totals.items():
        content = value
        print("{:<10} {:<15}".format(k, content))


data = get_survey_data()
survey_data = [int(num) for num in data]
update_scoreboard(survey_data, "scoreboard")
display_results()
