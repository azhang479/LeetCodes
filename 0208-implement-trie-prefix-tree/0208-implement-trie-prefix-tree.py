class Trie:

    #O(1) using a set
    def __init__(self):
        self.trieDict = set()
        self.prefixDict = set()

    #O(1) using a set
    #Also insert the prefixes, O(w) where w is word length
    def insert(self, word: str) -> None:
        self.trieDict.add(word)
        totalLength = len(word)
        for i in range(totalLength):
            self.prefixDict.add(word[:totalLength - i])

    #O(1) using a set
    def search(self, word: str) -> bool:
        return (word in self.trieDict)

    #O(n) startsWith, just check through all the words
    #we could maybe do a lower bound by inserting all the prefixes for a word on each word but space tradeoff
    #O(1) with the prefix dict
    def startsWith(self, prefix: str) -> bool:
        return (prefix in self.prefixDict)        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)