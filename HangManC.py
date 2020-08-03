import random
import array as arr
from collections import defaultdict

#Array and Dictionary is used in this file

class Hangman:
    
    def __init__(self): #Constructor Work
        
        '''Constructor to initialzie these variables as soon as game is started'''
        self.wordslist = self.readfile()
        
        
        self.letters = arr.array("u",['a','b','c','d','e','f','g','h','i','j','k','l',
                        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']) #Array is used in maingame.py to load images with these names
        
        self.images = ['man1','man2','man3','man4','man5','man6','man7'] #in folder
        self.score = 0
        self.count = 0
        self.win_count = 0
        
    def chooseWord (self):
        '''Chooseword to randomly choose word from the dictionary'''
        
        word, capital = random.choice(list(self.wordslist.items()))
       
        return word
    
    def readfile(self):
        '''Filereadiong function used to read the file for words'''
        
        
        file = open('words.txt','r')
        
        newDict = {} #Dictionary to storew words and their counts to make sure only unique words get into this and randonly selected word is selected
        for line in file:
            listedline = line.strip().split('\n') 
        
            if listedline[0] in newDict:
                newDict[listedline[0]] +=1 
            else:
                newDict[listedline[0]] =0
        
        return newDict
    
    def checkLetters(self,letter,selected):
        if letter not in selected:
            return False
        else:
            return True
    
    
    def __del__(self): #Destructor work to clear the lists
        self.wordslist.clear()
