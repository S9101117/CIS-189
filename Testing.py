import unittest

from HangManC import Hangman

#Unit Testing is done on the function of hangman class that is check letters that checks the letter passed by the user 



class TestButtonss(unittest.TestCase):
      
    def test_ItwillrejectifwrongButtonIspressed(self):
        '''Function to Test if the checkLetters is working correctly. It should reject
        if wrong button is pressed'''
        hang = Hangman()
        word = 'invalid'
        assert hang.checkLetters('h',word) == False
        assert hang.checkLetters('z',word) == False
        assert hang.checkLetters('a',word) == True
        

    def test_ItwillAcceptifCorrectButtonIspressed(self):
        '''Function to Test if the checkLetters is working correctly. It should reject
        if wrong button is pressed'''
        hang = Hangman()
        words = 'correctly'
        assert hang.checkLetters('o',words) == True
        assert hang.checkLetters('c',words) == True
        assert hang.checkLetters('z',words) == False
        

if __name__ == '__main__':
    unittest.main()
