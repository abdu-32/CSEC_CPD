n=[int(i) for i in input().split()]
n.sort()
s=0

for i in range(len(n)-1):
    if(n[i]==n[i+1]):
        s=s+1
      
print(s)
