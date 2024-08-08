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
        curr["*"] = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = set()
        def backtrack(row, col, parent):
            letter = board[row][col]
            curr = parent.get(letter, {})

            word_match = curr.get("*", False)
            if word_match:
                ans.add(word_match)
            
            board[row][col] = '#'
            for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + x, col + y
                if newRow < 0 or newCol < 0 or newRow >= len(board) or newCol >= len(board[0]):
                    continue
                if not board[newRow][newCol] in curr:
                    continue
                
                backtrack(newRow, newCol, curr)
            board[row][col] = letter

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i,j,trie.trie)
        return ans

        