# word=input("Enter your text")
# a=word[::-1]
# if(word==a):
#     print("is a palindrom")
# else:
#     print("not a palindrom")

# #count even number

# count=0
# for i in range(1,10+1):
#     if(i%2==0):
#         count=count+1
# print(count)

# #factorial

# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(n,"Of factorial :",fact)

#perfect number

# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if(n==sum):
#     print(n,"is perfect number")
# else:
#     print(n,"is not perfect number")

#fibonacci series

n=int(input())
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,b+a

#another method
n=int(input())
f=0
s=1
for i in range(n):
    print(f)
    t=f+s
    f=s
    s=t

#vowels

a=input("Give me a input").lower()
vowels="aeiou"
count=0
for i in a:
    if (i in vowels):
        count=count+1
print(count)

#pattern

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()