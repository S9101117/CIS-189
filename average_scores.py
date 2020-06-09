# def average():
#   pass
"""code for average score"""

last_name = input( "enter your last name:" )
first_name = input( 'Enter your first name:' )
age = int(input('age:'))
a = int( input( 'score1:' ) )
b = int( input( 'score2:' ) )
c = int( input( 'score3:' ) )


def average(a, b, c):
    return (int( a + b + c ) / 3)


average_scores: float = average(a,b,c)

# Get input for scores
# declare variables, use score1, score2, score3 in calculation

if __name__ == '__main__':
    print( average( a, b, c ) )


"""enter your last name:Shoaib
Enter your first name:Saad
age:22
score1:90
score2:95
score3:85


Ran 1 test in 0.004s

OK
Process finished with exit code 0
"""
"""enter your last name:Shoaib
Enter your first name:Saad 
age:22
score1:90
score2:95
score3:85
90.0
"""
