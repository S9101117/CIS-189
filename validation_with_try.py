def average( score1, score2, score3 ):
    NUMBER_TESTS = 3
    try:
        if score1 < 0 or score2 < 0 or score3 < 0:
            raise ValueError
        else:
            result = (score1 + score2 + score3) / NUMBER_TESTS
            print("all positive")
            return result

    except ValueError as error:
        return str(error)



def main():
    print(average(-90,80,30))

if __name__=="__main__":
    main()



