class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        #Greedy DFS? 
        #Find first letter, then expand?
        #or actaully BFS probably works better since you can count characters and prune
        #BFS with a visited set actually doesn't work as we may need to backtrack the visited set at some points. So, DFS is better as it allows us to backtrack.
        self.found = False
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    temp = board[i][j]
                    board[i][j] = "#"
                    if self.DFS(i, j, board, word, 1):
                        return True
                    board[i][j] = temp
                    
        return False
    
    def DFS(self, i, j, board, word, letter):
        if letter >= len(word):
            return True


        check = [(0,1), (1,0), (-1,0), (0, -1)]
        for x, y in check:
            curr_i = i + x
            curr_j = j + y

            #Out of bounds
            if curr_i < 0 or curr_i >= len(board) or curr_j < 0 or curr_j >= len(board[0]):
                continue

            #check letters that are adjacent, if it matches next letter, recurse in
            if board[curr_i][curr_j] == word[letter] and (curr_i, curr_j):
                temp = board[i][j]
                board[i][j] = "#"
                if self.DFS(curr_i, curr_j, board, word, letter + 1):
                    return True
                board[i][j] = temp

        #If queue has run out and we don't have our word, return false
        return False

