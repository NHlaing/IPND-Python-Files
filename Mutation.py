# mutation
s = 'Hello'
s = 'Yello'
s = s + 'w'
print (s)

# A list of strings

p = ['H','e','l', 'l','o']
print (p)
p[0] = 'Y'
print (p)
p[4] = '!'
print (p)

# Different Stooges

stooges = ['Moe','Larry', 'Curly']
stooges[2] = 'Shemp'
print ("stooges  ===>  " + str(stooges))

# Yello Mutation

p = ['H', 'e', 'l', 'l', 'o']
q = p
p[0] = 'Y'
print(p)
print(q)


# Secret Agent Man

spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1
print (agent[2])

# Replace_Spy
spy =[0,0,7]

def replace_spy(spy):
    spy[2]+=1
    return spy
print(replace_spy(spy))  # from User's answer:



spy = [0,0,7]
p = spy

def replace_spy(p):
    p[2] = p[2] + 1
    return p
print(replace_spy(p)) # .solution video

# list Operation

stooges = ['moe', 'larry', 'curly']
stooges.append('Shemp')
print (stooges)

# Testing length

p = [1,2]
p.append(3)
p = p + [4,5]              # operator
print (p)
print (len(p))

# Testing Append

p =[1,2]
q =[3,4]
p.append(q)                 # .append
print (p)
print(len(p))
