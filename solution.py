#################################################################################
## CREATED BY : ANISH RAJESH ADNANI
## SUBJECT: (CSCI 561) FOUNDATIONS OF ARTIFICIAL INTELLIGENCE
## HOMEWORK 1
## LANGUAGE USED : PYTHON 3
##LAST EDITED 22-09-2021 20:33

#######################################ALL IMPORT FILES###############################################
import math
import queue
from datetime import datetime

#######################################IMPORTING ENDS HERE###########################################
######################################COMMON FUNCTIONS##############################################
def goalstatecheck(new_node, exit):
    if new_node == exit:
        return True
    else:
        return False

def singleoutput(entry):
    f = open("output.txt","w+")
    f.write(str(0)+"\n")
    f.write(str(1)+"\n")
    f.write(str(entry[0])+" "+str(entry[1])+" "+str(entry[2])+" 0")
    f.close()

##################################COMMON FUNCTIONS END HERE#########################################
######################################A* CODE STARTS HERE###############################################


def astaroutput(path):
    cost = []
    cost.append(0)
    for x in range(len(path)-1):
        temp = abs(int(path[x+1][0]) - int(path[x][0])) + abs(int(path[x+1][1]) - int(path[x][1])) + abs(int(path[x+1][2]) - int(path[x][2]))
        if temp >=2: ## if traversed diagonally cost is 14
            cost.append(14)
        else: ## travelled straight, hence cost is 10
            cost.append(10)

    f = open("output.txt","w+")
    f.write(str(sum(cost))+"\n")
    f.write(str(len(path))+"\n")
    f.write(str(path[0][0]) + " " + str(path[0][1]) + " " + str(path[0][2]) + " 0\n")
    for x in range(1,len(path)-1):
        f.write(str(path[x][0]) + " " + str(path[x][1]) + " " + str(path[x][2]) + " "+str(cost[x]) + "\n")
    f.write(str(path[len(path)-1][0]) + " " + str(path[len(path)-1][1]) + " " + str(path[len(path)-1][2]) + " "+str(cost[len(path)-1]))


    f.close()
def backtrackastar(parent,entry,exit):
    path = [exit]

    while path[-1]!=entry:
        path.append(parent[str(path[-1][0])+","+str(path[-1][1])+","+str(path[-1][2])]) ## entering parent of current node into path

    path = path[::-1]

    astaroutput(path)
    return path

def heuristic(node, exit):
    i = abs(node[0] - exit[0])
    j = abs(node[1] - exit[1])
    k = abs(node[2] - exit[2])

    ans = int(math.sqrt(i*i + j*j + k*k))
    return ans


def astar(entry,exit,dict,grid_size):
    parent = {}
    frontier = queue.PriorityQueue()
    visited = set()

    entry_path_cost = heuristic(entry,exit)

    # f, g, h, node
    frontier.put((entry_path_cost,0,entry))


    while len(frontier.queue)!=0:

        full_node = frontier.get()
        node = full_node[2]
        node_f = full_node[0]
        node_g = full_node[1]

        if goalstatecheck(node,exit):
            return backtrackastar(parent,entry,exit)

        visited.add(tuple(node))
        temp = str(node[0])+","+str(node[1])+","+str(node[2])
        if dict.get(temp)!=None:
            possible_moves = dict.get(temp)
            for y in possible_moves:
                moving =[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],[1,0,1],[1,0,-1],[-1,0,1],[-1,0,-1],[0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1]]
                #new_node = [-1,-1,-1]

                current_move = moving[y-1]
                new_node = [a+b for a,b in zip(node,current_move)]


                checking = -1
                for z in range(len(frontier.queue)):
                    if new_node == frontier.queue[z][2]:
                        checking = z
                        break

                if y in [1,2,3,4,5,6]:
                    cc = 10
                else:
                    cc = 14

                n = tuple(new_node)
                if n not in visited and checking==-1:
                    if new_node[0]<grid_size[0] and new_node[0]>=0 and new_node[1]<grid_size[1] and new_node[1]>=0 and new_node[2]<grid_size[2] and new_node[2]>=0:
                        new_node_h = heuristic(new_node,exit)
                        new_node_g = node_g + cc
                        new_node_f = new_node_h + new_node_g
                        frontier.put((new_node_f,new_node_g,new_node))
                        parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])] = node

                elif checking!=-1:
                    old_cost = frontier.queue[checking][0]
                    if old_cost > node_g + cc + heuristic(new_node,exit):
                        new_node_h = heuristic(new_node,exit)
                        new_node_g = node_g + cc
                        new_node_f = new_node_h + new_node_g

                        frontier.queue.pop(checking)
                        frontier.put((new_node_f,new_node_g, new_node))

                        del parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])]
                        parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])] = node




        #if temp in dict:


    if len(frontier) == 0:
        return 'FAIL'
