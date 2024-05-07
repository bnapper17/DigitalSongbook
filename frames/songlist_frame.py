#gui and database imports
from tkinter import *
import ttkbootstrap as ttkbs
import sqlite3

class songlistFrame(Frame):
    """Sets up Songlist Screen """
    
    #setup songlist list
    sortedSonglist = []

    #connect to database
    con = sqlite3.connect('songlist.db')
    cur = con.cursor()

    #Checks if songs table exists
    tableExists = cur.execute("SELECT name FROM sqlite_master WHERE name='songs'")
    #if songs table does not exists, create it
    if tableExists.fetchone() == None:
        cur.execute("CREATE TABLE songs(title, lyrics)")
    #if songs table exists retrieve song titles
    else:
        titles = cur.execute("SELECT title FROM songs")
        songlist = titles.fetchall()
        sortedSonglist = sorted(songlist)
        

    def __init__(self, parent):
        """Initializes Songlist Frame"""
        super().__init__(parent,)

        # grid setup
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=8)
        self.rowconfigure(1, weight=1)

        #create main layot widgets
        self.songTitleFrame = ttkbs.Frame(self)
        self.buttonFrame = ttkbs.Frame(self)
        self.songLyrics = ttkbs.Text(self, font=('Helvetica', 14), pady=10)
        self.songLyrics.insert(INSERT, 'Click song title to display lyrics...')
        self.songLyrics.config(state='disabled')
        
        #place main layout widgets
        self.songTitleFrame.grid(row=0, column=0, sticky='nsw')
        self.songLyrics.grid(row=0, column=1, stick='nsew')      
        self.buttonFrame.grid(row=1, column=0, columnspan=2)
        
        #create child widgets
        self.songlistHeader = ttkbs.Label(self.songTitleFrame, text='Song Titles', bootstyle='info', font=('Helvetica 14 underline'))
        self.songlistHeader.pack(pady=10, padx=10, side='top')
        for title in self.sortedSonglist:
            self.songLink = ttkbs.Button(self.songTitleFrame, text=title[0], bootstyle='success, link', cursor='hand2', command=lambda value=title[0]: self.displaySong(value))
            self.songLink.pack(pady=5, padx=5, anchor='w')
        self.refresh = ttkbs.Button(self.buttonFrame, text='Refresh', bootstyle='info, outlined', command=self.refreshPage)
        self.homeButton = ttkbs.Button(self.buttonFrame, text='Home', bootstyle='info, outlined', command=parent.toHome)
        self.newSongButton = ttkbs.Button(self.buttonFrame, text='New Song', bootstyle='info, outlined', command=parent.toNewSong)
        self.exitButton = ttkbs.Button(self.buttonFrame, text='Close', bootstyle='danger, outline', cursor='hand2', command=parent.exit)
        
        #place child widgets
        self.refresh.grid(row=0, column=0, padx=5)
        self.homeButton.grid(row=0, column=1, padx=5)
        self.newSongButton.grid(row=0, column=2, padx=5)
        self.exitButton.grid(row=0, column=3, padx=5)

    def refreshPage(self):
        """Update songlist from database"""

        #connect to database
        con = sqlite3.connect('songlist.db')
        cur = con.cursor()

        #retrieve updated songlist
        updatedTitles = cur.execute("SELECT title FROM songs")
        updatedSonglist = updatedTitles.fetchall()
        sortedSonglist = sorted(updatedSonglist)
       
        #remove current list
        self.songTitleFrame.destroy()

        #create new list        
        self.songTitleFrame = ttkbs.Frame(self)
        self.songTitleFrame.grid(row=0, column=0, sticky='nsw')
        self.songlistHeader = ttkbs.Label(self.songTitleFrame, text='Song Titles', bootstyle='info', font=('Helvetica 14 underline'))
        self.songlistHeader.pack(pady=10, padx=10, side='top')
        for title in sortedSonglist:
            self.songLink = ttkbs.Button(self.songTitleFrame, text=title[0], bootstyle='success, link', cursor='hand2', command=lambda value=title[0]: self.displaySong(value))
            self.songLink.pack( pady=5, padx=5, anchor='w')
        

    def displaySong(self, value):
        """Displays song lyrics in text area"""

        #connect to database
        con = sqlite3.connect('songlist.db')
        cur = con.cursor()

        #retrieve lyrics
        lyrics = cur.execute(f'SELECT lyrics FROM songs WHERE title="{value}"')
        songLyrics = lyrics.fetchone()

        #Insert lyrics in text area, remove any lyrics that may already be there
        self.songLyrics.config(state='normal')
        self.songLyrics.delete('1.0', 'end')
        self.songLyrics.insert(INSERT, songLyrics[0])
        self.songLyrics.config(state='disabled')
        
        
