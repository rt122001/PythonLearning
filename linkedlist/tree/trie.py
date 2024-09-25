#Python code for Search operation of tries algorithm
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEndOfWord = True
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEndOfWord
    def startsWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
    def getRoot(self):
        return self.root
def printWords(node, prefix):
    if node.isEndOfWord:
        print(prefix)
    for ch, child in node.children.items():
        printWords(child, prefix + ch)
if __name__ == '__main__':
    car = Trie()
   #Inserting the elements
    car.insert("Lamborghini")
    car.insert("Mercedes-Benz")
    car.insert("Land Rover")
    car.insert("Maruti Suzuki")
    print("Tries elements are: ")
    printWords(car.root, " ")
    #Searching elements
    print("Searching Cars")
    #Printing the searched elements
    print("Found?",car.search("Lamborghini"))     # Output: True
    print("Found?",car.search("Mercedes-Benz"))   # Output: True
    print("Found?",car.search("Honda"))           # Output: False
    print("Found?",car.search("Land Rover"))      # Output: True
    print("Found?",car.search("BMW"))             # Output: False
    #printing elements name starts with?
    print("Cars name starts with")
    print("Does car name starts with 'Lambo'?", car.startsWith("Lambo"))       # Output: True
    print("Does car name starts with 'Hon'?",car.startsWith("Hon"))         # Output: False
    print("Does car name starts with 'Hy'?",car.startsWith("Hy"))          # Output: False
    print("Does car name starts with 'Mer'?",car.startsWith("Mer"))         # Output: True
    print("Does car name starts with 'Land'?",car.startsWith("Land"))        # Output: True    