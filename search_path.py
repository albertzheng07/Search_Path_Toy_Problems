# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

# Robot Search Grid Problem by expanding open set
# always return to minimum cost for new search until goal is reached

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [2,2]#[len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # Initialize open list
    g_value = 0
    print("initial open list: \n", [g_value] + init, "\n --------- \n")
    open_list = [[g_value] + init]
    current_pos = [open_list[0][1], open_list[0][2]]
    searched_list = []
    searched_list.append(current_pos)
    while (current_pos != goal):
        # get take list from open_list
        take_list = findTakeList(open_list)
        print("take list item: \n", take_list, "\n --------- \n")        
        # generate new open list
        current_pos = [take_list[1], take_list[2]] # set current position to take position
        open_list = generateNewOpenList(open_list, grid,take_list, delta, searched_list)

        if not(open_list is None):
            for i in range(len(open_list)):       
                searched_list.append([open_list[i][1],open_list[i][2]])
            # check if pos is at goal, otherwise continue 
            print("open list items: \n --------- \n")
            for i in range(0,len(open_list)):
                print(open_list[i], "\n")         

    path = take_list

    return path

def findTakeList(list_in):
    take_list = list_in[0]
    smallestG = list_in[0][0]
    for i in range(0,len(list_in)):
        if (smallestG > list_in[i][0]): # check if open list contains smaller value than g value
            take_list = list_in[i] # replace take list if so        

    return take_list

def generateNewOpenList(open_list, grid, take_list, delta, search_list):
    # generate new open list from take_list
    current_pos = [take_list[1], take_list[2]]
    open_list.remove(take_list) # remove take list from open list
    for i in range(0,len(delta)): # check all possible motion stpes
        move = [a + b for a, b in zip(current_pos, delta[i])] # add change in position to current position
        in_grid = move[0] >= 0 and move[0] <= len(grid)-1 and move[1] >= 0 and move[1] <= len(grid) # check that move is within grid
        if in_grid:
            if (not(grid[move[0]][move[1]]) and not(move in search_list)):   # check within grid, not occupied or searched previously
                open_list.append( [take_list[0]+1] + move) # add to open list with updated g value from current take list and new move position

    return open_list

path = search(grid,init,goal,cost)

print("The Path is ", path ,"!\n")
