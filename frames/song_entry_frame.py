#gui and database imports
from tkinter import *
import ttkbootstrap as ttkbs
from tkinter.simpledialog import askstring
from tkinter.messagebox import showwarning
import sqlite3
from PIL import Image, ImageTk


class songEntryFrame(Frame):
    """Sets up screen for entering in new songs"""
    def __init__(self, parent):
        """Initializes Song Entry Frame"""
        super().__init__(parent)

        #setup image
        self.img = Image.open('./resources/songbook.png').resize((125,125))
        self.tkImage = ImageTk.PhotoImage(self.img)

        #create widgets
        self.header = ttkbs.Label(self, text='Enter new song!', bootstyle='info', font=('Helvetica', 12))
        self.icon = ttkbs.Button(self, text='Song List', image=self.tkImage, compound='top', bootstyle='link, info', cursor='hand2', command=parent.toSonglist)
        self.icon.image= self.tkImage
        self.songEntry = ttkbs.Text(self, font=('Helvetica', 14))
        self.addButton = ttkbs.Button(self, text='Add Song', bootstyle='success, outline', cursor='hand2', command=self.addSong)
        self.homeButton = ttkbs.Button(self, text='Home', bootstyle='info, outlined', cursor='hand2', command=parent.toHome)

        #widget placement
        self.header.place(relx=0.1, y=20, anchor=CENTER)
        self.icon.place(relx=0.9, rely=0.2, anchor=CENTER)
        self.songEntry.place(x=0, y=40, relheight=1.0, relwidth=0.75)
        self.addButton.place(relx=0.9, rely=0.4, relheight=0.05, relwidth=0.15, anchor=CENTER)
        self.homeButton.place(relx=0.9, rely=0.6, relheight=0.05, relwidth=0.15, anchor=CENTER)
   
    # add song to database method
    def addSong(self):
        """Add new song to database"""

        #connect to database
        con = sqlite3.connect('songlist.db')
        cur = con.cursor()

        #check if song table exists, create if not
        tableExists = cur.execute("SELECT name FROM sqlite_master WHERE name='songs'")
        if tableExists.fetchone() == None:
            cur.execute("CREATE TABLE songs(title, lyrics)")
        else:
            pass
        
        #get lyrics from text widget
        lyrics = self.songEntry.get("1.0", "end-1c")

        #check if lyrics have been entered
        if lyrics:
            
            #if lyrics entered ask for title
            titleEntry = askstring('Title', 'What is the song title?')
           
            #Check if title has been entered
            if titleEntry:
            
            #if title is entered add song to database
                cur.execute("INSERT INTO songs VALUES(:title, :lyrics)",{
                'title': titleEntry,
                'lyrics': lyrics
            })
                con.commit()
                self.songEntry.delete('1.0', 'end')            
                #if title not entered show warning
            else:
                showwarning('Invalid Action', 'Title must be entered in pop up box!')
        else: 
           
            #if lyrics not entered show warning
            showwarning('Invalid Action', 'Please enter song lyrics in text box!')
        
    

    