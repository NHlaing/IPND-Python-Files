
#  Finding String in Strings

pythagroas = "There is geometry in the humming of the strings, there is music in the spacing of the spheres."
print (pythagroas.find('string'))
print (pythagroas[40:])
print ("(pythagroas.find('t')) --> " + str(pythagroas.find('t')))
print (pythagroas[14:])
print (pythagroas.find('T'))
print ("(pythagroas.find('in')) ===>" + str(pythagroas.find('in')))

# Testing Find

Numbers = "One two three Four Five Six Seven Eight Nine Ten."
print ("(Numbers.find('F' , 15)) ====>" + str(Numbers.find('F' , 15)))
print ("(Numbers[18:]) +++>" + str(Numbers[18:]))



print ("test".find("t"))
print ("test".find('st'))
print ('test'.find('te'))
print ("test".find("test"))

# practice with string.find
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print (favorite_color)
print (favorite_color[7:])


# Finding With Numbers

danton = "De l'audace, encore de l'audace, toujours de l'audace."
print(danton.find('audace'))
print (danton.find('audace', 0))
print (danton.find('audace', 5))
print (danton.find('audace', 6))
print(danton[6:])
print(danton[25:])
print (danton.find ('audace', 25))
print (danton.find('audace', 26))
print (danton[47:])
print(danton.find('audace', 48))

# More Practice with string.find

example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
print(first)
print(second)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print (new_string)
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print (new_string)


# Make apple

apple = "Do U like it! Don't you ! You like it?"
F = apple.find('!')
S = apple.find('!', F + 1)
New = apple[:F] + apple[F +1:S] + apple[ S +1:]

print (New)
New = apple[:F] + '*'+ apple[F +1:S] + '*' + apple[ S+1:]
print (New)
