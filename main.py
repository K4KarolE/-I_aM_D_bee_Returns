

from tkinter import *
from tkinter import filedialog      # for browse window (adding path)
import tkinter.messagebox           # for pop-up windows

import sys
import platform                     # to check which OS is used
import os
from pathlib import Path

from functions import engine
from functions import settings
settings_data = settings.open_settings()        # access to the saved/default settings (settings_db.json)


# COLORS - FONT STYLE
# IMDb yellow: #E6B91E // original tkinter grey: #F0F0F0 - FYI
skin_selected = settings_data['skin_selected']                                  # example: default
background_color = settings_data['skins'][skin_selected]['background_color']    # example: skins / default / background_color / #E6B91E
field_background_color = settings_data['skins'][skin_selected]['field_background_color'] 
font_style = settings_data['skins'][skin_selected]['font_style']
font_color = settings_data['skins'][skin_selected]['font_color']
window_background_color = settings_data['skins'][skin_selected]['window_background_color']

# OS
os_linux: bool = (sys.platform == 'linux')

# WINDOW
window = Tk()
# window.configure(background=window_background_color) FYI - not necessary / not working if the image background color is set
window.title(settings_data['skins'][skin_selected]['window_title'])
window_width = 500
window_length = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2-200, screen_height/2-250))
window.resizable(0,0)   # locks the main window

# IMAGES
working_directory = os.path.dirname(__file__)     # os.path.dirname(__file__) = D:\_DEV\Python\31_I_aM_D_bee   //in my case
path_image = Path(working_directory, "skins", skin_selected, "BG.png")      # Path functions makes the path OS independent, running the program on Windows: ..skins\default.., on Linux: ..skins/default..)
background_image = PhotoImage(file = path_image)
background_image_label = Label(window, image = background_image, background=window_background_color)
background_image_label.place(x = -2, y = 0)

if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
    window.iconbitmap(path_icon)        # window icon - left, top corner

## CHECKBOXES
checkbox = {
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Posters in a new tab' ],
    'quit': ['quit_after_run', 'quit_after_run_button', 'Quit after run' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ]
}

for item in checkbox.values():
    first_list_item = item[0]                               # we need the titles of first items in the dic. values('imdb_link_in_clipboard'..) in the next line
    item[0] = IntVar(value=settings_data[first_list_item])  # loading the previosly saved values (ticked/unticked) from settings_db.json
    item[1] = Checkbutton(
        window,
        text = item[2],
        variable = item[0], 
        height = 1,
        font = (font_style, 12),
        foreground=font_color,
        background=background_color,
        activeforeground = font_color,
        activebackground=background_color,   # activebackground - color when clicked
        highlightbackground=background_color,
        selectcolor=window_background_color     # background color of the box
        )