#######################################A* CODE ENDS HERE ###################################################
######################################UCS CODE STARTS HERE#####################################################
def ucsoutput(path):
    cost = []
    cost.append(0)
    for x in range(len(path)-1):
        temp = abs(int(path[x+1][0]) - int(path[x][0])) + abs(int(path[x+1][1]) - int(path[x][1])) + abs(int(path[x+1][2]) - int(path[x][2]))
        if temp >=2: ## if traversed diagonally cost is 14
            cost.append(14)
        else: ## travelled straight, hence cost is 10
            cost.append(10)

    f = open("output.txt","w+")
    f.write(str(sum(cost))+"\n")
    f.write(str(len(path))+"\n")
    f.write(str(path[0][0]) + " " + str(path[0][1]) + " " + str(path[0][2]) + " 0\n")
    for x in range(1,len(path)-1):
        f.write(str(path[x][0]) + " " + str(path[x][1]) + " " + str(path[x][2]) + " "+str(cost[x]) + "\n")
    f.write(str(path[len(path)-1][0]) + " " + str(path[len(path)-1][1]) + " " + str(path[len(path)-1][2]) + " "+str(cost[len(path)-1]))


    f.close()

def backtrackucs(parent, entry,exit):
    #print(parent)
    path = [exit]  ## we will move from goal node to root node using its parent

    while path[-1]!=entry:
        #print("hi")
        path.append(parent[str(path[-1][0])+","+str(path[-1][1])+","+str(path[-1][2])]) ## entering parent of current node into path

    path = path[::-1]


    ucsoutput(path)
    return path
def ucs(entry,exit,dict,grid_size):
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #print("UCS started at =", current_time)

    frontier = queue.PriorityQueue()
    #frontier = []
    visited = set()
    parent = {}
    frontier.put((0,entry))


    while len(frontier.queue)!=0:


        #frontier.sort(reverse=False)
        full_node = frontier.get()

        node = full_node[1]
        node_cost = full_node[0]
        if goalstatecheck(node,exit):
            return backtrackucs(parent,entry,exit)


        visited.add(tuple(node))
        temp = str(node[0])+","+str(node[1])+","+str(node[2])
        if dict.get(temp)!=None:
            possible_moves = dict.get(temp)

            for y in possible_moves:
                moving =[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],[1,0,1],[1,0,-1],[-1,0,1],[-1,0,-1],[0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1]]
                #new_node = [-1,-1,-1]

                current_move = moving[y-1]
                new_node = [a+b for a,b in zip(node,current_move)]
                #if goalstatecheck(new_node,exit):
                    #parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])] = node
                    #return backtrackucs(parent,entry,exit)

                checking = -1
                for z in range(len(frontier.queue)):
                    if new_node == frontier.queue[z][1]:
                        checking = z
                        break

                if y in [1,2,3,4,5,6]:
                    cc = 10
                else:
                    cc = 14
                n = tuple(new_node)
                if n not in visited and checking==-1:
                    if new_node[0]<grid_size[0] and new_node[0]>=0 and new_node[1]<grid_size[1] and new_node[1]>=0 and new_node[2]<grid_size[2] and new_node[2]>=0:
                        frontier.put((node_cost+cc, new_node))
                        parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])] = node

                elif checking!=-1:
                    old_cost = frontier.queue[checking][0]

                    if old_cost > node_cost + cc:

                        frontier.queue.pop(checking)
                        frontier.put((node_cost+cc, new_node))

                        del parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])]

                        parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])] = node





    if len(frontier.queue) ==0:
        return 'FAIL'
######################################UCS CODE ENDS HERE #####################################################
######################################BFS CODE STARTS HERE ##########################################
def bfsoutput(path):
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #print("Printing file started at =", current_time)
    f = open("output.txt","w+")
    if len(path) == 0:
        f.write("FAIL")
        f.close()

    f.write(str(len(path) - 1)+"\n")
    f.write(str(len(path))+"\n")
    f.write(str(path[0][0]) + " " + str(path[0][1]) + " " + str(path[0][2]) + " 0\n")
    for x in range(1,len(path)-1):
        f.write(str(path[x][0]) + " " + str(path[x][1]) + " " + str(path[x][2]) + " 1\n")
    f.write(str(path[len(path)-1][0]) + " " + str(path[len(path)-1][1]) + " " + str(path[len(path)-1][2]) + " 1")

    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #print("Printing file completed at =", current_time)
    f.close()

