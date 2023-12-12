#Tuples are indexed, allow duplicate values and cannot b modified.
#(immutable) holds multi data

'''demo_tuple =(1,2,3,4,5)
demo_tuple1 = ( "Delhi","Delhi","Kolkata","Melbourne","Sydney")
demo_tuple2 = (True,False,False,True)
demo_tuple13 = (True,1,"Delhi",23.56)
print (len(demo_tuple1))

# you cannot add anything once you create tuple.'''

demo_tuple =(1,2,3,4,5)
demo_tuple1 = ( "Delhi","Delhi","Kolkata","Melbourne","Sydney")
demo_tuple2 = (True,False,False,True)
demo_tuple13 = (True,1,"Delhi",23.56)
print (demo_tuple1.count("Delhi"))
print (demo_tuple1.index("Melbourne"))

for x in demo_tuple1:
    print(x)

joined_tuple = demo_tuple1 + demo_tuple2 + demo_tuple13
print(joined_tuple)
print (type(joined_tuple))