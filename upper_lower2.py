ch=input("enter the character: ")
if(ch>='A' and ch<='Z'):
  print(ch, "is upper case alphabet")
elif(ch>='a' and ch<='z'):
  print(ch, "is lower case alphabet")
elif(ch>='0' and ch<='9'):
  print(ch, "is no between 0 and 9")
else:
  print(ch, "is other character or special symbol")