## ROLL DOWN MENUS
# SKIN - ROLL DOWN MENU
# highlightbackground - color around the button
# activebackground - color when mouse over or clicked
def change_skin(__):
    settings_data['skin_selected'] = skins_roll_down_clicked.get()  # updating & saving the "skin_selected" value in settings_db.json with every click/skin change
    settings.save_settings(settings_data)
    skin_selected = skins_roll_down_clicked.get()

    # LIST OF WIDGETS TO UPDATE
    #TEXT
    window.title(settings_data['skins'][skin_selected]['window_title'])

    #IMAGES
    path_image = Path(working_directory, "skins", skin_selected, "BG.png")
    background_image.configure(file = path_image)

    if platform.system() == 'Windows': 
        path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
        window.iconbitmap(path_icon)

    ##COLORS
    background_color = settings_data['skins'][skin_selected]['background_color']
    font_color = settings_data['skins'][skin_selected]['font_color']
    window_background_color = settings_data['skins'][skin_selected]['window_background_color']
    
    # WINDOW
    # window.configure(background=window_background_color) FYI - not necessary / not working if the image background color is set
    background_image_label.configure(background=window_background_color)

    # CHECKBOXES
    for item in checkbox.values():
        item[1].configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color, selectcolor=window_background_color)
    
    # ROLL DOWN MENUS
    skins_roll_down.configure(foreground=font_color, background=background_color, activeforeground=font_color, activebackground=background_color, highlightbackground=background_color)
    skins_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=font_color, activeforeground = window_background_color)

    title_search_roll_down.configure(foreground=font_color, background=background_color, activeforeground=font_color, activebackground=background_color, highlightbackground=background_color)
    title_search_roll_down['menu'].configure(foreground=font_color, background=background_color, activeforeground = window_background_color, activebackground=font_color)

    poster_roll_down.config(foreground=font_color, background=background_color, activeforeground=font_color, activebackground=background_color, highlightbackground=background_color)
    poster_roll_down["menu"].config(foreground=font_color, background=background_color, activeforeground = window_background_color, activebackground=font_color)

    # PATH - FIELDS + SEARCHBOXES
    target_sheet_field.configure(foreground=font_color, background=background_color)
    target_sheet_field_title.configure(foreground=font_color, background=background_color)
    target_sheet_button.configure(foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

    # SAVE AND START BUTTON
    button_save_and_start.configure(foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)


skins_options = []
for item in settings_data['skins']:        # creating a list of the SKINS from settings_db.json / skins
    skins_options = skins_options + [item]
skins_options.sort()        #sorts the list ascending

skins_roll_down_clicked = StringVar()
skins_roll_down_clicked.set("Skins")    
skins_roll_down = OptionMenu( window, skins_roll_down_clicked, *skins_options, command=change_skin)     
skins_roll_down.configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
skins_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=font_color, activeforeground = window_background_color)

# TITLE SEARCH - ROLL DOWN MENU
title_search_options = []
for item in settings_data['title_search_links']:
    title_search_options = title_search_options + [item]        # creating a list of the "title_search_links" dictonary`s keys (Hungarian / Czech /..) from settings_db.json
title_search_options.sort()         #sorts the list ascending   # adding new title link key-value pair: just add it to the settings_db.json / "title_search_links" dictionary

title_search_roll_down_clicked = StringVar()
title_search_roll_down_clicked.set(settings_data['title_search_link_selected'])   # set to the latest saved value (Hungarian / Czech /..)
title_search_roll_down = OptionMenu( window, title_search_roll_down_clicked, *title_search_options )
title_search_roll_down.configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
title_search_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=font_color, activeforeground = window_background_color)

# POSTER SIZE - ROLL DOWN MENU
poster_size_options = []
for item in settings_data['poster_size_options']:        # creating a list of the POSTER SIZE OPTIONS holded in settings_db.json / poster_size_options
    poster_size_options = poster_size_options + [item]

poster_roll_down_clicked = StringVar()
poster_roll_down_clicked.set(settings_data['poster_size'])       # # set to the latest saved value
poster_roll_down = OptionMenu( window, poster_roll_down_clicked, *poster_size_options)
poster_roll_down.config(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
poster_roll_down["menu"].config(foreground=font_color, background=background_color, activebackground=font_color, activeforeground = window_background_color)


## PATH - FIELDS + SEARCHBOXES
mandatory_field_text = ' - - MANDATORY - -'

# TARGET SHEET - FIELD + SEARCHBOX
target_sheet_text = "Target sheet path"
target_sheet_field = Text(window, height = 1, width = 20, foreground=font_color, background=field_background_color)

if settings_data['path_movie_new_record'] == "":        # mandatory field reminder
    target_sheet_field.insert(END, mandatory_field_text)
else:
    target_sheet_field.insert(END,settings_data['path_movie_new_record'])   # set to the latest saved PATH value

target_sheet_field_title = Label(window, text = target_sheet_text, foreground=font_color, background=background_color)
target_sheet_field_title.config(font =(font_style, 12))

filename = None
def browseSheet_1():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                        ("all files", "*.*")))
    target_sheet_field.delete('1.0', END)       # once a button is clicked, removes the previous value
    target_sheet_field.insert(END,filename)     # adding the path and the name of the selected file
target_sheet_button = Button(window, text = ">>", command = browseSheet_1, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)


