from HangManC import Hangman
from Interface import Interface
import random # for randomizing 
from tkinter import * #For Making interfaces
from tkinter import messagebox #Fpr using in Alert boxes



#For Infinite Running
running = True

#Hanman Placement
initialhangmanX = 350
initialhangmanY = -30

#Position of Dash Variables
Xdash = 300 #Placemnt ofdashes on scren in xaxis
Ydash = 200
DashGap = 50

#Points Position  
pointsX = 15 
pointsY = 15

#Exit button Position
eximgX = 870
eximgY = 10

# Case Switch
def UserClick(argument): 
	switcher = { 
		True: 1, 
		False: 0, 
		 
	} 
	return switcher.get(argument, False) 


#Exiting clicks
def Finish():
    
    '''It is called when the user presses or clicks exit button'''
    
    global running
    answer = messagebox.askyesno('Exiting','You want to exit the game?')
    gett = UserClick(answer) #Case Switch
    if gett == 1:
        running = False
        interface.window.destroy()
        
   
    

    

#Button Checking
def checkbuttons(letter,button,selected):
    
    '''It is called when the user presses or clicks any of the 26 letter buttons'''
    
    
    
    global running
    button.destroy()
    
    
    if not(hang.checkLetters(letter,selected)):
        
        #Here the hangman pictures a re extended if the guess is wrong
        pics[hang.count].destroy()
        pics[hang.count+1].place(x=initialhangmanX,y=initialhangmanY-5)
        hang.count += 1

        if hang.count == 6:
            answer = messagebox.askyesno('Finished','YOU LOST! Word WAS : '+selected+'\n Want to play again?')
            gett = UserClick(answer) # Case Switch
            
            
            if gett == 1:
                running = True
                hang.score = 0
                interface.window.destroy()
            else:
                running = False
                interface.window.destroy()
        return False
        
        
    else:
        
        #Increasing score and placing an increment on screen
        
        hang.score += 1
        points=hang.score
        sp2 = 'Points: '+str(points)
        sp1 = Label(interface.window,text = sp2,bg = "#808000",font = ("calibri",25))
        sp1.place(x = pointsX,y = pointsY) 
        
        
        for i in range(0,len(selected)):
            
            #If the guess is right then the dash is replaced with the text user enters or clicks
            if selected[i] == letter:
                hang.win_count += 1
                dashes[i].config(text=letter.upper())

                
        # Wining condition
        if hang.win_count == len(selected):
            hang.score += 1
            answer = messagebox.askyesno('Finished','YOU WON!\n Want to play again?')
            
            gett = UserClick(answer) #Case Switch
            
            #Case Switch Condition
            if gett == 1:
                running = True
                interface.window.destroy()   
            else:
                running = False
                interface.window.destroy()
                hang.count += 1
        return True
        
        
     



