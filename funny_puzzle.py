import heapq
import numpy as np
import time




def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0
    to_state = np.array(to_state)
    to_state.resize(3,3)
    from_state = np.array(from_state)
    from_state.resize(3,3)

    if np.array_equal(from_state, to_state) == False:
        for row in range(3):
            for col in range(3):
                if from_state[row,col] != to_state[row,col]:
                    if from_state[row,col] == 0:
                        continue
                    from_state_coordinate = [row,col]
                    result = np.where(to_state == from_state[row,col])
                    to_state_coordinate = list(zip(result[0], result[1]))
                    sub_result = np.subtract(from_state_coordinate,to_state_coordinate)
                    distance += (abs(sub_result[0,0]) + abs(sub_result[0,1]))                
        return distance
    else:
        return distance
    




def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state): 
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    succ_states = []
    state = np.array(state)
    # succ_states.append(state.tolist())
    matrix = state.reshape(3,3)
    zero_result = np.where(matrix == 0)
    index_list= list(zip(zero_result[0], zero_result[1]))
    
    for index in index_list: # zero index in matrix  
        if index[1] == 0:
            # bottom
            tempbottom = state.copy();
            tempMatrix4 = tempbottom.reshape(3,3)
            tempMatrix4[index[0],index[1]] = tempMatrix4[index[0],index[1]+1]
            tempMatrix4[index[0],index[1]+1] = 0
            succ_states.append(tempbottom.tolist())
        if index[0] == 0:
            # right
            tempright = state.copy(); 
            tempMatrix2 = tempright.reshape(3,3)
            tempMatrix2[index[0],index[1]] = tempMatrix2[index[0]+1,index[1]]
            tempMatrix2[index[0]+1,index[1]] = 0
            succ_states.append(tempright.tolist())
        if index[1] == 2:
            # top
            temptop = state.copy();
            tempMatrix3 = temptop.reshape(3,3)
            tempMatrix3[index[0],index[1]] = tempMatrix3[index[0],index[1]-1]
            tempMatrix3[index[0],index[1]-1] = 0
            succ_states.append(temptop.tolist())  
        if index[0] == 2:
            # left
            templeft = state.copy();  
            tempMatrix1 = templeft.reshape(3,3)
            tempMatrix1[index[0],index[1]] = tempMatrix1[index[0]-1,index[1]]
            tempMatrix1[index[0]-1,index[1]] = 0
            succ_states.append(templeft.tolist())  
        if index[1] == 1:
            # top
            temptop = state.copy();  
            tempMatrix3 = temptop.reshape(3,3)
            tempMatrix3[index[0],index[1]] = tempMatrix3[index[0],index[1]-1]
            tempMatrix3[index[0],index[1]-1] = 0
            succ_states.append(temptop.tolist())
            # bottom
            tempbottom = state.copy();
            tempMatrix4 = tempbottom.reshape(3,3)
            tempMatrix4[index[0],index[1]] = tempMatrix4[index[0],index[1]+1]
            tempMatrix4[index[0],index[1]+1] = 0
            succ_states.append(tempbottom.tolist())
        if index[0] == 1:
            # left
            templeft = state.copy();
            tempMatrix1 = templeft.reshape(3,3)
            tempMatrix1[index[0],index[1]] = tempMatrix1[index[0]-1,index[1]]
            tempMatrix1[index[0]-1,index[1]] = 0
            succ_states.append(templeft.tolist())
            # right
            tempright = state.copy();
            tempMatrix2 = tempright.reshape(3,3)
            tempMatrix2[index[0],index[1]] = tempMatrix2[index[0]+1,index[1]]
            tempMatrix2[index[0]+1,index[1]] = 0
            succ_states.append(tempright.tolist()) 
            
    succ_states = [succ_states[i] for i in range(len(succ_states)) if i == succ_states.index(succ_states[i])] # remove duplicate list
    if state.tolist() in succ_states:
        succ_states.remove(state.tolist())                  
    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    pq = []
    parent_index = -1
    g = 0
    closed_list = []
    closed_node = []
    uid = 0
    result_node = None
    max_queue_length = None
    trace_list = []
    heapq.heappush(pq,(g+get_manhattan_distance(state), state, (g, get_manhattan_distance(state), parent_index, uid)))
    
    while len(pq)!= 0:
        node = heapq.heappop(pq)
        closed_list.append(node[1])
        closed_node.append(node)
        
        if node[1] == goal_state:
            result_node = node
            max_queue_length = len(pq)+1
            trace_list.insert(0,result_node)
            break
        else:
            for succ in get_succ(node[1]):
                # if closed add to pq
                if succ not in closed_list:
                    g = node[2][0]+1
                    parent_index = node[2][3] # uid
                    uid += 1
                    heapq.heappush(pq, (g+get_manhattan_distance(succ), succ, (g, get_manhattan_distance(succ), parent_index, uid)))            
                # else do nothing
                else:
                    continue
    
    index = 0
    while len(trace_list) != result_node[2][0]+1:
        for c in closed_node:
            if trace_list[index][2][2] == c[2][3]:
                trace_list.append(c)
                break
        index += 1
    
    trace_list = trace_list[::-1]
    for l in trace_list:
        print(f"{l[1]} h={get_manhattan_distance(l[1])} moves: {l[2][0]}")  
    
    print(f"Max queue length: {max_queue_length}") 
            
        


if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,0,6,7,0,3])
    print()
    


