inputstr = input("Enter the string: ")
words = []
word = ''

for i in inputstr:
    if i != ' ':
        word = word + i
    else:
        words.append(word)
        word = ''
words.append(word)#to append last word
print(len(words))
