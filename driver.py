
given_inputs = ["d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2}",
          "d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2},d(q0,lambda)={q2}"]

states = []
inputs = []

demo_matrix = [["q0,q1", "q0,q1", "q0,q1"],
               ["q0,q1", "q0,q1", "q0,q1"],
               ["q0,q1", "q0,q1", "q0,q1"]]

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
        
def check_inputs_for_states():
    # checks to see if other states should be included
    pass
        
            
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
            
print_given_input(given_inputs[1])
gather_states(given_inputs[1])
gather_inputs(given_inputs[1])
print_matrix(states, inputs, demo_matrix)

