try:
    num1=int(input("Enter the firs number: "))
    num2=int(input("Enter the second number: "))
    result=num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by 0 is error!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will excecute no matter what")