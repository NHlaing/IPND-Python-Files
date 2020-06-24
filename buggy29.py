def printExample(a, b):
    print (a + b)

def printInches(n):
    print (str (n) + " inches")

printExample('long  ', 'word')
printExample( 17 ,    23)
printInches(42)




def bracket(text):
    return '[' + text + ']'

# def blodwrap(s)
#   return '<b>' + s + '</b>'
def bracket2(text):
    return '<b>' + text +  '</b>'

print (bracket2("This is so important"))



def bracket(text):
    return '[' + text + ']'

# def boldwrap(s)
#   return "<b>" + s + "</b>"

def boldwrap(text):
    return  "<b>" + text + "</b>"

print (boldwrap("test"))



def bar(n, ch='-'):
    """A horizontal bar of length n."""
    return ch * n

def separator(html=False):
    """A horizontal line, either in plain text or HTML."""
    if html:
        print ("<hr />")
    else:
        print (bar(40))

x = bar(5)
print ("x is ", x)
def box(txt):
    """Put txt inside a box."""
    print ("+-" + bar(len(txt)) + "-+")
    print ("| " + txt           + " |")
    print ("+-" + bar(len(txt)) + "_+")
box("Hello")



def bar(n, ch='-'):
    """A horizontal bar of length n."""
    return ch * n

def separator(html=False):
    """A horizontal line, either in plain text or HTMl."""
    if html:
        print ("<hr />")
    else:
        print (bar(40))

x = bar(5)
print ("x is ", x)

def box(txt):
    """Put txt inside a box."""
    print ("+-" + bar(len(txt )) + "-+")
    print ("| " + txt            + " |")
    print ("+-" + bar(len(txt))  + "-+")
box("Sweet")

def bar(n, ch= "-"):
    """A horizontal bar of length n."""
    return ch * n
def separator(html=False):
    """A horizontal line, either in plain text or HTML."""
    if html:
        print ("<hr/>")
    else:
        print (bar(40))
x = bar(5)
print ("x is ", x)
def box(txt):
    """Put txt inside a box."""
    print ("**" + bar(len(txt)) + "**")
    print ("| " + txt           + " |")
    print ("**" + bar(len(txt)) + "**")
box ("Good Evening!")


def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location == -1:
        return somestring
    length = len(sub)
    print ("# length", length)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    print ("# before and after", part_before, part_after)
    return part_before + part_after

print (remove("audacity", "a"))
print (remove("pythonic", "ic"))
print (remove("substring institution", "string in"))
print (remove("ding", "do"))
print (remove("doomy", "dooming"))
print (remove("ding", "do "))
