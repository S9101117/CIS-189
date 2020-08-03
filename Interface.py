from tkinter import *
from tkinter import messagebox


class Interface:
    
    def __init__(self): #Constructor Work
        
        '''Constructor to initialzie these variables as soon as game is started'''
        
        self.buttons = [[0,300],[120,300],[240,300],[360,300],[480,300],[600,300],[720,300],
                      [0,400],[120,400],[240,400],[360,400],[480,400],[600,400],[720,400],
                      [0,500],[120,500],[240,500],[360,500],[480,500],[600,500],[720,500],
                      [120,600],[240,600],[360,600],[480,600],[600,600]]
       
        
        self.window = Tk()
        self.window.geometry('1024x1024')
        self.window.title("Hangman Game")
        self.window.config(bg = '#808000')
      
        
    def getButton(self,ind):
        return self.buttons[ind]
        
    def gethangman(self,ind):
        return self.hangman[ind]
            
