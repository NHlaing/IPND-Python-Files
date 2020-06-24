print ("EXAMPLE 1: Lists can contain strings")
string_list = ['HTML', 'CSS', 'Python']
print (string_list)
print ('')

print ("EXAMPLE 2: Lists can contain numbers")
number_list = [3.14159, 2.71828, 1.61308]
print (number_list)
print ('')

print ("EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons")
pi = number_list[0]
not_pi = number_list[1:]
print (pi)
print (not_pi)
print('')

print ("EXAMPLE 4: Lists can contains string AND numbers")
mixed_list = ['Hello!', 42, "Goodbye!"]
print (mixed_list)
print('')

print ('EXAMPLE 5: List can even contain other lists')
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print (list_with_lists[2])
print ('')
# Days in a Month


days_in_month = [31, 28, 31, 30, 30, 30,
                 31, 31, 30, 31, 30, 31]

def how_many_days(month):
    return days_in_month[month - 1 ]
print (how_many_days(3))

### Practice ###

COLOR = ['Blue','red',
        'yellow','brown']
def color_name(color):
    return COLOR[color - 1]
print (color_name(2))

#### Practice ####

ACTOR = ['NAY TOE','PYAE TI OO', 'NAING NAING',
         'AUNG YE LIN','MYINT MYAT','SAI SAI']

def actor_name(name):
    return ACTOR[name-1]
print ('')
print ("Who is the best actor?")
print (actor_name(1))
