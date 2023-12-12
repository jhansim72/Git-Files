#Dictionaries are used to store data in key: Value pairs. They are changeble in array
#Difine dictionaries
#Accessing items from dictionary
#Adding items to dictionary
#Removing items from dictionary.
# We use curly brases {} as sets


'''demo_dict = {} #This is empty dictionary
demo_dict1 = {1:20, 2:45, 3:50, 6:67}     #1:20) 1is a key 20 is value curly braces holds key and key values
demo_dict2 = { "QA": "testurl","uat": "uaturl"}
demo_dict3 = {"qa":34, 3:"uaturl"}
#print(type(demo_dict)) # finding type
demo_dict2 ['prod']= 'produrl'  # adding value
demo_dict1.pop (1) #to remove value
print(demo_dict1[2])# finding index
print(demo_dict1)# to find added value
print(demo_dict1)# to find removed value
print(demo_dict2)'''
#Dictionary key Methods

# popitem () Removed the arbitrary key: value pair
# update()add the specified key-value pairs to dictionary
# copy() Returns a copy of the dictionary
# Clear()Removes all the elements from the dictionary

demo_dict2={"qa":"testurl","uat":"uaturl","prepod":"produrl"}
# use get method to retrieve key values
print(demo_dict2.get("prepod")) #brings specific mentioned key
print(demo_dict2.keys()) # Returns all keys and values in the array/dictionary
print(demo_dict2.items()) # Returns all the keys and values in the array/dictionary
print(demo_dict2. values()) # Returns  only values in the array/dictionary