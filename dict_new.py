'''
thisdict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
thisdict.pop("model")
print(thisdict)
'''


'''
thisdict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
thisdict.popitem()  #last inserted item is removed using pop item
print(thisdict)
'''


'''
thisdict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
del thisdict["model"]  #del = deletes the item
print(thisdict)
'''


''''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)  #dict is deleted so errors occurs
'''

'''
thisdict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
thisdict.clear()  #clears dictionary
print(thisdict)
'''


'''
thisdict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
thisdict["color"]="red"  #adding items in dict
print(thisdict)
'''

'''
thisdict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
thisdict.update({"color":"blue"})  #update/add colour item to the dictionary
print(thisdict)
'''

'''
thisdict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
thisdict["year"]=2018  #change year
print(thisdict)
'''


''''
thisdict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
x = thisdict.get("model")  #accessing elements
'''


'''
car = {
"brand":"Ford",
"model":"Mustang",
"year":1964
}
x = car.values()
print(x)
car["year"]=2020  #change original dict
print(x)
'''


thisdict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
if "model1" in thisdict:    #checks if specific key is present
  print("Yes,'model' is one of the keys in the thisdict")
else:
  print("no")