while running:
    
    interface = Interface() #Interface class object
    hang = Hangman() #Hangman Object
    selected = hang.chooseWord() # Selected word randomly from words


   
  
   #Exit Button On click the finish function is called
    eximg = Button(interface.window,command = Finish,bg="#808000",activebackground = "#808000",text = "EXIT")
    eximg.place(x=eximgX,y=eximgY)
    
    
    points=hang.score
    sp2 = 'Points: '+str(points)
    sp1 = Label(interface.window,text = sp2,bg = "#808000",font = ("calibri",25))
    sp1.place(x = pointsX,y = pointsY) 
    
    
    
    #Dashes are placed on screen according to number of letters
    xd = Xdash
    dashes=[]
    for i in range(0,len(selected)):

        dashes.append(Label(interface.window,text="_",bg="#808000",font=("calibri",50)))  
        dashes[i].place(x=xd,y=Ydash)
        xd += DashGap

       
       
    # 26 photos of characters are loaded
    Photos = []
    
    for i in range(0,26):
        Photos.append(PhotoImage(file="LetterPics/"+hang.letters[i]+".png"))

   
    
    # Alphabet Buttons with images loaded from letter pics above
    b1=Button(interface.window,command=lambda:checkbuttons('a',b1,selected),bg="#E7FFFF",activebackground="#808000",image=Photos[0])
    b1.place(x=interface.buttons[0][0],y=interface.buttons[0][1])
    
    b2=Button(interface.window,command=lambda:checkbuttons('b',b2,selected),bg="#808000",activebackground="#E7FFFF",image=Photos[1])
    b2.place(x=interface.buttons[1][0],y=interface.buttons[1][1])
    
    b3=Button(interface.window,command=lambda:checkbuttons('c',b3,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[2])
    b3.place(x=interface.buttons[2][0],y=interface.buttons[2][1])
    
    b4=Button(interface.window,command=lambda:checkbuttons('d',b4,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[3])
    b4.place(x=interface.buttons[3][0],y=interface.buttons[3][1])
    
    b5=Button(interface.window,command=lambda:checkbuttons('e',b5,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[4])
    b5.place(x=interface.buttons[4][0],y=interface.buttons[4][1])
    
    b6=Button(interface.window,command=lambda:checkbuttons('f',b6,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[5])
    b6.place(x=interface.buttons[5][0],y=interface.buttons[5][1])
    
    b7=Button(interface.window,command=lambda:checkbuttons('g',b7,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[6])
    b7.place(x=interface.buttons[6][0],y=interface.buttons[6][1])
    
    b8=Button(interface.window,command=lambda:checkbuttons('h',b8,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[7])
    b8.place(x=interface.buttons[7][0],y=interface.buttons[7][1])
    
    b9=Button(interface.window,command=lambda:checkbuttons('i',b9,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[8])
    b9.place(x=interface.buttons[8][0],y=interface.buttons[8][1])
    
    b10=Button(interface.window,command=lambda:checkbuttons('j',b10,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[9])
    b10.place(x=interface.buttons[9][0],y=interface.buttons[9][1])
    
    b11=Button(interface.window,command=lambda:checkbuttons('k',b11,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[10])
    b11.place(x=interface.buttons[10][0],y=interface.buttons[10][1])
    
    b12=Button(interface.window,command=lambda:checkbuttons('l',b12,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[11])
    b12.place(x=interface.buttons[11][0],y=interface.buttons[11][1])
    
    b13=Button(interface.window,command=lambda:checkbuttons('m',b13,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[12])
    b13.place(x=interface.buttons[12][0],y=interface.buttons[12][1])  
    
    b14=Button(interface.window,command=lambda:checkbuttons('n',b14,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[13])
    b14.place(x=interface.buttons[13][0],y=interface.buttons[13][1])
    
    b15=Button(interface.window,command=lambda:checkbuttons('o',b15,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[14])
    b15.place(x=interface.buttons[14][0],y=interface.buttons[14][1])
    
    b16=Button(interface.window,command=lambda:checkbuttons('p',b16,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[15])
    b16.place(x=interface.buttons[15][0],y=interface.buttons[15][1])
    
    b17=Button(interface.window,command=lambda:checkbuttons('q',b17,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[16])
    b17.place(x=interface.buttons[16][0],y=interface.buttons[16][1])
    
    b18=Button(interface.window,command=lambda:checkbuttons('r',b18,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[17])
    b18.place(x=interface.buttons[17][0],y=interface.buttons[17][1])
    
    b19=Button(interface.window,command=lambda:checkbuttons('s',b19,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[18])
    b19.place(x=interface.buttons[18][0],y=interface.buttons[18][1])
    
    b20=Button(interface.window,command=lambda:checkbuttons('t',b20,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[19])
    b20.place(x=interface.buttons[19][0],y=interface.buttons[19][1])
    
    b21=Button(interface.window,command=lambda:checkbuttons('u',b21,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[20])
    b21.place(x=interface.buttons[20][0],y=interface.buttons[20][1])
    
    b22=Button(interface.window,command=lambda:checkbuttons('v',b22,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[21])
    b22.place(x=interface.buttons[21][0],y=interface.buttons[21][1])
    
    b23=Button(interface.window,command=lambda:checkbuttons('w',b23,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[22])
    b23.place(x=interface.buttons[22][0],y=interface.buttons[22][1])
    
    b24=Button(interface.window,command=lambda:checkbuttons('x',b24,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[23])
    b24.place(x=interface.buttons[23][0],y=interface.buttons[23][1])
    
    b25=Button(interface.window,command=lambda:checkbuttons('y',b25,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[24])
    b25.place(x=interface.buttons[24][0],y=interface.buttons[24][1])
    
    b26=Button(interface.window,command=lambda:checkbuttons('z',b26,selected),bg="#E7FFFF",activebackground="#E7FFFF",image=Photos[25])
    b26.place(x=interface.buttons[25][0],y=interface.buttons[25][1])
    
    
    #hangman pictures loading
    man = []
    for i in range(0,7):
        man.append(PhotoImage(file="hangmanPics/"+hang.images[i]+".png"))

    #7 pictures creation and placing them on screen
    pics=[]   
    for i in range(0,7):
        pics.append(Label(interface.window,bg="#808000",image=man[i]))
    
    
    # placement of first hangman image
    pics[0].place(x = initialhangmanX,y = initialhangmanY)

    #main interface loops
    interface.window.mainloop()
    
