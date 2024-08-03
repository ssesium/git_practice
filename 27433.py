n=int(input())
if n==0:
    print(1)
else:
    result=1
    for i in range(1,1+n):
        result*=i
    print(result)

