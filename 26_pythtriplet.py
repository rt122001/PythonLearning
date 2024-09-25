limit= int(input("Enter the upper limit of triplet: "))

m=2
c=0

while c<limit:
    for n in range(1,m):
        a= m**2 - n**2
        b= 2*m*n
        c= m**2 + n**2
        if c > limit:
            break
        print(a,b,c)
    m = m+1