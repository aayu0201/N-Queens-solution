from tkinter import N


class Queensproblem:
    
    def __init__(self, n):
        self.n = n
        self.chesstable = [[0 for i in range(n)] for j in range(n)]
    
    def change(self):
        for i in range(self.n):
            self.chesstable[i][i] = 1
    
    def cell_valid(self,row,col):
        for j in range(col):
            if self.chesstable[row][j] == 1:
                return False
        for i in range(self.n):
            for j in range(col):
                if i+j == row + col and self.chesstable[i][j] == 1:
                    return False
                if i-j == row - col and self.chesstable[i][j] == 1:
                    return False
        return True
    
    def solve(self,col=0):
        if col == self.n:
            return True        
        for row in range(self.n):
            if self.cell_valid(row,col):
                self.chesstable[row][col] = 1
                if self.solve(col+1):
                    return True
                self.chesstable[row][col] = 0
        return False
            
            
        
    def printtable(self):
        print(self.chesstable)

if __name__ == "__main__" :
    q1 = Queensproblem(4)
    q1.printtable()
    q1.solve()
    q1.printtable()
    #q1.change()
    #q1.printtable()