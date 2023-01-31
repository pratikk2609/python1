def display_menu():
    print("\nMenu Categories:")
    print("1. Main Course")
    print("2. Desserts")
    print("3. Drinks")
    print("4. Exit")

def main_course():
    print("\nMain Course Options:")
    print("1. Spaghetti")
    print("2. Fried Rice")
    print("3. Chicken")
    print("4. Back to Main Menu")

def desserts():
    print("\nDessert Options:")
    print("1. Ice Cream")
    print("2. Cheesecake")
    print("3. Chocolate Cake")
    print("4. Back to Main Menu")

def drinks():
    print("\nDrink Options:")
    print("1. Lemonade")
    print("2. Ice Tea")
    print("3. Coffee")
    print("4. Back to Main Menu")

choice = 0
display_menu()

while choice != 4:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        main_course()
    elif choice == 2:
        desserts()
    elif choice == 3:
        drinks()