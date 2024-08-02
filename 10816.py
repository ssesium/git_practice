n=int(input())
li=list(map(int,input().split()))
dic={}
for value in li:
    if value in dic:
        dic[value]+=1
    else:
        dic[value]=1
m=int(input())
lis=list(map(int,input().split()))
l=[]
for value in lis:
    if value in dic:
        l.append(dic[value])
    else:
        l.append(0)
print(" ".join(map(str,l)))