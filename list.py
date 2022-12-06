
"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
'''Lists, Array, Vectors'''
"""in python lists can hold different types of values"""

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""

from turtle import position
listMyName = [
    'Juan',
    'Sebastian',
    'Suarez',
    'Ramirez'
]
print("Print all elemt of the list(array) [:]\n", listMyName[:])
print("Print elemt of the list(array) [position]\n", listMyName[1])
print("Print elemt of the list(array) reverse [-]\n", listMyName[-3])
print(
    "Print elemt of the list(array)  exclude [incial_position : position_range ]\n", listMyName[0:3])
print(
    "Print elemt of the list(array)  exclude [incial_position : rest_of_elemts ]\n", listMyName[2:])


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""

""".append add item to end of list """
listMyName2 = [
    'Juan',
    'Sebastian',
    'Suarez',
    'Ramirez'
]
listMyName2.append("I'm the best")
print(".append add item to end of list\n", listMyName2[:])


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
""".insert(position_insert_elemt, elemt_to_inseret) add item with position in the list """
listMyName3 = [
    'Juan',
    'Sebastian',
    'Suarez',
    'Ramirez'
]
listMyName3.insert(2, "I'm the best")
print(".insert add item with position in the list\n", listMyName3[:])

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
""".extend(position_insert_elemt, elemt_to_inseret) almost like concatenating another list"""
listMyName4 = [
    'Juan',
    'Sebastian',
    'Suarez',
    'Ramirez'
]
listMyName4.extend(["I'm", 'The', 'Best'])
print(".extend([]) almost like concatenating another list\n", listMyName4[:])

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
""".index('name_of_elemt') position of the elemt"""
listMyName5 = [
    'Juan',
    'Sebastian',
    'Suarez',
    'Ramirez'
]

position_index = listMyName5.index('Juan')
print(".index('name_of_elemt')  position of the elemt\n", position_index)


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
"""print("name_of_elemt" in list) if exist return true else return false"""
listMyName6 = [
    'Juan',
    'Sebastian',
    'Suarez',
    'Ramirez'
]
print("if exist return true")
print("Juan" in listMyName6)
print("else exist return false")
print("Juliana" in listMyName6)
listMyName6.remove('Juan')
print(".remove('name_of_elemt') remove elemt\n",listMyName6)
listMyName6.pop()
print(".pop() deleted the last elemt\n",listMyName6)

lists_concatened = listMyName6+listMyName2 

print("+ concatenator in list(array)\n",lists_concatened )

list_repeat = lists_concatened * 2
print(" * repeat\n", list_repeat)

