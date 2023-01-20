min = 0
max = 100
for i in range(1, 11):
    age = int((min + max) / 2)
    answer = input('are you ' + str(age) + ' years old ')
    if answer.lower() == 'correct':
        print("have a nice day")
        break
    elif answer.lower() == 'less':
        max = age
    elif answer.lower() == 'more':
        min = age
    else:
        print("wrong answer")

else:
    print("your out of turn")