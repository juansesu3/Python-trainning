"""age=7
if 0<age<100: 
    print("Correct age")
else:
    print("Incorrect age")"""



"""Salary Comparation"""
"""
Manager_salary = int(input('Enter Manager Salary pleas:\n'))
print('Manager Salary: ' + str(Manager_salary))

lead_salary = int(input('Enter Lead Salary pleas:\n'))
print('Manager Salary: ' + str(lead_salary))

senior_indexer_salary = int(input('Enter indexer senior Salary pleas:\n'))
print('Manager Salary: ' + str(senior_indexer_salary))

indexer_salary = int(input('Enter indexer Salary pleas:\n'))
print('Manager Salary: ' + str(indexer_salary))

if indexer_salary<senior_indexer_salary<lead_salary<Manager_salary:
    print('Everything works correctly')
else: 
    print('Something smells wrong in this company')"""

"""scholarship program"""
"""
print("scholarship program")
distance_to_school=int(input('Enter the distance from home to school in KM:\n'))
print(distance_to_school)
number_of_siblings = int(input('Enter number of siblings in the school\n'))
print(number_of_siblings)
family_salary = int(input('Enter family salary per year\n'))
print(family_salary)

if distance_to_school>40 and number_of_siblings>2 or family_salary<20000:
    print('You can apply for a scholarship')
else:
    print('You cant apply for a scholarship')"""

print('Optional subjects')
print('computer graphics - software testing - usability and accessibility')

option = input('Enter optional subjects you selected:\n')
asignature=option.lower()

if asignature in ('computer graphics', 'software testing', 'usability and accessibility'):

    print('Optional subjects you selected: \n'+asignature)
else:
    print('The chosen subject is not available this period')

