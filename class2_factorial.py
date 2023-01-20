n=int(input("enter the number to find factorial "))
def factorial(a):
  fact=1
  if(a<0):
    print("entered no does not have fact")
  elif(a==0):
    print("fact of 0 = 1")
  else:
    for i in range (1,a+1):
      fact=fact*i
    print(fact)

factorial(n)