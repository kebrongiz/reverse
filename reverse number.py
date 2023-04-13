def reverse_number():
    num = input("Enter number to be reversed:")

    while int(num) < 0 :
        print("please enter posetive intiger")
        num = input("Enter number to be reversed :")
    print("The reversed number is {}".format(num[::-1]))

reverse_number()
