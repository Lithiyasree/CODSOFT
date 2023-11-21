while True:
    print("#SIMPLE CALCULATOR#")
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.FLOOR DIVISION\n6.MODULUS\n7.EXPONENTIATION")
    ch=int(input("Enter your choice:"))
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    if ch==1:
        print("\nThe SUM of ",num1,"and",num2,"is: ",num1+num2)
    elif ch==2:
        print("\nThe DIFFERENCE of ",num1,"and",num2,"is: ",num1-num2)
    elif ch==3:
        print("\nThe PRODUCT of ",num1,"and",num2,"is: ",num1*num2)
    elif ch==4:
        print("\nQuotient with fractional part")
        if num2==0:
            print("Cannot divide by zero")
            num2=float(input("Enter the second number:"))
            print("\nThe QUOTIENT of ",num1,"and",num2,"is: ",num1/num2)
        else:
           print("\nThe QUOTIENT of ",num1,"and",num2,"is: ",num1/num2)
    elif ch==5:
        print("\nquotient without fractional part\n")
        if num2==0:
            print("Cannot floor divide by zero")
            num2=float(input("Enter the second number:"))
            print("\nThe QUOTIENT of ",num1,"and",num2,"is: ",num1//num2)
        else:
           print("\nThe QUOTIENT of ",num1,"and",num2,"is: ",num1//num2)
    elif ch==6:
        print("\nResult will be Remainder")
        if num2==0:
            print("Cannot divide by zero")
            num2=float(input("Enter the second number:"))
            print("\nThe REMAINDER of ",num1,"and",num2,"is: ",num1%num2)
        else:
           print("\nThe REMAINDER of ",num1,"and",num2,"is: ",num1%num2)
    elif ch==7:
        print(num1,"POWER",num2,"is",num1**num2)
    else:
        print("\nInvalid choice.\nPlease enter a valid choice.")
        break
        
        
        
