a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
list=[]
list.append(a)
list.append(b)
list.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i != j & j != k & k!=i):
                print(list[i],list[j],list[k])