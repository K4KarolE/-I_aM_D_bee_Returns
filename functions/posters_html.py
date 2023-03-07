import os
import json
from pathlib import Path
import webbrowser
from functions import settings
# import settings  #testing


def compose():
    settings_data = settings.open_settings()
    if settings_data['poster_open_in_new_tab'] == 1:
        # PATH
        functions_directory = os.path.dirname(__file__)     # os.path.dirname(__file__) = D:\_DEV\Python\31_I_aM_D_bee\functions   //in my case
        main_directory = functions_directory.replace("functions",'')
        path__poster_links_json = Path(main_directory, "json", "poster_links.json")
        path_posters_temp_html = Path(main_directory, "html", "posters_template.html")       # Path functions makes the path OS independent
        path_posters_html = Path(main_directory, "html", "posters.html") 

        # OPEN HTML TEMP
        poster_template = open(path_posters_temp_html)
        list_poster_template = list(poster_template)

        # FINDING THE INDEX IN THE LIST
        # n=0
        # for i in range(len(list_poster_template)):
        #     print(n, list_poster_template[i])
        #     n+=1
        # print(list_poster_template[7])
        # print(list_poster_template[10])

        # TITLE
        list_poster_template[7] = settings_data['title']

        # OPEN POSTER LINKS.JSON
        f = open(path__poster_links_json)
        poster_links_list = json.load(f)

        ## BODY COMPILING
        # POSTER SIZE
        if settings_data['poster_size'] == "Small":
            poster_per_row = 4
        if settings_data['poster_size'] == "Medium":
            poster_per_row = 3
        if settings_data['poster_size'] == "Large":
            poster_per_row = 1

        element_index = 10
        list_poster_template[element_index] = '<div align="center">'
        counter = 1
        for index, item in enumerate(poster_links_list):
            list_poster_template[element_index] += f'<img src={item} hspace="20">'
            if index != 0 and counter % poster_per_row == 0:
                list_poster_template[element_index] += '</div><br><div align="center">'
            if index+1 == len(poster_links_list):
                list_poster_template[element_index] += '</div>'
            counter += 1

        # EXAMPLE
        # '<div align="center"><img src="https://image.tmdb.org/t/p/w200/wAv2tBzcTlzrRIKlM7s2cjnpxwA.jpg" hspace="20"><img src="https://image.tmdb.org/t/p/w200/wAv2tBzcTlzrRIKlM7s2cjnpxwA.jpg"></div>'

        # SAVING HTML
        file = open(path_posters_html, 'w')
        for i in list_poster_template:
            file.write(i)
        file.close()

        # OPEN POSTER PAGE
        webbrowser.open(path_posters_html)

# compose()  #testing
