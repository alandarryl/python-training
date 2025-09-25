

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def showGrade(self):
            print(f" {name} grade is : {self.grade}")
    
    def addGrade(self):
        try:
            self.grade = int(input("Enter the grade : "))
        except ValueError:
            print("Entry Invalid, pleaser enter a number")

working = True

while working:
    print("Welcome in our student managemet app :")
    print('''
        what do you want to do : 
        1 - see the grade of all student
        2 - see the grade of a specific student
        3 - enter the grade of a new studen
        4 - quit the program
        ''')
    entry = int(input(" > "))
    if entry == 4:
        working = False
    elif entry == 3:
        print("pleease enter the name and grade of the student")
        name = input("Name : ")
        grade = int(input("Grade : "))
        new_student = Student(name, grade)
    elif entry == 2:
        named = input("Enter the name of the sytudent : ")
        if Student[named] in Student:
            print(f" the student {Student[named]} have {Student.showGrade()}")


