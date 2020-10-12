
file = 'Textfile.py'

def write_to_file(studentTuple):

    new_file = open(file,'a')
    new_file.write(studentTuple + "\n")
    new_file.close()

def get_student_info(studentName):
    test_scores = []
    print("Enter scores for: " +studentName)
    while True:
        student_score = int(input("Enter the scores "))
        test_scores.append(student_score)
        stop = input("Press s to stop")
        if(stop != "s"):
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
    main()


('Ben', (80,))
('Ben', (80, 70))
('Eric', (80,))
('Eric', (80, 70))
('David', (60,))
('David', (60, 40))
('Frank', (60,))
('Frank', (60, 42))
