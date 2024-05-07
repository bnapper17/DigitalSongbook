"""
Ben Napper

Digital Song Book

This application allows the user to type in or copy over
new songs and add them to a songlis. The user can 
see a list of available songs and select a song to 
display the lyrics.
"""

# gui and database imports
from tkinter import *
import ttkbootstrap as ttkbs
import sqlite3

# module imports
from frames.home_frame import homeFrame
from frames.song_entry_frame import songEntryFrame
from frames.songlist_frame import songlistFrame

class setList(ttkbs.Window):
    """
    Sets up main tkinter window of the application
    """
    def __init__(self):
        """Initializes main window giving title, style theme and size"""
        super().__init__(themename='darkly') 

        #set attributes of window
        self.title('Set List')
        self.geometry('750x850') 
        self.minsize(750,850)
        self.maxsize(750,850)

        #create Frame instances
        self.home = homeFrame(self) 
        self.songEntry = songEntryFrame(self) 
        self.songlist = songlistFrame(self) 

        #place Home Frame on window
        self.home.pack(fill='both', expand=True) 
    
    #method for clearing screen
    def removeFrames(self):
        """Removes whichever frame is visible in main window"""
        self.home.pack_forget()
        self.songEntry.pack_forget()
        self.songlist.pack_forget()

    #navigation methods     
    def toHome(self):
        """Displays Home Frame in window"""
        self.removeFrames()
        self.home.pack(fill='both', expand=True)
    
    def toNewSong(self):
        """Displays Song Entry Frame in window"""
        self.removeFrames()
        self.songEntry.pack(fill='both', expand=True)
        
    def toSonglist(self):
        """Displays Song List Frame in window"""

        #connect to database
        con = sqlite3.connect('songlist.db')
        cur = con.cursor()
        #check to see if songs table is present
        tableExists = cur.execute("SELECT name FROM sqlite_master WHERE name='songs'")
        #if songs table is not present then create it
        if tableExists.fetchone() == None:
            cur.execute("CREATE TABLE songs(title, lyrics)")
        #if songs table is present do nothing
        else:
            pass

        self.removeFrames()
        self.songlist.pack(fill='both', expand=True)
    
    #Exit application
    def exit(self):
        self.destroy()
        
# Begin main loop
if __name__ == '__main__':
    setList().mainloop()

