num1, num2 = map(int,input().split())

num2 = num2 - 45

if(num2 < 0):
    num2 = 60 + num2
    num1 = num1 - 1
    if(num1 < 0):
        num1 = 23
print(num1,num2)