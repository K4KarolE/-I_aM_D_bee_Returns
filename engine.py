from functions import api
from functions import excel_sheet
from functions import own_language_title

def start_engine():     # executed with the "Save & Start" button click in main

    title, year_of_release, directors, actors, genres, lengthHour, lengthMinute = api.data_collection()

    excel_sheet.write_sheet(title, year_of_release, directors, actors, genres, lengthHour, lengthMinute)

    own_language_title.search(title, year_of_release)

    excel_sheet.launch_sheets()

# start_engine()