#  Clayton Clark 92141310. ICS 31 Lab sec 11.

### c.1
print('------------------------- c.1 ----------------------')

from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

def read_menu_with_count(name: str)-> list:
    ''' Takes a string naming a file, reads the file, and returns a list of Dish Structures
        created from the data '''

    infile = open(name, 'r')
    results = []
    counter = 0
    for i in infile:
        new_infile = i.split('\t')
        if counter >=1:
            results.append(Dish(new_infile[0],float(new_infile[1][1:]), int(new_infile[2])))
        counter += 1
    infile.close()
    return results

print(read_menu_with_count('menu1.txt'))
print(read_menu_with_count('menu2.txt'))

### c.2
print('------------------------- c.2 ----------------------')

def read_menu(name: str)-> list:
    ''' Takes a string as an argument, reads the file, and returns a list of Dishes '''
    infile = open(name, 'r')
    results = []
    for i in infile:
        new_infile = i.split('\t')
        results.append(Dish(new_infile[0], float(new_infile[1][1:]), int(new_infile[2])))
    infile.close()
    return results

print(read_menu('menu3.txt'))

### c.3
print('------------------------- c.3 ----------------------')

def write_menu(d: list, name: str):
    ''' Takes a list and a filename, then writes the list to the file name '''
    outfile = open(name, 'w')
    for i in range(len(d)):
        outfile.write(str(len(d)) + '\n' + d[i].name + ' $' + str(d[i].price) + ' ' + str(d[i].calories))
    outfile.close()

write_menu([Dish(name='Cheese Enchiladas', price=3.5, calories=400), Dish(name='Wet Burrito', price=6.0, calories=700), Dish(name='Chile Relleno', price=4.0, calories=600), Dish(name='Taco Salad', price=4.0, calories=400), Dish(name='Beef Taco', price=1.5, calories=250), Dish(name='Menudo', price=5.0, calories=750)], 'menu4.txt')

### d.1
print('------------------------- d.1 ----------------------')

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1 = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)

Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Clark, Clay', 'SR', 'CSE', [ics32, mgt1])
sA = Student('41223344', 'Bryant, Kobe', 'SO', 'BIM', [ics32, mgt1])
sB = Student('41223344', 'James, LeBron', 'FR', 'INFX', [ics32, mgt1])
sC = Student('41223344', 'Westbrook, Russell', 'SR', 'CGS', [ics32, mgt1])
sD = Student('41223344', 'Irving, Kyrie', 'JR', 'SE', [ics32, mgt1])
sE = Student('41223344', 'George, Paul', 'FR', 'ICS', [ics32, mgt1])


StudentBody = [sW, sX, sY, sZ, sA, sB, sC, sD, sE]

def Students_at_level(s: list, levels: str)-> list:
    ''' Returns list of students whose class level matches the level '''
    final = []
    for x in s:
        if x.level == levels:
            final.append(x)
    return final

print(Students_at_level(StudentBody, 'FR'))
print(Students_at_level(StudentBody, 'SR'))

### d.2
print('------------------------- d.2 ----------------------')

def Students_in_majors(s: list, maj: list)-> list:
    '''takes a list of Students and a list of strings (where each string represents a major)
        and returns a list of Students that have majors on the specified list.'''

    final = []
    for x in s:
        if x.major in maj:
            final.append(x)
    return final

print(Students_in_majors(StudentBody, ['CS', 'PSB']))

### d.3
print('------------------------- d.3 ----------------------')

def Students_in_class(s: list, dep: str, num: int)-> list:
    ''' takes a list of Students, and two strings—a department name and a course number
    (e.g., 'ICS' and '31')—and returns a list of those Students who are enrolled in the
    specified class.'''

    finals = []
    for x in s:
        for i in x.studylist:
            if i.dept + str(i.num) == dep + str(num):
                finals.append(x)
    return finals

print(Students_in_class(StudentBody, 'ICS', 31))

### d.4
print('------------------------- d.4 ----------------------')

def Student_names(s: list)-> list:
    ''' Takes a list of Students and just returns their names'''
    results = []
    for x in s:
        results.append(x.name)
    return results

print(Student_names(StudentBody))

### d.5
print('------------------------- d.5 ----------------------')

def Student_CSmajors(s: list)-> list:
    ''' Takes a list of Students and returns Students in ICS School '''
    results = []
    CS_majors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']
    for x in s:
        if x.major in CS_majors:
            results.append(x)
    return results

print(Student_CSmajors(StudentBody))

def Student_CSnames(s: list)-> list:
    ''' Takes a list of Students and returns names in ICS '''
    li = []
    results = Student_CSmajors(s)
    for x in results:
        li.append(x.name)
    return li

print(Student_CSnames(StudentBody))

def Student_CS_num(s: list)-> int:
    ''' The number of Students who are majors from the School of ICS '''

    result = Student_CSnames(s)
    return len(result)

print(Student_CS_num(StudentBody))

def CS_Seniors(s: list)-> list:
    ''' names of seniors who are majors in the School of ICS '''
    results = []
    CS_majors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']
    for x in s:
        if x.major in CS_majors and x.level == 'SR':
            results.append(x)
    return results

print(CS_Seniors(StudentBody))

def CS_Senior_num(s: list)-> int:
    '''  number of seniors who are majors from the School of ICS '''
    results = CS_Seniors(s)
    return len(results)

print(CS_Senior_num(StudentBody))

def CS_Senior_per(s: list):
    ''' percentage of majors from the School of ICS who are seniors'''
    senior = CS_Senior_num(s)
    return str((senior / Student_CS_num(s)) *100) + '%'

print(CS_Senior_per(StudentBody))

def Fresh_ICS31_per(s: list)-> int:
    ''' number of freshmen who are majors from the School of ICS and enrolled in ICS 31 '''
    CS = Student_CSmajors(s)
    results = Students_in_class(CS, 'ICS', 31)
    return results

print(Fresh_ICS31_per(StudentBody))

def avg_fresh_units(s: list):
    ''' average number of units that freshmen in ICS 31 are enrolled in '''
    results = []
    count = 0
    fresh = Students_at_level(s, 'FR')
    new_fresh = Students_in_class(fresh, 'ICS', 31)
    for x in new_fresh:
        for i in x.studylist:
            count += i.units
    return count / len(new_fresh)

print(avg_fresh_units(StudentBody))