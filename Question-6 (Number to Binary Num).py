#Convert a number to binary number
num = int(input('Enter num: '))
def num2binary(num):
    binary = ""
    while num > 0:
        binary = str(num%2) + binary
        num = num//2
    print("Binary Number: ",binary) 
    return

num2binary(num)
