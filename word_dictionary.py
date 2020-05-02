import json
from tkinter import *
import tkinter.scrolledtext
from difflib import get_close_matches

word_list = json.load(open('dictionary.json'))


def Meaning(word):
    word = word.lower()
    if word in word_list.keys():
        print('Searched meaning of word : ', word)
        return word_list[word]
    elif word.title() in word_list.keys():
        print('Searched meaning of word : ', word.title())
        return word_list[word.title()]
    elif word.upper() in word_list.keys():
        print('Searched meaning of word : ', word.upper())
        return word_list[word.upper()]
    elif word.capitalize() in word_list.keys():
        print('Searched meaning of word : ', word.capitalize())
        return word_list[word.capitalize()]
    elif get_close_matches(word, word_list.keys()):
        print('Searched meaning of word : ', get_close_matches(word, word_list.keys())[0])
        return word_list[get_close_matches(word, word_list.keys())[0]]
    else:
        return 'No such word exists'


def action():
    mean = Meaning(the_word.get())
    word = the_word.get().lower()
    try:
        s = get_close_matches(word, word_list.keys())[0]
        scroll.delete('1.0', 'end')
        scroll.insert(END, 'Meaning of ' + s + ' :' + '\n')
        scroll.insert(END, '---------------------------' + '\n')
        list_mean = list(mean)
        n = 1
        for i in range(len(list_mean)):
            if list_mean[i] == '1':
                n += 1
                list_mean[i - 1] = '\n'
            if list_mean[i] == str(n):
                n += 1
                list_mean[i - 1] = '\n'
            if i != len(list_mean) - 3:
                if list_mean[i:i + 3] == ['S', 'y', 'n']:
                    list_mean[i - 1] = '\n\n'
        new_word = ''.join(list_mean)
        scroll.insert(END, new_word)
    except:
        s = 'No such word exists...'
        scroll.delete('1.0', 'end')
        scroll.insert(END, s)


window = Tk()
window.title("Dictionary")

frame = Frame(window)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
scroll_H = Scrollbar(frame, orient=HORIZONTAL)
scroll_H.pack(side=BOTTOM, fill=X)

lb1 = Label(window, text="Enter Word", width=5, font=("Times", 16), fg="Black", padx="50")
lb1.place(x=55, y=430)
the_word = StringVar()
tf = Entry(window, width=30, fg='black', bd=3, font=16, textvariable=the_word)
tf.place(x=250, y=430)
scroll = tkinter.scrolledtext.ScrolledText(window, bg='white')
scroll.place(x=10, y=10)

btn = Button(window, text="Show", fg='white', bg="black", font=140, padx="50", command=action)
btn.place(x=50, y=490)
window.geometry("685x550")
window.configure(bg="grey")
window.mainloop()