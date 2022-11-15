a = int(input("enter"))
b = 0
while a >0:
    rem =a%10
    a = a//10
    b = rem **3 + a**3
    print(b)
