def get_input():
    user_input = input("Enter a number")
    return user_input


def make_list():
    lst = []
    length = 3
    for i in range(length):
        try:
            data = int(get_input())
        except ValueError:
            print("Enter Numbers")
        else:
            if(data < 1 or data > 50):
                print("Numbers 1 through 50 please")
            else:
                lst.insert(len(lst),data)
    return lst

if __name__=="__main__":
    print(make_list())