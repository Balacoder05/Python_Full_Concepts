# n=int(input("enter the value:"))
# for i in range(n):
#     print("*",end="")


n=int(input("enter the value:"))
for i in range(1,n+1):
    for i in range(1,i+1):
        print("*",end="")
    print()