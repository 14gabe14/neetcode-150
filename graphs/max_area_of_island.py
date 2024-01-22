
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

def print_grid():
    for i in range(len(grid)):
        print(grid[i])


diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(i : int, j : int):
    area = 0
    queue = [(i, j)]
    
    while len(queue) > 0:
        x, y = queue.pop()

        if grid[x][y] == 1:
            grid[x][y] = None
            area += 1
            for (dx, dy) in diff:
                nx = x+dx
                ny = y+dy
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == 1:
                    queue.append((nx,ny))

    return area

max_area = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            max_area = max(dfs(i, j), max_area)
            print(max_area)
            
            print_grid()
            print()


print(max_area)
