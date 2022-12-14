#write a python code to get remainder of two integers by following ways
#basic operator
#modulus operator
#divmod operator

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
print("Quotient and remainder by basic operators")
print("Quotient=", int(a/b), "Remainder=", a-b*(int(a/b)))        #basic operator
print("Quotient=", a//b, "Remainder=", a%b)                       #modulus operator
print("Quotient=", divmod(a,b)[0], "Remainder=", divmod(a,b)[1])  #divmod operator