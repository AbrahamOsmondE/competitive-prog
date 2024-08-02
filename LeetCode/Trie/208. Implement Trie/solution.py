class Trie(object):

    def __init__(self):
        self.trie = {}
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.trie
        for char in word:
            if curr.get(char, None) == None:
                curr[char] = {}
            curr = curr[char]    
        curr["*"] = True 

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.trie
        for char in word:
            if curr.get(char, None) == None:
                return False
            curr = curr[char]
        return curr.get("*", False)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.trie
        for char in prefix:
            if curr.get(char, None) == None:
                return False
            curr = curr[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)