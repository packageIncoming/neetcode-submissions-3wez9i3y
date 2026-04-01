
'''
Design a data structure that supports adding new words and searching for existing words.
    -Using a Trie/Prefix Tree
void addWord(word) Adds word to the data structure.
    - Simple prefix tree insert function
bool search(word) 
Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.
    -Idea: iterate over trie nodes in the regular prefix tree method for a-z letters,
    when a '.' comes up then you call a recursive function starting from all the children 
    and you can OR the results from the recursive call

Example Walkthrough:
addWord("day")
addWord("bay")
addWord("may")

search("b..")
    1. start at root check for b in children, YES, continue to step 2
    2. starting at node 'b', input character is a '.', begin recursive call on all children
        with input string '.'
        2a. Base case is when the input string is empty => return True
''' 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word=True

    def _searchStartingFrom(self,node,word) -> bool:
        curr = node
        
        for i in range(len(word)):
            letter = word[i]
            if letter == '.':
                #special '.' case
                res = False
                for child in curr.children:
                    res = res or self._searchStartingFrom(curr.children[child],word[i+1:])
                return res
            else:
                #regular case
                if letter not in curr.children:
                    return False
                curr = curr.children[letter]
        return curr.word
                

    def search(self, word: str) -> bool:
        return self._searchStartingFrom(self.root,word)
