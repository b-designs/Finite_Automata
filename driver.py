
inputs = ["d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2}",
          "d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2},d(q0,lambda)"]

states = []

# Prints all inputs
def print_input(str):
    print("~ Inputs ~")
    for index in range(0, len(str)):
        if str[index-1] == "}" and str[index] == ",":
            print(str[index])
        else:
            print(str[index], end="")
            
# Adds states from a string and stores them in the states list     
def gather_states(str):
    global states
    for index in range(0, len(str)):
        if str[index-1] == "q":
            states.append("q" + str[index])
    
    # Removes an repeats
    dummyvar = set(states)
    states = dummyvar
    
    # Sorts the states
    dummyvar = sorted(states)
    states = dummyvar
            
    # Prints the states
    print("\n\n~ States gathered: ~")
    print(states)
    
            
print_input(inputs[1])
gather_states(inputs[1])        