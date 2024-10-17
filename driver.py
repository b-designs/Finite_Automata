
given_inputs = ["d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2}",
                "d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2},d(q0,lambda)={q2}"]

states = []
inputs = []


demo_matrix = [["q0,q1", "q0,q1", "q0,q1"],
               ["q0,q1", "q0,q1", "q0,q1"],
               ["q0,q1", "q0,q1", "q0,q1"]]

my_map = {}
symbol_positions = []

# Prints all inputs in the format of d()={}
def print_given_input(str):
    print("~ Given Inputs ~")
    for index in range(0, len(str)):
        if str[index] == "," and str[index-1] == "}":
            pass
        elif str[index] == "}":
            print("}")
        elif str[index] == "=":
            print(" = ", end="")
        else:
            print(str[index], end="")
            
def print_map():
    global my_map
    for key, value in my_map.items():
        print("Input: " + key, "\tOutput: " + value)

# Prints a matrix
# States will represent the rows
# Inputs will represent the states
def print_matrix(states, inputs, matrix):
    print("\n\t     MATRIX")
    print("- - - - - - - - - - - - - - - - -")
    
    # Prints the column labels
    for element in inputs:
        print("\t" + element, end=" ")
    print("")
    
    row = 0 # Keeps track of what row is going to be printed
    
    # Prints the row labels and element in each matrix cell
    for element in states:
        print(element, end="\t")
        
        for element in matrix[row]:
            print(element, end="\t")
        print("")
        
        row = row + 1
        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                        MAP SECTION               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Setup program and symbol positions
Checks strings for () and {}  
If pair is not found, ERROR will occur
"""
def find_parenthesis_and_curly_braces(str):
    global symbol_positions
    for index in range(0, len(str)):
        if str[index] == "(" or str[index] == ")" or str[index] == "{" or str[index] == "}":
            symbol_positions.append(index)
    if len(symbol_positions) % 2 != 0:
        print("ERROR")

"""
Gets string information between two positions
Returns the information in single string
"""        
def get_between_symbols(str, p_start, p_end):
    temp_str = ""
    for i in range(p_start+1, p_end):
        if str[i] != "," and str[i+1] == "l":
            temp_str = temp_str + "lambda"
            i = i + 6
        else:
            temp_str = temp_str + str[i]
    return temp_str


"""
Setup map 
- to have all keys be the left hand side of an "="
- to have all values be the right hand side of the corresponding "=" 
"""   
def set_up_map(str, map, positions):
    gathered_strings = []
    
    # Gathers all strings
    for i in range(0,len(positions), 2):
        gathered_strings.append(get_between_symbols(str, positions[i], positions[i+1]))
    
    # Setup for map using all gathered strings
    for i in range(0,len(gathered_strings),2):
        map.update({gathered_strings[i]:gathered_strings[i+1]})
    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                   STATES and INPUTS SECTION               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Adds states from a string and stores them in the states list  
# Inputs cannot be q or l as they will cause issues when gathering states 
def gather_states(str): 
    global states
    
    for index in range(0, len(str)):
        if str[index-1] == "q":
            states.append("q" + str[index])
        if str[index] == "t":
            states.append("trap")
    
    # Removes an repeats
    states = set(states)
    
    # Sorts the states
    states = sorted(states)
            
    # Prints the states gathered
    print("\n~ States gathered: ~")
    print(states)
    
def gather_inputs(str):
    global inputs
    
    for index in range(0, len(str)):
        if str[index] == ")":
            inputs.append(str[index-1])
        if str[index] == "l":
            inputs.append("lambda")
            
    inputs = set(inputs)
    
    # # Separate the non-normal inputs (lambda, trap) from normal inputs
    normal_inputs = [input for input in inputs if not input.startswith("l") and not input.startswith("t")]
    other_inputs = [input for input in inputs if input.startswith("l") or input.startswith("t")]
    
    # # Sorts the states
    normal_inputs.sort()
    other_inputs.sort()
    
    # Combine q states first, followed by other states
    inputs = normal_inputs + other_inputs
    
    print("\n~ Inputs gathered: ~")
    print(inputs)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            DRIVER            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if __name__ == '__main__':
    find_parenthesis_and_curly_braces(given_inputs[1])
    set_up_map(given_inputs[1], my_map, symbol_positions)
    print_map()

# print_given_input(given_inputs[1])
# gather_states(given_inputs[1])
# gather_inputs(given_inputs[1])
# print_matrix(states, inputs, demo_matrix)