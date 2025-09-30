import csv
def read_dictionary(filename, key_column_index):
    s_dictionary={}
    with open(filename,'rt') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=",")
        next(csvreader)
        for row in csvreader:
            key_value=row[key_column_index]
            s_dictionary[key_value]=row
    return s_dictionary    


def main():
    key_index=0
    name_index=1
    students=read_dictionary('students.csv',key_index)
    inumber=input("Enter an i-number: ")
    inumber=inumber.replace("-","")
    if not inumber.isdigit():
        print("invalid i-number")
    elif len(inumber)!=9:
       print("An i-number must have 9 digits")    
    else:
       if inumber in  students:   

        student=students[inumber]
        name=student[name_index]
        print(f"student name is {name}")
       else:
        print("No such student!")
        


if __name__ == "__main__":
    main()