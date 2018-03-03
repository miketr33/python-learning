#   Dictionary Example
dogs = {'name_1':'Rox', 'breed_1':'Lab','age_1':2,'name_2':'Snoop',\
'breed_2':'Westie-Schnauzer','age_2':2}

#   Print all items in dictionary
print(dogs.items())

#   Print list of keys
print(dogs.keys())

#   Print list of values
print(dogs.values())

#   Print key + value one by on without line break (end='')
for key in dogs:
    print (key, dogs[key] ,end='')
