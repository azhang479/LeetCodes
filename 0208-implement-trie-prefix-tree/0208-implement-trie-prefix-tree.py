class Trie:

    #O(1) using a set
    def __init__(self):
        self.trie = {}

    #Use a dict with root connecting to all first letters
    #Insertion adds in the letters working down the tree.
    #O(w) time for letters
    def insert(self, word: str) -> None:
        current = self.trie
        #For each letter, check if it is in the current nested tree branch
        for letter in word:
            #If it is, continue searching down letter by letter
            if letter not in current:
                current[letter] = {}
            #We have reached the end or a split, add in a spot for the last letter and swap over to it incase there are more letters
            current = current[letter]
        #At the end, we have to also assign and "end" special character to know we've inserted a word that ends here
        #Since we only insert singular letters, we can just use the word "end"
        current["end"] = True

    #O(w) time for searching down the letters
    def search(self, word: str) -> bool:
        current = self.trie
        for letter in word:
            if letter in current:
                current = current[letter]
            else:
                return False
        return ("end" in current)

    #O(w), go through all letters of the prefix. If we reach the end and dont encounter a not in, then it is a prefix
    def startsWith(self, prefix: str) -> bool:
        current = self.trie
        for letter in prefix:
            if letter in current:
                current = current[letter]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)