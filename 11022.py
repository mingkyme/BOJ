count = int(input())
for i in range(1,count+1):
    num1,num2 = map(int,input().split())
    print("Case #{}: {} + {} = {}".format(i,num1,num2,num1+num2))