class Trie:

    #O(1) using a set
    def __init__(self):
        self.trieDict = set()

    #O(1) using a set
    def insert(self, word: str) -> None:
        self.trieDict.add(word)

    #O(1) using a set
    def search(self, word: str) -> bool:
        return (word in self.trieDict)

    #O(n) startsWith, just check through all the words
    #we could maybe do a lower bound by inserting all the prefixes for a word on each word but space tradeoff
    def startsWith(self, prefix: str) -> bool:
        for word in self.trieDict:
            if word.startswith(prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)