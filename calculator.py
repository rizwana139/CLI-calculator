#calculator.py
print("\t___CALCULATOR CLI APP___")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a > b:
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    return q, r
while(True):
    print("\n\nChoose the Operation you want to perform: ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.EXIT")

    choice = int(input('>'))
    if choice == 1:
       print("\n\nEnter the two numbers: ")
       num1 = int(input('>'))
       num2 = int(input('>'))
       s = sum(num1,num2)
       print("\nThe sum is : %s" %s)

    elif choice == 2:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        d = sub(num1,num2)
        print("\nThe difference is : %s" %d)
    elif choice == 3:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        m = mul(num1,num2)
        print("\nThe product is: %s" %m)
    elif choice == 4:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        q, r = div(num1,num2)
        print("\nThe Quotient is : %s" %q)
        print("\nThe Remainder is : %s" %r)
    else:
        print("\nYou chose to exit.Bye.....")
        break

