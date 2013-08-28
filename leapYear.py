def determineLeap(n):
    if n % 4 == 0:
        print(str(n) + " is a leap year!")
        return True
    if n % 100 == 0:
        print(str(n) + " is not a leap year!")
        return False
    if n % 400 == 0:
        print(str(n) + " is a leap Year")
        return True
    else:
        print("Fail!  This isn't even close!")
        return False
determineLeap(int(input("Enter a year: ")))
