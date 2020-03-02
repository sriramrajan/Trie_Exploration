## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        # self.root = None
        self.child = {}
        self.isEndOfWord = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.child:
            self.child[char] = TrieNode()

    def setEndOfWord(self):
        self.isEndOfWord = True
    
    def suffixes(self, suffix = '', listofSuffixes = []):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if suffix == '':
            listofSuffixes = [] # Reset list at begininng
        
        if (self.isEndOfWord == True):
            listofSuffixes.append(suffix)
            # print ("Suffix: ", suffix, "List: ", ", ".join(listofSuffixes))

        if self.child == {}:
            return listofSuffixes
        
        for letter in self.child:
            temp = suffix
            suffix += letter

            node = self.child[letter]
            listofSuffixes =  node.suffixes(suffix, listofSuffixes)
            suffix = temp # remove last appended suffix
        return listofSuffixes
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        for idx in range(len(word)):
            self.insertAtIndex(idx, word)
        # idx = 0
    
    def insertAtIndex(self, index, word):
        node = self.root
        for letterIndex in range(index, len(word)):
            letter = word[letterIndex]
            if letter not in node.child:
                node.insert(letter)
            
            node = node.child[letter]
        node.setEndOfWord()

    def existsPrefix(self, prefix):
        node = self.root

        for letter in prefix:
            if letter in node.child:
                node = node.child[letter]
            else:
                return False
        return True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        letter = prefix[0]
        if letter not in node.child:
            return None
        # if len(prefix) == 1:
        #     return node.child[letter]

        if (self.existsPrefix(prefix)):
            for letter in prefix:
                if letter in node.child:
                    node = node.child[letter]
                else:
                    # print (node.child.keys())
                    break
                # print("Letter: ", letter)
            return node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry",
]
'''"ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", '''
for word in wordList:
    MyTrie.insert(word)

assert(MyTrie.existsPrefix("antag") == True)
assert(MyTrie.existsPrefix("Abcd") == False)
assert(MyTrie.find("tri").suffixes(suffix="", listofSuffixes=[]) == ['e', 'gger', 'gonometry'])
assert(MyTrie.find("f").suffixes() == ['un', 'unction', 'actory'])
