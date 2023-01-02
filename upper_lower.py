ch=input("enter the letter: ")

if ch.isupper():
  print(ch, "is upper case alphabet")
elif ch.islower():
  print(ch, "is lower case alphabet")
else:
  print(ch, "is neither upper nor lower case alphabet")