### BUTTONS
# SAVE SETTINGS, START THE ENGINE - BUTTON
def save_and_start():
    ## SETUP AND SAVE
    
    # POSTER IN NEW TAB - CHECKBOX + ROLL DOWN BUTTON
    settings_data['poster_open_in_new_tab'] = checkbox['poster'][0].get() 
    settings_data['poster_size'] = poster_roll_down_clicked.get()

    # QUIT AFTER RUN CHECKBOX
    settings_data['quit_after_run'] = checkbox['quit'][0].get()

    # LOOK FOR NATIVE TITLE - CHECKBOX + ROLL DOWN BUTTON
    settings_data['title_search'] = checkbox['title'][0].get()                              # from CHECKBOXES for loop: variable = item[0] -> item[0] = checkbox['title'][0]
    settings_data['title_search_link_selected'] = title_search_roll_down_clicked.get()      # Hungarian / Czech..

    # TARGET SHEET PATH FIELD
    settings_data['path_movie_new_record'] = target_sheet_field.get("1.0", "end-1c")

    # SKINS ROLL DOWN BUTTON
    # FYI: the skin is saved, when it is updated -> next time will load the latest used skin, without the need of the Save & Start button/process  

    settings.save_settings(settings_data)

    
    ### START ###
    ## MANDATORY FIELDS CHECK   
    error_popup_window_title = settings_data['skins'][skin_selected]['error_window_title']  # after skin switch the window title will be updated once the prog. restarted
    # TARGET SHEET
    if target_sheet_field.get("1.0", "end-1c") in ['', mandatory_field_text]:
        tkinter.messagebox.showinfo(error_popup_window_title, f"#{target_sheet_text}# needs to be added")   # error pop-up message
        return
    
    engine.start_engine()   # will start data collection / save to excel sheet / if selected: open poster and native title search in new tabs, open movie DB sheet...

    if checkbox['quit'][0].get() == 1:
        sys.exit()
    
button_save_and_start = Button(window, text = "Save & Start", command = save_and_start, font = (font_style, 15), foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)        
# no () in save_and_start() otherwise will execute it automatically before clicking the button
# binding multiple commands to the same button: command = lambda: [save_settings(), engine.start_engine()]


### DISPLAY WIDGETS
def display_widgets():
    # BASE VALUES
    linux_diff_a, linux_diff_b, linux_diff_c = 0, 0, 0
    if os_linux:
        linux_diff_a = 15
        linux_diff_b = 3
        linux_diff_c = 5
    # X
    x = 150
    x_button_gap = 170
    x_gap_for_path_objects = 5
    # Y
    y_base = 200
    y_gap = 30

    
    def y_location(gap_by_number):
        display_y = y_base + y_gap * gap_by_number
        return display_y

    # POSTER CHECKBOX + ROLL DOWN BUTTON
    checkbox['poster'][1].place(x=x, y=y_location(1))
    poster_roll_down.place(x=x+x_button_gap+linux_diff_a, y=y_location(1))

    # LOOK FOR NATIVE TITLE + ROLL DOWN BUTTON
    checkbox['title'][1].place(x=x, y=y_location(2))
    title_search_roll_down.place(x=x+x_button_gap+linux_diff_a, y=y_location(2))

    # QUIT AFTER RUN CHECKBOX
    checkbox['quit'][1].place(x=x, y=y_location(3))

    # TARGET SHEET PATH - TITEL + FIELD + BUTTON
    target_sheet_field_title.place(x=x+x_gap_for_path_objects, y=y_location(4)+10)
    target_sheet_field.place(x=x+x_gap_for_path_objects+3, y=y_location(4)+35+linux_diff_b)
    target_sheet_button.place(x=x+x_gap_for_path_objects+x_button_gap+linux_diff_b, y=y_location(4)+23+linux_diff_c)

    # SKINS ROLL DOWN BUTTON
    skins_roll_down.place(x=212, y=y_location(6)+10)

    # SAVE SETTINGS & START BUTTON
    button_save_and_start.place(x=x+x_gap_for_path_objects+30, y=y_location(8)+10)

display_widgets()

window.mainloop()