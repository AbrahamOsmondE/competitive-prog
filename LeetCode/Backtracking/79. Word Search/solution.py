class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        flag = [False]
        def backtrack(i, j, index):
            if flag[0] or i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] == "#" or len(word) == index:
                return
            

            char = board[i][j]
            if char == word[index] and index == len(word) - 1:
                flag[0] = True
                return
            if char != word[index]:
                return
            for x,y in [(1,0), (0,-1), (-1,0), (0,1)]:
                board[i][j] = '#'
                backtrack(i+x, j+y, index + 1)
                board[i][j] = char

        for n in range(len(board)):
            for m in range(len(board[0])):
                backtrack(n,m, 0)
        return flag[0]