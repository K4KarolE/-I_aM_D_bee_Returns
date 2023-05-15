import tkinter.messagebox
from functions import settings
settings_data = settings.open_settings()

skin_selected = settings_data['skin_selected']  
error_popup_window_title = settings_data['skins'][skin_selected]['error_window_title']

popup_message_dic = {
    'wrong_link': 'Wrong link in clipboard\n\nCopy the IMDb link and click OK',
    'excel_is_open':'Close your sheet and click OK',
    'excel_is_saved':'Data is added to your sheet.',
    'excel_cant_open':'Was not able to launch the excel sheet.',
    'bye_bye':'You just blew it honey!'
    }

def error_pop_up(popup_message_dic_key):
    tkinter.messagebox.showinfo(error_popup_window_title, f"{popup_message_dic[popup_message_dic_key]}") # tkinter.messagebox.showinfo ( window title, message )
