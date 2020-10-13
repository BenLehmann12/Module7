
def sort_array(lst):
    lst.sort()
    return lst


def search_array(lst, value):  #Value is the item in the list, asks the user to put in
    try:
        return lst.index(value)   #return the index of the user value if found
    except ValueError:
        return -1    #If not, return -1


if __name__=="__main__":
    print(sort_array([2,10,1,6,8,3]))
    print(search_array([2,10,1,6,8,3],1))








