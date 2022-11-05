# factorial
'''def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1)
a = int(input())
print(factorial(a))'''



# use of key

'''def a_f(a):
    return(a[0])
a=[[5,9],[6,6],[7,5]]
a.sort(key=a_f)
print((a))'''

# random
'''import random
ran=random.randint(0,10)
# print(ran)
rand=random.random()*100
print(rand)
lst= ["star plus","dd1","aaj tak"]
choice=random.choice(lst)
print(choic)'''

# argument
'''def fun(*arg):
    print(type(arg))
    print(arg)
    for i in arg:
        print(i)
a=["harry","ujj","ggg","jjj"]
fun(*a)'''

# arg uses
'''def fun(*arg):
    print(arg)
    print(arg[0],arg[1],arg[2])

fun(19,20,25)'''

# kwargs is dictonary

'''def fun(**kwargs):
for key, value in kwargs.items():'''

# time
'''import time
initial = time.time()
print(initial)
a=5
b=6
print(a+b)
print(time.time()-initial)
k=0
while (k<45):
    print("thos is my")
    time.sleep(2)
    k+=1'''

# enumerate function
'''ll=["ggg","gddd","wwww","dews0"]
for index , item in enumerate(ll):
    if index%2==0:
        print(f"{item}")
print(0%2)'''









