inputstr= input("Enter the string: ")
strarray= inputstr.split()
print(strarray)

newarr=[]
for stri in strarray:
    for i in range(int((len(stri)+1)/2)):
        arrstr=list(stri)
        tmp=arrstr[i]
        arrstr[i]=arrstr[len(arrstr)-1-i]
        arrstr[len(arrstr)-1-i]=tmp
        stri=''.join(arrstr)
    newarr.append(stri)
print(newarr)

newstr=''
for item in newarr:
    newstr= newstr + str(item) + ' '
print(newstr)

