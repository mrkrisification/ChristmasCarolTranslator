from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font
from tkinter import ttk
from serial_translator import SerialTranslator
from tkinter import messagebox as msg
import random

language_options = []
serial_translator = SerialTranslator()


def get_input_language():
    input_language = combobox.get()
    return input_language

def get_language_list():
    selected_list = list(listbox.curselection())
    options = serial_translator.get_language_options()
    language_list = []
    for s in selected_list:
        language_list.append(options[s])

    random.shuffle(language_list)
    return language_list


def read_input():
    lyrics = lyrics_input.get(1.0, END)
    input_lang = get_input_language()
    language_list = get_language_list()
    print(language_list)
    serial_translation(lyrics, serial_translator, input_lang, language_list)

def serial_translation(text, translator, input_language, language_list):
    translated_lyrics.insert('1.0', 'Running Translations now. Please wait a few seconds')
    translated_text = translator.serial_translation(text, input_language, language_list)

    translated_lyrics.delete('1.0', END)
    translated_lyrics.insert('1.0', translated_text)

def show_about():
    text = """Christmas Carol Translator uses Google Translate to translate the inital lyrics through a selection of languages for fun results. 
    \n\nDeveloped by Christian Rezek in 2019. \nHave Fun!"""
    msg.showinfo('About', message=text)

def show_help():
    text = """Usage of the Christmas Carol Translator is pretty straightforward.\n
    1) Copy/Paste or Type any kind of lyrics in the left box '
    2) Select the corresponding source language
    3) Select a list of languages to translate to (before being translated back to origin)
    4) Press Button 'Translate Now' on the Bottom
    5) Enjoy results in the Box on the right hand side  
    
    PS: The sequence of languages gets shuffled to get different results all the time.
           """
    msg.showinfo('HELP', text)

root = Tk()
root.title("Christmas Carol Translator")
myfont = Font(family="Times New Roman", size=8)

menu = Menu(root)
root.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=show_about)
helpmenu.add_command(label='Help', command=show_help)

#input section
Label(root, text="Lyrics", font=myfont).grid(row=0, column=0, padx=10)
lyrics_input = ScrolledText(root, height=20, width=60); lyrics_input.grid(row=1, column=0, rowspan=3, sticky = 'W')
Button(root, text="Translate Now ", font=myfont, command=read_input).grid(row=5, column=0,columnspan=2, sticky="EW")

#section to select languages
Label(root, text="Source Language", font=myfont).grid(row=0, column=1, padx=10)

options = serial_translator.get_language_options()
combobox = ttk.Combobox(root,values = options)
combobox.set(options[0])
combobox.grid(row=1, column=1, sticky='NEW')


Label(root, text="Translation Languages", font=myfont).grid(row=2, column=1, padx=10)

listbox = Listbox(root, selectmode='multiple')
for o in options:
    listbox.insert('end',str(o))
listbox.grid(row=3, column=1, sticky='NSEW')


separator = ttk.Separator(root,orient=VERTICAL)
separator.grid(row=1, column=8, rowspan=4, sticky='NS')

#section for output
Label(root, text="Fun Translated Lyrics", font=myfont).grid(row=0, column=9, padx=10)
translated_lyrics = ScrolledText(root, height=20, width=60); translated_lyrics.grid(row=1,rowspan=3, column=9)

Button(root, text="Exit", font=myfont, command=sys.exit).grid(row=5, column=9, sticky="EW")



def main():
    root.mainloop()



if __name__ == '__main__':
    main()