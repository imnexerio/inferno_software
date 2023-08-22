from copy import deepcopy

inittal = [[4,3,6],[7,8,2],[5,1,0]]
goal_ = [[1,2,3],[4,5,6],[7,8,0]]

state_history = []
maax_val = 123456789 #for infinity

def solv(current_state):

    total_distance = 0
    
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            
            cur_pos = (i*3) + j + 1
            
            if current_state[i][j] == 0:
                continue
            
            for k in range(len(goal_)):
                for l in range(len(goal_[k])):
                    
                    if current_state[i][j] == goal_[k][l]:
                        
                        goal_pos = (k*3) + l + 1
                        
                        abs_diff = abs(goal_pos-cur_pos)
                        
                        if abs_diff >= 3:
                            total_distance += int(abs_diff/3) + abs_diff%3
                        else: total_distance += abs_diff

    return total_distance



def display():
    print(inittal[0])
    print(inittal[1])
    print(inittal[-1])

    #print()



def moves():    
    possible_moves = [0,1,2,3]
    
    for i in range(len(inittal)):
        for j in range(len(inittal[i])):
            if inittal[i][j] == 0:
                if j == 2: possible_moves.remove(1)
                if j == 0: possible_moves.remove(3)
                if i == 0: possible_moves.remove(0)
                if i == 2: possible_moves.remove(2)
                
                return possible_moves

def explore(move):
    current_state = deepcopy(inittal)
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            if current_state[i][j] == 0:
                if move == 0:                 
                    current_state[i][j] = current_state[i-1][j]
                    current_state[i-1][j] = 0
                    if current_state not in state_history:
                        return solv(current_state)
                    return maax_val
                elif move == 1:                 
                    current_state[i][j] = current_state[i][j+1]
                    current_state[i][j+1] = 0
                    if current_state not in state_history:
                        return solv(current_state)
                    return maax_val
                elif move == 2:                 
                    current_state[i][j] = current_state[i+1][j]
                    current_state[i+1][j] = 0
                    if current_state not in state_history:
                        return solv(current_state)
                    return maax_val
                elif move == 3:                 
                    current_state[i][j] = current_state[i][j-1]
                    current_state[i][j-1] = 0
                    if current_state not in state_history:
                        return solv(current_state)
                    return maax_val



def execute(move):

    state_history.append(deepcopy(inittal))
    for i in range(len(inittal)):
        for j in range(len(inittal[i])):
            if inittal[i][j] == 0:
                if move == 0:                 
                    inittal[i][j] = inittal[i-1][j]
                    inittal[i-1][j] = 0
                elif move == 1:                 
                    inittal[i][j] = inittal[i][j+1]
                    inittal[i][j+1] = 0
                elif move == 2:                 
                    inittal[i][j] = inittal[i+1][j]
                    inittal[i+1][j] = 0
                elif move == 3:                 
                    inittal[i][j] = inittal[i][j-1]
                    inittal[i][j-1] = 0

                return 

step_count = 0 
def __main__():
    global step_count
    display()
    while (inittal != goal_):
        possible_moves = moves()
        best_move = possible_moves[0]
        smallest_score = explore(best_move)

        for move in possible_moves:
            move_score = explore(move)
            if move_score < smallest_score:
                smallest_score = move_score
                best_move = move
                

        execute(best_move)
        step_count=step_count+1
        print(step_count)
        display()

__main__()
print(step_count)