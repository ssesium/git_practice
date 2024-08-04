import sys
s=set([])
n=int(sys.stdin.readline().strip())
for i in range(n):
    command=sys.stdin.readline().strip().split()
    if command[0]=='add':
        s.add(int(command[1]))
    if command[0]=='remove':
        s.discard(int(command[1]))
    if command[0]=='check':
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    if command[0]=='toggle':
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1]))
    if command[0]=='all':
        s=set(range(1,21))
    if command[0]=='empty':
        s.clear()