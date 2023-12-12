#Zip functions: will map data in  two different variable.
'''list1 = ["India","USA","Australia","UK"]
list2 = ["Pune","New York","Sydeny","London","Melbourne"]'''
#print (type(list1))
#print (type(list2))
#s = zip (list1,list2)
#print(list(s))

total_cost = [55,77,89,87]  # lists
sale_price=  [45,67,65,76]
for x,y in zip(total_cost,sale_price) :
 print(x-y)

total_cost = (55,77,89,87) # Tuples
sale_price=  (45,67,65,76)
for x,y in zip(total_cost,sale_price) :
 print(x-y)




