menu = int(input("   ORDER PLEASE \n 1.starter-water,main course-burger&fries"
"\n 2.starter-fruit juice,main couse-puri bhaji"
" \n 3.starter-masala papad,main course-panner butter masala,desert-colddrinks"
" \n \n "
"Select Yours"))

if menu == 1:
    print("starter-water,main course-burger&fries price ₹100 ")

    confirm =int(input("confirm to press one"))

    if confirm ==1:
        print("Order confirmed")
    else:
        print("chose correct option")

elif menu == 2:
    print("starter-fruit juice,main couse-puri bhaji ₹200")

    confirm = int(input("confirm to press one"))

    if confirm == 1:
        print("Order confirmed")
    else:
        print("chose correct option")

elif menu == 3:
    print("starter-masala papad,main course-panner butter masala,desert-colddrinks ₹300")

    confirm = int(input("confirm to press one"))

    if confirm == 1:
        print("Order confirmed")
    else:
        print("chose correct option")

else:
    print("Wrong Choice")


def intro():
    name=input("enter name: ")
    people=int(input("enter no of people: "))
    rec_menu=input("do u want recommended menu or whole menu?")
    foodtype=input("veg or non-veg")
    hungerlevel=input("enter hunger level: ")
    budget=int(input("enter budget:"))
    dessert=input("do u want dessert or not?")

intro()