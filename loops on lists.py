#def print_all_elements(p):
#    i = 0
 #   while (i<=p):
  #      print (p[i])
   #     i = i + 1
#print_all_elements(6)


#  For loops

print("Numbers")
my_list =['1','2','[3,4]']
for num in my_list:
    print (num)
print( len(num))

# For Loop playground

print ("EXAMPLE 1: We can use for loops to go through a list of strings")
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print (thing)

print ("EXAMPLE 2: We can use for loops on nested lists too!")
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print (capital + ' is the capital of ' + country)


# Practice......

print ("Question 1: Have you watched the best 'Korean Series' and you know the actors names?")
names_1 = [['Crash landing on you', 'Hyun Bin and Son Ye-jin'],
           ['Godblin', 'Gong Yoo and Kim Go-eun'],
           ['DOTS', 'Song Joong-Ki and Song Hye-kyo']]
for series_with_actors in names_1:
    series = series_with_actors[0]
    actors = series_with_actors[1]
    print ("(series + ' is the best series and' + actors +' include in this series.')====>     " + str(series + ' is the best series and' + actors +' include in this series.'))


## practice;;;

print ('Question 2: Which places have you been in Myanmar?')
places = [['Bangan',  'a beautiful place'],
          ['Inlay',  ' one of the peaceful place'],
          ['SuHlay' , 'a commercial city']]
for P_with_P1 in places:
    P = P_with_P1[0]
    P1 = P_with_P1[1]

    print (">>> "+P + P1  + ' in Myanmar.' )
