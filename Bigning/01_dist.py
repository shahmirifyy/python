dist= {
  "shahmir":{"name":'shahme',
  "email":"shah@g.com",
  "phone":+92314512005},
"junaid":{
  "name":'junaid',
  "email":"junaid@g.com",
  "phone":+92314512005
  },
}

# print(dist)

# print(dist["junaid"]['email'])

# list with multiple dictionary we say objects in JS
persons= [
  {"name":'shahme',
  "email":"shah@g.com",
  "phone":+92314512005
  },
{
  "name":'junaid',
  "email":"junaid@g.com",
  "phone":+92314512005
  },
]


for person in persons:
    if person["name"] == "junaid":
        person["name"] = "junaid khan"  # ← Change the name

# Print to confirm the change
for person in persons:
    # print(person["name"])
    per=person
    
d={ "name":'junaid',
  "email":"junaid@g.com",
  "phone":+92314512005}



# print(d.values())
# print(d.keys())
# print(d.pop('name'))
# d.clear() # for removing everything in the dist 
# print(d)
# d.update({'name':"ali","age":16})
# print(d.get("name")) # if the key not exist it will give the none value for that key
# print(d["name"])  # if the key not exist it will give the error for key 
# print(d)
 

