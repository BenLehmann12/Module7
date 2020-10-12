

def sort_list(a_list):
    a_list.sort()
    return a_list

def search_list(a_list,number):
    try:
        index = a_list.index(number)
        print("Index: " + str(index))
    except ValueError:
        return -1
    else:
        return index

if __name__=="__main__":
    print(sort_list([9,20,1,16,2]))
    print(search_list(a_list=[9,20,1,16,2],number=2))


