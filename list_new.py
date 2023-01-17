'''
thislist=["apple","banana","cherry"]
print(thislist)
'''

'''
thislist=["apple","banana","cherry","apple","cherry"]
print(thislist)
'''

'''
thislist=["apple", "banana", "cherry"]
print(len(thislist))
'''

'''
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
'''

'''
thislist = list(("apple","banana","cherry")) #list()constructor
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
print(thislist[1]) #accessing
'''

'''
thislist = ["apple","banana","cherry"]
print(thislist[-1])  #last item = -1
'''

'''
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5]) #3rd,4th,5th
'''

'''
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])  #beginning to kiwi
'''

'''
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])  #fro cherry to end
'''

'''
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[-4:-1])  #orange to melon excluding mango
'''

'''
thislist = ["apple","banana","cherry"]
if "apple2" in thislist:
  print("Yes,'apple' is in the fruits list")
else:
    print("no")
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango" #change
print(thislist)
'''

'''
thislist = ["apple","banana","cherry","orange","kiwi",]
thislist[1:3] = ["mango", "watermelon"]
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")  #inset() method
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
thislist.append("orange")  #append() - add something
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)  #extend() - merge two lists
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
thislist.remove("banana") #remove
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
thislist.pop(1)  #pop() = remove 
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
thislist.pop()  #pop() = remove last
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
thislist.clear()  #clear() - clear list
print(thislist)
'''

'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  #sort() - alphabetically
print(thislist)
'''

'''
thislist = [100,50,65,82,23]
thislist.sort()  #sort() - numerically
print(thislist)
'''

'''
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse = True)  #sort() - reverse
print(thislist)
'''

'''
thislist = [100,50,65,82,23]
thislist.sort(reverse = True)
print(thislist)
'''

'''
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()  #copy() - copy a list
print(mylist)
'''