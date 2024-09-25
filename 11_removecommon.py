def remcommon(list1):
        for i in range(0,len(list1)):
                for j in range(0,i):
                        if i!=j and list1[i]==list1[j]:
                                x=list1[j]
                                commonel.append(x)
        
        
        noncommonlist=[]
        for x in list1:
        	for y in commonel:
        		if x!=y and x not in noncommonlist:
        			noncommonlist.append(x)

        print(noncommonlist)



list1=[1,2,3,4,5,6,7,8,9,10,2,4,6,8,10,12,14,16,18,20]
commonel=[]
remcommon(list1)
