import numpy as np
input = np.array(
        [[7,0,0,0,2,8,3,0,5],
         [0,5,0,0,0,0,0,0,4],
         [0,0,1,0,4,5,9,0,0],
         [0,2,8,0,0,0,0,6,0], 
         [3,0,0,5,8,1,0,0,2],
         [0,7,0,0,0,0,8,4,0],
         [0,0,2,7,1,0,4,0,0],
         [6,0,0,0,0,0,0,3,0],
         [4,0,7,2,3,0,0,0,6]])

grid = {(i, j): input[i,j] for i in range(9) for j in range(9)}

def validate_input(sudoku):
    ret = True
    ret = ret and (sudoku.shape==(9,9))
    for i in range(9):
        filled = [x for x in sudoku[i,:] if x > 0]
        ret = ret and (len(filled) == len(set(filled)))
        filled = [x for x in sudoku[:,i] if x > 0]
        ret = ret and (len(filled) == len(set(filled)))
        filled = [sudoku[3 * (i // 3) + k1, 3 * (i % 3) + k2] for k1 in range(3) for k2 in range(3) if 
                  sudoku[3 * (i // 3) + k1, 3 * (i % 3) + k2] > 0]
        ret = ret and (len(filled) == len(set(filled)))
    return ret

def set_grid(input):
    ret = False
    for i in range(9):
        for j in range(9):
            if(input[i,j] == 0):
                set1 = set(input[i,:])
                set2 = set(input[:,j])
                set3 = set(input[3*(i//3):3*(i//3)+2,3*(j//3):3*(j//3)+2].ravel())
                options = [x for x in range(1,10) if x not in (set1 | set2 | set3)]
                if (len(options)==0):
                    print("dead:", i,j)
                    return False
                grid[(i,j)] = options if len(options) > 1 else options[0]
                if len(options) == 1 :
                    set_cell(i, j, options[0])
                    ret = True
    return ret                        
    
def set_cell(i, j, v):
    if input[i, j] == 0 and v in range(1,10):
        input[i, j] = v 
        grid[(i, j)] = v
    

assert(validate_input(input))
while set_grid(input): assert(validate_input(input))

set_cell(8, 1, 8)
while set_grid(input): assert(validate_input(input))
