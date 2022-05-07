li1=[]
n=int(input("Enter size of list1 "))
for i in range(0,n):
    e=int(input("Enter element of list1 "))
    li1.append(e)

print("Positive numbers in",li1,"are: ")
for i in li1:   
    if i >= 0:
       print(i, end = " ")
       
  
li2=[]
n=int(input("Enter size of list2 "))
for i in range(0,n):
    e=int(input("Enter element of list2 "))
    li2.append(e)
print("Positive numbers in",li2,"are: ")
for i in li2:   
    if i >= 0:
       print(i, end = " ")
