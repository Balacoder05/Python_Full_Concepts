def add_pannu(a,b):
    result=a+b
    return result
output=add_pannu(5,10)
print(output)

new=add_pannu(4,5)
print(new)

#Build in function

a=2
b=3
c=pow(a,b)
print(c)

e=10
a=[1,2,3,4,5]
print(min(a))
print(max(a))


#user defined function

def call_pannu(a):
    result=a
    return result

print(call_pannu("call Balamurugan"))

#default argumrt

def say_hello():
    print("Hello")

def total(*numbers):
    print("Total=",sum(numbers))
total(10,20,30)


#lamda function

add_pannu=lambda a,b :a*b

output=(add_pannu(10,5))
print(output)

# def greet():
#     print("Hello")
#     greet()
# greet()

#map()
#map(function,iterable)
a=[1,2,3,4,5]
result=map(lambda x:x*2,a)
print(list(result))

#filter
#filter(function,iterable)

a=[1,2,3,4,5]
result=filter(lambda i:i%2==0,a)
print(list(result))


from functools import reduce

a=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,a)
print(result)

