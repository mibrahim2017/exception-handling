try:
    number=int(input("enter a number: "))
    print("the entered number is", number)
except ValueError as e:
    print("please input a valid INTEGAR value (number)",e)
