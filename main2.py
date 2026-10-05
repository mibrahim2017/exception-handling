try:
    num1=int(input("enter a number: "))
    num2=int(input("enter another number: "))
    result= num1 / num2
    print("result is:", result)
except ZeroDivisionError as a:
    print(f"{num1} is not divisible by {num2};",a)
except ValueError as v:
    print("please enter a valid number; ", v)
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will excecute no matter what;")