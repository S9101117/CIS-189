def get_input():
    user_value = input("Please enter a value: ")
    return user_value

def make_list():

    collection = []

    for i in range(0,3):
        tempVar = get_input()
        if tempVar.isdigit() == False:
            raise ValueError("Input is non-integer")
        collection.append( tempVar )

    return collection



print(make_list())



