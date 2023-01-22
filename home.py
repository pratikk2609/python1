n=int(input("enter no of elements:"))
list=[]
factorlist=[]
for i in range(n):
    x=int(input())
    list.append(x)

print("list is ",list)
print("the length of the list is ", len(list))

def printmatrixorder(num, factorlist):
    for i in range(len(factorList)):
        for j in range(len(factorList)):
            if factorList[i] * factorList[j] == num:
                print("**********Matrix with order m=", factorList[i], " X n=", factorList[j])
                printMatrix(list, factorList[i], factorList[j])


def printMatrix(lst, m, n):
    idx=0;
    for i in range(m):
        for j in range(n):
            print(lst[idx], end=" ")
            idx = idx +1
        print("\n")


def printfactors(x):
    tempf = []
    print("factors are:")
    for i in range(1, x + 1):
        if x % i == 0:
            tempf.append(i)
    print(tempf)
    return tempf

num = len(list)
factorList = printfactors(num)
printmatrixorder(num,factorlist)

'''printmatrixorder(num, factorList)'''

'''
printMatrix(list, 2, 2)
print("------------")
printMatrix(list, 4, 1)
print("------------")
printMatrix(list, 1, 4)
'''

