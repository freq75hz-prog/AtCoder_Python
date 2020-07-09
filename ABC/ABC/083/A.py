a,b,c,d = map(int,input().split())
L = a + b
R = c + d

if L < R:
    print ('Right')
elif L > R:
    print ('Left')
else:
    print ('Balanced')