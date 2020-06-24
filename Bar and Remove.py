
def bar(n, ch= '='):
    """A horizontal bar of lengrh n."""
    return ch * n
def separator (html=False):
    """Horizontal line, either in plain text or HTML."""

x=bar(7)
print ("x is ", x)
def box(txt):
    """Put txt inside a box."""
    print ("+" + bar(len(txt)) + "+")
    print ("| " + txt          + " |")
    print ("+" + bar(len(txt)) + "+")
box (" Warmly Welcome!!!! ")




# Check Intermediate Results


def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)

    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

print (remove('audacity', 'a'))
print (remove('pythonic', 'ic'))
print (remove('substring institution', 'string in'))
print (remove('ding', 'do'))
print (remove('doomy', 'dooming'))


def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location == -1:
        return somestring
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

print (remove("ding", "do"))
print (remove("doomy", "dooming"))
