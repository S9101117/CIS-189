def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again " ):
    if test_score < 0 or test_score >= 100:
        print(invalid_message)
        while test_score <= 0 or test_score >= 100:
            test_score = int(input("Please enter a number between 0-100 "))
            if test_score <= 0 or test_score >= 100 or test_score != int:
                print (invalid_message)
    print(test_name, test_score)


if __name__ == '__main__':

     score_input("Saad", test_score=90, invalid_message="Invalid test score, try again ")
