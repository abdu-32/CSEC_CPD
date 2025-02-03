num = int(input())
string = input()
c = 0
d = 0
 
for i in range(num):
    if( string [i] == "A" ):
        c = c + 1
    elif( string [i] == "D" ):
        d = d + 1
        
if( c > d ):
    print("Anton")
    
elif( d > c ):
    print("Danik")
    
else:
    print("Friendship")
