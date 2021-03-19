import errno

class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
	# put your code here
    pass

class Wrongamountofcolumns(BadLine):
    pass

class FileEmpty(StudentsDataException):
    pass

def check_the_file(file):
    #with file.read(1) as ini:
    #    if not ini:
    #        raise FileEmpty

    lines = file.readlines()
    if not lines.__len__():
        raise FileEmpty
    for line in lines:
        columns = line.split('\t')
        size = len(columns)
        if not size == 3:
            raise Wrongamountofcolumns
        name = columns[0] + " " + columns[1]
        grade = float(columns[2])
        if name in grade_dict.keys():
            grade_dict[name] += grade
        else:
            grade_dict[name] = grade

global lines
global grade_dict

grade_dict = {}
lines = []
if __name__ == '__main__':

    filename = input("Whats the name of the file?\n")
    try:
        file = open(filename + '.txt', 'rt')

        try:
            check_the_file(file)
        except FileEmpty:
            print('its empty!')
            exit()
        except BadLine:
            print("This file has bad lines...")
            exit()

        file.close()

    except Exception as exc:
        if exc.errno == errno.ENOENT:
            print("The file doesn't exist.")
        elif exc.errno == errno.EMFILE:
            print("You've opened too many files.")
        else:
            print("The error number is:", exc.errno)

    sorted_grades = sorted(grade_dict.items())
    for i in sorted_grades:
        print(i[0] + '\t' + str(i[1]))