#python program to make a calculator and perform operations based on user's choice

#taking two numbers input from user
num1=float(input("Enter the First Number::--"))
num2=float(input("Enter the Second Number::--"))
while(True):
#creating a menu for the operations
        print("***********************MENU***********************")
        print("Following are the operations to perform::--")
        print("  CHOICE CODE          OPERATION       ")
        print("    1.           Addition of",num1,"and",num2,"\n    2.           Substraction of",num1,"from",num2,"\n    3.           Substraction of",num2,"from",num1)
        print("    4.           Multiplication of",num1,"and",num2,"\n    5.           Division of",num1,"to",num2,"\n    6.           Division of",num2,"to",num1)
        print("    7.           Square of",num1,"\n    8.           Square of",num2,"\n    9.           Square root of",num1)
        print("    10.          Square root of",num2)

        #asking the  user to enter the choice code for respective operations
        ch=int(input("Enter the Choice code::--"))

        #using if elif ans else statements to follow operations based on user's choice code 
        if ch==1:
            sum1=num1+num2
            print("The Addition of",num1,"and",num2,"is::",sum1)
        elif ch==2:
            sub1=num2-num1
            print("The Substraction of",num1,"from",num2,"is::",sub1)
        elif ch==3:
            sub2=num1-num2
            print("Substraction of",num2,"from",num1,"is::",sub2)
        elif ch==4:
            mul=num1*num2
            print("Multiplication of",num1,"and",num2,"is::",mul)
        elif ch==5:
            div1=num1/num2
            print("Division of",num1,"to",num2,"is::",div1)
        elif ch==6:
            div2=num2/num1
            print("Division of",num2,"to",num1,"is::",div2)
        elif ch==7:
            sq1=num1*num1
            print("Square of",num1,"is::",sq1)
        elif ch==8:
            sq2=num2*num2
            print("Square of",num2,"is::",sq2)
        elif ch==9:
            sr1=num1**0.5
            print("Square root of",num1,"is::",sr1)
        elif ch==10:
            sr2=num2**0.5
            print("Square root of",num2,"is::",sr2)
        else:
            print("INVALID CHOICE")    