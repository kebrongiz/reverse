def prime_number(num):
    stop_num= num/2
    for value in range(2, int(stop_num)+ 1):
        if(num % value == 0):
            return False
    return True
num = int(input("Enter a number:"))
print(prime_number(num))
