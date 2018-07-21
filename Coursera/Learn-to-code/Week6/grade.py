def read_grades(gradefile):
    """(file open for reading) -> list of float

    Read and return list of grades in gradefile

    Precondition: gradefile starts with a header
    that contains no blank lines, then has a blank line,
    and then lines contain a student number and a grade.
    """
    #skip over header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    #read the grades, accumlating them into a list.
    grades = []
    
    line = gradefile.readline()
    while line != '':
        #We have a string containing info for single student.
        #Find last space and take everything after space.
        grade = line[line.rfind(' ') + 1:]
        grades.append(float(grade))
        line = gradefile.readline()
        
    return grades
