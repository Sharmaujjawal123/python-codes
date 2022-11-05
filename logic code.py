
# input times print output using split to input at a same line

'''z=int(input("how many time print: "))
n = 0
while n<z:
    a , b=input("enter").split()
    if a<b:
        print("Good")
    elif a==b:
        print("well")
    elif a>b:
        print("Nice")
    n=n+1'''


# multiply the value upto n times


'''a = int(input())
b=1
d=1


while b<=a:

    d=b*d
    b=b+1
    print(d)'''

# print only even part of string assign with (a)

'''a ="abcdefghklmnopqmnuh0ngbmojonoyfvgdccsxctdxxrstuv"
print(len(a))
b = 2
while b<len(a):
    print(a[b])
    b =b+2'''

# find greatest and smallest number

'''l= []
i= 0
while(i<10):
    n= int(input())
    l.append(n)
    i=i+1
l.sort()
print(l[-1])
print(l[0])'''

# use of end
'''a = 2
b=4
print(a+b,a-b,end=" end use to print all out in same line")'''

# reverse the number using end

'''a = int(input())

while a>0:
    r = a%10
    a = a//10
    print(r,end="")'''