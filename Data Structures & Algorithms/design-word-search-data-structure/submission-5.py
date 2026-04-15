'''
trie obviously

trie made of trie nodes
trie node has letter and neighbors which are themselves
trie nodes
trie also has 'isEnd' which represents if it is a word
or not

adding a word:
start at the root
add letter to neighbors
for that letter create a new TrieNode
assign that letter in the neighbors map to that new TrieNode
current pointer becomes that new neighbor
continue until you're out of characters
the last node has its isEnd set to True
-if a node already exists don't make a new one


'''

class TrieNode:
    def __init__(self):
        self.isEnd= False
        self.neighbors = {} # map char:node

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        curNode = self.root

        for letter in word:
            if letter in curNode.neighbors:
                curNode = curNode.neighbors[letter]
            else:
                node = TrieNode()
                curNode.neighbors[letter] = node
                curNode= node

        # when done set curNode as end
        curNode.isEnd = True

    def searchStartingFrom(self,word,node)->bool:

        curNode = node 
        for i in range(len(word)):
            letter  = word[i]
            if letter == '.':
                for char,node in curNode.neighbors.items():
                    if self.searchStartingFrom( word[i+1:],node):
                        return True
                return False
            else:
                if letter not in curNode.neighbors:
                    return False
                curNode = curNode.neighbors[letter]
        return curNode.isEnd
       
    def search(self, word: str) -> bool:
        return self.searchStartingFrom(word,self.root)
        
