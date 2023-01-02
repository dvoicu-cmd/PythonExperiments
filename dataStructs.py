#Lists
#Flexable, can have lists within lists. can store multiple data types within. Order is important in lists

myList = [1,2,3,4]
print(myList)
len(myList) #The length of the list. Should be 4

#Sets, Like lists, but unordered as you know and all elements are unique
mySet = {1,2,3,4,4}
print(mySet)
len(myList)

#Tuples. Order maters. You can't add anything to tuples
myTuple = (1,2,3)
len(myTuple)
myList.append(6) #This is allowed. But myTuple.append is not allowed. This is more memory efficient. Like x,y,z points

#Dictionaries. These are key and value pairs. Order does not matter. Unique values only. Kind of like sets.
myDictionary = {
    'apple': 'A red fruit', #This gets replaced
    'bear': 'A friend',
    'apple': 'Sometimes are green'
}
#call a key
myDictionary['apple']