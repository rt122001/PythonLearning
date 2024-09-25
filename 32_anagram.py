str1= input("Enter the string1: ")
str2= input("Enter the string2: ")
trimstr1=str1.replace(" ","")
trimstr2=str2.replace(" ","")
liststr1= list(trimstr1)
sortstr1= sorted(liststr1)
liststr2= list(trimstr2)
sortstr2= sorted(liststr2)

if sortstr1==sortstr2:
    print("Anagram.")
else:
    print("Not an anagram.")