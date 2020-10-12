
file = 'Textfile.py'

def write_to_file(student):

    new_file = open(file,'a')   #Append
    new_file.write(student + "\n")  #New Line
    new_file.close()

def get_student_info(studentName):
    test_scores = []
    print("Enter scores for: " +studentName)
    while True:
        student_score = int(input("Enter the scores "))
        test_scores.append(student_score)
        stop = input("Press s to stop")
        if(stop == "s"):   #If you press s, it will go to the next person
            break
        write_to_file(str((studentName, tuple(test_scores))))


def read_from_file():
    read = open(file)
    for text in read.readlines():
        print(text)
    read.close()

def main():
    get_student_info('Ben')
    get_student_info('Eric')
    get_student_info('David')
    get_student_info('Frank')
    read_from_file()

if __name__ == "__main__":
    main()  #Output


('Ben', (80,))
('Ben', (80, 70))
('Eric', (90,))
('Eric', (90, 20))
('David', (67,))
('David', (67, 51))
('Frank', (56,))
('Frank', (56, 45))
