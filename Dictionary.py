# Dictionaries are used to store data values in key:value pairs.
# spk={key:value}
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# dictionary also represent in ' {} '

'''dict={"name":"spk"}
print(dict)
print(type(dict))
print(dict["name"])
print(len(dict))'''


#using dict() function
'''spk=dict(name="spk",age=25,place="akvd")
print(spk)'''

'''spk = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#x = spk["model"]
#x=spk.get("model")
#x=spk.keys()
print(x)'''

'''#change values and update values
spk = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#spk["brand"]="audi"
spk.update({"year":1974})
print(spk)'''

#adding items or update
'''spk  = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#spk["colour"]="red"
spk.update({"colour":"red"})
print(spk)'''

#removing item--> pop() & popitem()  and delete & clear
'''spk= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#spk.pop("year")
#spk.popitem()
#del spk["model"]
#spk.clear()
print(spk)'''


#looping

'''spk= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#for x in spk:
#for x in spk.values():
#for x in spk.keys():
#for x,y in spk.items():
  print(x,":",y)'''

#copy
'''spk= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#x=spk.copy()
x=dict(spk)
print(x)'''


#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.

'''myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child4"  :{
      "name":"Pavan"
  }
}

#print(myfamily["child1"]["name"])

for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])'''