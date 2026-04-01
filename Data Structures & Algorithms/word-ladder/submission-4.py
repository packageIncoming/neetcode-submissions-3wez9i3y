class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getDifference(s1,s2):
            dif = 0
            for i in range(len(s1)):
                # all strings are of equal length
                if s1[i] != s2[i]:
                    dif+=1
            return dif
        adjHash = defaultdict(set)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(i+1,len(wordList)):
                otherWord = wordList[j]
                if getDifference(word,otherWord) == 1:
                    # connected
                    adjHash[word].add(otherWord)
                    adjHash[otherWord].add(word)

        if endWord not in adjHash:
            return 0

        q = collections.deque()
        q.append(beginWord)
        seen = set()
        level = 1
        while q:
            for i in range(len(q)):
                print(q)
                word = q.popleft()
                if word == endWord:
                    return level
                if word in seen: continue
                seen.add(word)
                # unseen word that is not the one we want
                # expand its children
                for child in adjHash[word]:
                    if child not in seen:
                        q.append(child)
            level+=1
        return 0