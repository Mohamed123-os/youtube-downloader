import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from pytube import *

root = Tk()
root.geometry("500x400")
root.title("Youtube Video Downloader")
root.resizable(0, 0)
# first label
label = Label(root, text="Youtube Video Downloader", font="Arial 20 bold")
label.pack()
# first textbox
link = StringVar()
Label(root, text="Enter link Here:", font="arial 15 bold").place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)
# second label
Label(root, text="Choose Quality:", font="arial 15 bold").place(x=160, y=150)
# combo box
combo = Combobox(root)
combo['values'] = ('144p', '240p', '360p', '480p', '720p')
combo.current(0)
combo.place(x=170, y=190)


def downloader():
    name = filedialog.askdirectory()
    url = YouTube(str(link.get()))
    video = url.streams.get_by_resolution(combo.get()).download(f"{str(name)}")
    Label(root, text='DOWNLOADED', font='arial 15').place(x=160, y=310)


# downloading button
Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=downloader).place(x=167,
                                                                                                            y=270)
root.mainloop()
