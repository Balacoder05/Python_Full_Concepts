word=input("Enter your text")
a=word[::-1]
if(word==a):
    print("is a palindrom")
else:
    print("not a palindrom")

#count even number

count=0
for i in range(1,10+1):
    if(i%2==0):
        count=count+1
print(count)

#factorial

n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(n,"Of factorial :",fact)