## BFS BACKTRACK
def backtrack(parent,entry,exit):
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #print("Backtracking started at =", current_time)
    path = [exit]  ## we will move from goal node to root node using its parent
    #print(path[-1][2])
    #print(path)

    while path[-1]!=entry:
        #print("hi")
        path.append(parent[str(path[-1][0])+","+str(path[-1][1])+","+str(path[-1][2])]) ## entering parent of current node into path

    path = path[::-1]
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #print("Backtracking ended at =", current_time)
    bfsoutput(path)

    return path

## BFS FUNCTION
def bfs(entry, exit, dict,grid_size):
    parent = {}
    queue = []
    visited = set()
    queue.append(entry)
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")

    while queue:

        node = queue.pop(0)
        visited.add(tuple(node))
        #print(node) ## check this for node format
        if goalstatecheck(node,exit): ## reached at goal state
            #now = datetime.now()
            return backtrack(parent,entry,exit)


        temp = str(node[0])+","+str(node[1])+","+str(node[2])
        if dict.get(temp)!=None:
            move_of_node = dict.get(temp)
            #print(move_of_node[0])
            for x in range(len(move_of_node)): ## to explore all nodes in that level
                ###### doing all the operations to find new node###########
                moving =[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],[1,0,1],[1,0,-1],[-1,0,1],[-1,0,-1],[0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1]]
                new_node = [-1,-1,-1]

                tempss = moving[int(move_of_node[x]) - 1]
                new_node = [a+b for a,b in zip(node,tempss)]



                ############# new node computed ###########
                ## now check if its already visited ##########
                #print(new_node[0]<=grid_size[0])
                n = tuple(new_node)
                if n not in visited : ##check here is this new_node is visited or not
                    if new_node[0]<grid_size[0] and new_node[0]>=0 and new_node[1]<grid_size[1] and new_node[1]>=0 and new_node[2]<grid_size[2] and new_node[2]>=0:
                        parent[str(new_node[0])+","+str(new_node[1])+","+str(new_node[2])] = node ## above checking if new_node is inside the grid or not
                        queue.append(new_node)



    if len(queue) == 0:
        return 'FAIL'
#####################################BFS CODE ENDS HERE####################################################
with open("input.txt") as f:
    lines = f.read()
    algorithm_choice = lines.split('\n',1)[0]

f = open("input.txt",'r')
lines = f.readlines()

#for line in lines:
    #line = line.strip()
lines[1] = lines[1].strip() ## to remove \n from end of line
lines[2] = lines[2].strip() ## entry point
lines[3] = lines[3].strip() ## exit point
lines[4] = lines[4].strip() ## number of nodes with actual moves
grid_size = list(lines[1].split(" "))
entry = list(lines[2].split(" "))
exit = list(lines[3].split(" "))
nodes_with_moves = list(lines[4].split(" "))
node = [] ## contains all nodes and their actions represented in number format

entry[0] = int(entry[0])
entry[1] = int(entry[1])
entry[2] = int(entry[2])

exit[0] = int(exit[0])
exit[1] = int(exit[1])
exit[2] = int(exit[2])

grid_size[0] = int(grid_size[0])
grid_size[1] = int(grid_size[1])
grid_size[2] = int(grid_size[2])

#print(entry)
for y in range(int(nodes_with_moves[0])):
    lines[5+y] = lines[5+y].strip()
    node.append(list(lines[5+y].split(" ")))
dict = {}
for z in range(len(node)):
    key = node[z][0] + "," + node[z][1] + "," + node[z][2]
    #print(key)
    temp = []
    for m in range(3,len(node[z])):
        temp.append(int(node[z][m]))

    dict[key] = temp


if algorithm_choice == "BFS":
    print("started finding path using BFS")
    if entry == exit:
        singleoutput(entry)
    else:
        result = bfs(entry,exit,dict,grid_size)
        if result == 'FAIL':
            f = open("output.txt","w+")
            f.write("FAIL")
            f.close()

elif algorithm_choice == "A*":
    print("started finding path using A* algorithm")
    if entry == exit:
        singleoutput(entry)
    else:
        result = astar(entry,exit,dict,grid_size)
        if result == 'FAIL':
            f = open("output.txt","w+")
            f.write("FAIL")
            f.close()


elif algorithm_choice == "UCS":
    print("started finding path using Uniform cost search")
    if entry==exit:
        singleoutput(entry)
    else:
        result = ucs(entry,exit,dict,grid_size)
        if result == 'FAIL':
            f = open("output.txt","w+")
            f.write("FAIL")
            f.close()
