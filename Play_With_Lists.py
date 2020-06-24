nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

second_concept = nested_list[2]

print ("What do you think this will print?")
print (second_concept)

print ("Since second_concept was itself a list, we can access its elements")
first_title = second_concept[0]
first_description = second_concept[1]


print ("What will this print?")
print (first_title)
print (first_description)
