# while test_expression:
#    body of while loop
# break and continue.
#break: Breaks out from the nearest enclosing loop
#Continue: Go to the start of nearest enclosing loop.
# While <expression>
#<statement(s)>
#break
#<statement(s)>
#continue
#<statement>
#<statement>
#else clause:
#while <expression>
#< <statement(s)>
#else:
#  <statement (s)>


'''x = 0
while x <= 10:
     print(x)
     x = x + 1
     #break
     #continue
     print("inside while")
print("out of while loop")'''

'''city = "mebourne"
x = 0
while x < len(city):
    print(city[x])
    x = x + 1'''

'''x = 0
y = 0
while x <= 10:
     print(x)
     x = x + 1
     print("parent while")
     while y < 5 :
      print(y)
      y = y + 1
      continue
      #break
print("Inner loop")
print("out of while loop")'''

x = 0
while x <= 10:
     print(x)
     x = x + 1
     if x == 5:
      break
else:
    print ("out of the while")