# Trie_Exploration

A Trie node was designed to use suffix tree. Initially, the algorithm was designed for all suffixes with O(N²) complexity. This can be seen on commented lines of class Trie:

    def insert(self, word):
        ## Add a word to the Trie
        idx = 0
        # for idx in range(len(word)):
        self.insertAtIndex(idx, word

Later, on seeing the implementation in **ipywidgets** the code was chagned to only store first suffix O(N). This would be the entire word alone.

### Time Complexity:
For insert, time complexity is O(N) for storing each character in the Trie. 

For search, again it is O(N) which is split between the **existsPrefix** method and the **find** methods of **class Trie**

The **suffixes** method creates a list of suffixes at each node and uses *backtracking* to remove the last added suffix. The necessary time complexity is **O(N + M)**, where **N** is the number of children, and **M** is the combined length of the suffixes at each child

Total time complexity is weighed most by the **suffixes** method at **O(N + M)**

### Space Complexity: 

Insert method uses a space of O(N) for each character in the word.

Searching done via **find** and **existsPrefix** is constant at O(1) since we are only traversely the Trie

**suffixes** method is creating a list of size **O(N + M)** and leads the space complexity.
