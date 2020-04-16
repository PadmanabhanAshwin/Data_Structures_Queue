#%%
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        num_col = len(grid[0])
        num_row = len(grid)
        #print("Number of rows= ", num_row, "Number of Columns = ", num_col)
        
        class O():
            def __init__(self, x, y, layer):
                self.x = x
                self.y = y
                self.layer = layer
                
        def valid(i, j, row_num, col_num, movement):
            assert(movement in ["U", "D", "L", "R"]), "Invalid movement"
            if movement == "U":
                if i == 0:
                    return False
                return True
            if movement == "D":
                if i == (row_num - 1):
                    return False
                return True
            if movement == "L":
                if j == 0:
                    return False
                return True
            if movement == "R":
                if j == col_num -1:
                    return False
                return True
        
        movement_vec = {
            "U": [-1,0],
            "D": [1,0],
            "L": [0, -1],
            "R": [0,1]
        }
        self.layer = 0
    
        q = deque()
        visited = [[False for _ in range(num_col)] for _ in range(num_row) ]
        #print(visited)
        #create the queue:
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == 2:
                    q.appendleft(O(i, j, 0))
                    visited[i][j] = True
                if grid[i][j] == 0:
                    #print("row = ", i, "col = ", j, "found 0")
                    visited[i][j] = True
        #print(visited)

        if sum([x for y in visited for x in y ]) == num_row*num_col:
            return self.layer
  
        while(len(q) > 0):
            self.layer+=1
            #print(self.layer, "th infection")
            for _ in range(len(q) -1, -1, -1):
                rotten_tomato = q[len(q) - 1]
                #print("Rotten tomato x= ",rotten_tomato.x,"Rotten tomato y= ", rotten_tomato.y  )
                for movement in ["U", "D", "L", "R"]:
                    #print("Valid move? = ",valid(rotten_tomato.x, rotten_tomato.y, num_row, num_col, movement) )
                    if valid(rotten_tomato.x, rotten_tomato.y, num_row, num_col, movement) and not visited[rotten_tomato.x + movement_vec[movement][0]][rotten_tomato.y + movement_vec[movement][1]]:
                        #print("Valid tomatoes found @ ", rotten_tomato.x + movement_vec[movement][0], ",", rotten_tomato.y + movement_vec[movement][1])
                        q.appendleft(O(rotten_tomato.x + movement_vec[movement][0], rotten_tomato.y + movement_vec[movement][1], self.layer))            
                        visited[rotten_tomato.x + movement_vec[movement][0]][rotten_tomato.y + movement_vec[movement][1]] = True
                q.pop()
            if sum([x for y in visited for x in y ]) == num_row*num_col:
                return self.layer

        return -1
                        
                           
solution = Solution()
solution.orangesRotting(grid = [[0,1,0],[1,2, 1],[0,1,0]])
        
        
        

#%%
