def search_list( listToFind, itemToFind ):

    for i in range(0, len(listToFind) ):
        if listToFind[i] == itemToFind:
            return i
    return -1

def sort_list( listToSort ):
    listToSort.sort()   #there is no return statement because list is passed by
                        #reference and therefore simply doing sort_list( listA )
                        #will sort the list.


listA = [4, 3, 5, 1, 9, 3, 8 ]

print( "The searched element is at index: ",search_list( listA, 77 ))

sort_list(listA)

print("Sorted Array is: ",listA)












