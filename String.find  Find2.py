text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""
noun_position = text.find('NOUN')
verb_position =text.find('VERB')
print (noun_position)
print (verb_position)
print (text[125:])
print (text[171:])

#  Bodacious Udacity

s ='udacity'
t = 'bodacious'
print(s[0]+t[2:])

 #  find 2

test = 'all zip files are zipped'
first_zip = test.find('zip')

print (test.find('zip', first_zip + 1))
print (test[18:])

test = 'all zip files are compressed'
first_zip = test.find("zip")

print (test.find('zip', first_zip+ 1))


Flower= ' Most of the person likes Rose but some of person does not like it.'
first_person = Flower.find('person')
print (first_person)
print ( Flower[13:])
print(Flower.find ("does", first_person +1))
print (Flower[50:])         # Eg find 2
