import webbrowser
from functions import settings      # when you call it outside functions folder
# import settings                   # learning Python - when you run/test it from insinde functions folder

def search(titleRead, yearRead):
    settings_data = settings.open_settings()
    if settings_data['title_search'] == 1:
        selected_default_link = settings_data['title_search_links'][settings_data['title_search_link_selected']]    # settings_db.json / 'title_search_links' dictionary looking for the 
        link = selected_default_link + ' '.join([titleRead, yearRead])                                              # saved value(link) of the key: Hungarian or Czech..
        webbrowser.open(link)

## TEST
# use /import settings/ instead of /from functions import settings/
# search("My Cousin Vinny","1992")
