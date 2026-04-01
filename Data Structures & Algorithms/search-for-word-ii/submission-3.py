class Solution:
    class TrieNode:
        def __init__(self):
            self.is_word=False
            self.word_idx=-1
            self.children={}

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # idea: turn words list into a Trie and then try to iterate through using the board
        ROWS = len(board)
        COLS = len(board[0])
        foundWords = []
        trieRoot = self.TrieNode()

        for i,word in enumerate(words):
            curNode = trieRoot
            for letter in word:
                if letter not in curNode.children:
                    curNode.children[letter] = self.TrieNode()    
                curNode = curNode.children[letter]
            curNode.word_idx = i
            curNode.is_word=True

        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
        def findWordsStartingAt(r,c,node,seen):
            nonlocal foundWords
            if (r,c) in seen:
                return
            if r<0 or c<0 or r>= len(board) or c >= len(board[0]):
                return # out of bounds
            if node.is_word == True and node.word_idx !=-1:
                foundWords.append(words[node.word_idx])
                node.word_idx=-1
            seen.add((r,c))
            for rChange,cChange in DIRECTIONS:
                newR, newC = r+rChange, c+cChange
                if (newR >=0 and newR < ROWS ) and (newC >=0 and newC < COLS):
                    # valid, in bounds point
                    if board[newR][newC] in node.children :
                        findWordsStartingAt(newR,newC,node.children[board[newR][newC]],seen)
            seen.remove((r,c))
            
        for R in range(len(board)):
            row = board[R]
            for C in range(len(row)):
                if board[R][C] in trieRoot.children:
                    print(f"search start at {R},{C}: {board[R][C]}")
                    findWordsStartingAt(R,C,trieRoot.children[board[R][C]],set((R,C)))

        
        return foundWords