
inputs = ["d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2}",
          "d(q0,a)={q0,q1},d(q1,b)={q1,q2},d(q2,a)={q2},d(q0,lambda)"
          ]

# Prints all inputs
def print_input(str):
    print("~ Inputs ~")
    for index in range(0, len(str)):
        if str[index-1] == "}" and str[index] == ",":
            print(str[index])
        else:
            print(str[index], end="")



print_input(inputs[1])
        