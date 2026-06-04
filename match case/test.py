x = int(input("Enter a number:"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x % 2 == 0:
        print("x is a even number")
    case _ if x != 0:
        print("x is an odd number")
    case _ :
        print(x)