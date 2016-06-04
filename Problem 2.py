s=0
f = [1,1]
x=0
while f[1] < 4000000:
    x = f[0] + f[1]
    if x%2 == 0:
        s = s+x
    a=f[1]
    f[0]=a
    f[1]=x
print s, 'is the answer'


        
