def sum_list(a, b, c):
    return (a+ b +c)
print(sum_list(1,7,4)) # own

# Sum list
# Answer


def sum_list(list):
    return sum(list)
print (sum_list([1,3,6]))  # User's answer:


def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result

print (sum_list([1, 7, 4])) # .solution:

# measure_udacity

def measure_udacity(list):
    count = 0
    for name in list:
        if name[0] == 'U':
            count+= 1
    return count

print (measure_udacity(['Dave','Sebastian', 'Katy']))
print (measure_udacity (['Umika', 'Umberto', 'Uule']))


def measure_udacity(list):
    result = 0
    for adj in list:
        if adj[0] == 'D':
            result = result + 1
    return result

print (measure_udacity(['Done','Well','Dear']))
