inputstr = input("Enter the string: ")
chardict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

for letter in inputstr:
    for key in chardict:
        if letter == key:
            chardict[key]=chardict[key]+1

for x in chardict.values():
    if x < 1:
        flag=1
    else:
        flag=0

if flag==1:
    print("Not a pangram")
else:
    print("Pangram")