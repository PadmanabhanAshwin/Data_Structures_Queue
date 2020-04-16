# Data_Structures_Queue

Queue Data Structures Implementation example: 

In a given grid, each cell can have one of three values:

- the value 0 representing an empty cell;
- the value 1 representing a fresh orange;
- the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Given below: instance progression for: 

``
grid = [[2,1,1],[1,1,0],[0,1,1]]
``
![alt text](/backtracking.png)