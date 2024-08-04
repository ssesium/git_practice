def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        memo[0]=0
        return(0)
    elif n==1:
        memo[1]=1
        return(1)
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
    
T=int(input())
for i in range(T):
    N=int(input())
    if N==0:
        print("1 0")
    elif N==1:
        print("0 1")
    else:
        print(" ".join(map(str,[fib(N-1),fib(N)])))