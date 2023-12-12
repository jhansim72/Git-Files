
'''demo_set1={"Delhi","Kolkata","Melbourne","Sydney"}
demo_set2={"Delhi","Kolkata","Melbourne","Sydney"}

print(demo_set1)
demo_set1.add("Gold Coast")
print(demo_set1)
demo_set1.pop()
demo_set1.clear()
print(demo_set1)'''
#use union method to join 2 sets
demo_set1={"Delhi","Kolkata","Melbourne","Sydney"}
demo_set2={"Delhi","Kolkata","Melbourne","Sydney"}
demo_set3 = demo_set1.union(demo_set2)

print(demo_set3)
demo_set1 = demo_set1.update(demo_set2)
print(demo_set1)

