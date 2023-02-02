import view
# students
{1:{'First Name': 'Иван', 'Last Name': 'Иванов', 'Birthday': '2000-01-01'}}
# class
{'1a': [],'1b':[]}
student_id_counter = 1 
students = {}
classes = {}
#def GetStudentClass():
#    return view.GetNewStudentInfo('student`s class')

def AddNewStudent():
    new_student = dict()
    new_student['Id'] = GetNewId()
    new_student['First Name'] = view.GetNewStudentInfo('student`s first name')
    new_student['Last Name'] = view.GetNewStudentInfo('student`s last Name')
    new_student['Birthday'] = view.GetNewStudentInfo('student`s birthday' )
   # new_student['Class Name'] = view.GetNewStudentInfo('student`s class ' )
    AddStudentsInClasses(new_student['Id'])
    return new_student
 
    
def GetNewId():
    global student_id_counter
    student_id_counter +=1
    return student_id_counter   
 
    
def SaveStudents(student):
    with open('c:/Users/semiya/Desktop/обучение наташа/Питон/seminar8/students.csv', 'a') as file:
        file.write(f"{student['Id']};{student['First Name']};{student['Last Name']};{student['Birthday']}\n")

        
def AddStudentsInClasses(student_id):
    global classes
    student_class = view.GetNewStudentInfo('student`s class')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]
        
      
def GetLastStudentId():
    global student_id_counter
    with open('c:/Users/semiya/Desktop/обучение наташа/Питон/seminar8/last_student_id.txt', 'r') as file:
        student_id_counter = int(file.read())
        
        
def SaveLastStudentId():
    global student_id_counter
    with open('c:/Users/semiya/Desktop/обучение наташа/Питон/seminar8/last_student_id.txt', 'w') as file:
        file.write(str(student_id_counter)) 
        
               
def SaveClasses():
    with open('c:/Users/semiya/Desktop/обучение наташа/Питон/seminar8/classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')


def GetClasses():
    with open('c:/Users/semiya/Desktop/обучение наташа/Питон/seminar8/classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
            print(classes)
             
def get_classes():
    with open('c:/Users/semiya/Desktop/обучение наташа/Питон/dz8/classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
            print(classes)