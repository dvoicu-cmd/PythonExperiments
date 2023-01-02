#If/Else syntax
a = True
if a:
    print('this') #part of if statement
else:
    print('this otherwise')
print('always this')


print('\n')
#double indent
b = True
c = True
if b:
    print('next')
    if c:
        print('my head hurts')
else:
    print('what to do')
print('this is always printed')


print('\n')
#loops over iterables
d = [1,2,3,4,5,6,7]
for item in d: #the 'in' in this case is just part of the syntax. and 'item' can be changed to whatever the programer wants.
    print(item)

for thing in d: 
    print(thing)


print('\n')
#While loops
e = 0
while e < 5:
    print(e)
    e = e + 1 