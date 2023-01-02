ch=input("enter the character: ")
x=ord(ch)
if(x>=65 and x<=90):
  print(chr(x), "is upper case alphabet")
elif(x>=92 and x<=122):
  print(chr(x), "is lower case alphabet")
elif(x>=48 and x<=57):
  print(chr(x), "is a digit")
else:
  print(ch(x), "is other character or special symbol")