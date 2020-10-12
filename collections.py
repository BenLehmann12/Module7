
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
            print("Enter a number")
        else:
            lst.insert(len(lst), data)
    return lst

print(make_list())



