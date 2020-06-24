test = 'all zip files are zipped'
first_zip = test.find('zip')

print (test.find('zip', first_zip + 1))
print (test[18:])
test = "all zip files are"

mary = "Mary "
randa = mary
katie = randa
salwa = katie
kathleen = salwa
gabriel = kathleen

print (salwa)

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace("NOUN", "duck")
sentence = sentence.replace("VERB", "Walle")
print (sentence)

s = " I am a bird."
s = s.replace("bird", "man")
print (s)

def say_hello():
    return "Hello!"
print (say_hello())
def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

print (say_hello("Mary"))
print (say_hello('Andy')) # inputs and outputs

def add_two_numbers(number_1, number_2):
    return number_1 + number_2
print (add_two_numbers(4, 3))
print (add_two_numbers(2, 6))   # adding


def rest(a):
    return a[1:]
print (rest('audacity')) # using procedures

def square(n):
    return  n * n

c = 12
print (square(c))
print (square(square(c)))
y = 144
print (square(y))

def sum3(a,b,c,d):
    return ((a + b) -c) * d

print (sum3(2,18,2,4))

print (sum3(5,4,3,2))

def abbaize(a, b):
    return a + b + a + b
print (abbaize('a', 'b'))
print(abbaize('dog','cat'))
print (abbaize('dog', 'cat'))

def a(a, b):
    return a + b + b + a
print (a('owl', 'crol'))

print(2>3)
print (2*2 !=5)
print (2*2 == 4)



def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        return False
print (is_friend('Diane'))
