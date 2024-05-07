#gui imports
from tkinter import *
import ttkbootstrap as ttkbs
from PIL import Image, ImageTk 


class homeFrame(Frame):
    """Sets up home screen of application"""
    def __init__(self, parent):
        """Initializes Home Frame """
        super().__init__(parent)

        #setup image
        self.img = Image.open('./resources/binder_icon.png').resize((350,350))
        self.tkImage = ImageTk.PhotoImage(self.img)
        
            
        #Create widgets
        self.title = ttkbs.Label(self, text='Digital Song Book', bootstyle='primary', font=('Helvetica', 24))
        self.homeIcon = ttkbs.Label(self, image=self.tkImage)
        self.homeIcon.image=self.tkImage
        self.newsong = ttkbs.Button(self, text='New Song', bootstyle='success, outline', cursor='hand2', command=parent.toNewSong)
        self.songlist = ttkbs.Button(self, text='Song List', bootstyle='success, outline', cursor='hand2', command=parent.toSonglist)
        self.exitButton = ttkbs.Button(self, text='Close', bootstyle='danger, outline', cursor='hand2', command=parent.exit)
        

        #place widgets
        self.title.place(relx=0.5, rely=0.1, anchor='center')
        self.homeIcon.place(relx=0.5, rely=0.4, anchor='center')
        self.newsong.place(relx=0.25, rely=0.8, relheight=0.075, relwidth=0.2)
        self.songlist.place(relx=0.55, rely=0.8, relheight=0.075, relwidth=0.2)
        self.exitButton.pack(side='bottom', pady=30)

        

      