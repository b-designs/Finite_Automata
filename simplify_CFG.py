
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DESCRIPTION: SIMPLY CONTEXT FREE GRAMMARS

This program demonstrates how to simplify Context Free Grammars 
with the given test cases. There are two test cases.
After Simplification, a prompt between production conversion to
Chomsky Normal Form and Greibach Normal Form is given 
for the desired form.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Test cases
# Element 0 of each string is the is the production variable.
# After element 0 is the production
# e.g Test Case 1
# test_case_1[0] = "SAB"       = S -> A|B,
# test_case_1[1] = "AL"        = A -> L,       
# test_case_1[2] = "BABb|b"    = B -> ABb|b    

test_case_1 = ["SA|B", "AL", "BABb|b"]
test_case_2 = ["Sa|aA|B|C", "AaB|L", "CcCD", "Dddd|Cd"]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    Simplification Functions               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Helper function to find nullable variables
# Once they are found, it returns an array of the nullable variables
def find_nullable_variables(test_case, prod_var):
    null_vars = []
    for str in test_case:
        if prod_var in str and prod_var != str[0]:
            null_vars.append(str[0])
    return null_vars   

# Function to find lambda in a string. Once lambda is found, 
# the staring char in string will be stored.
# It will be referenced later to further adjustments out-side of the string.
# The starting character is the variable that can produce the following
# characters in the string. Let this variable be called production.

def remove_lambda_productions(test_case):
    production = ""
    lambda_index = -1
    lambda_str = ""
    
    # Finds lambda
    for str in test_case:
        for i in range(len(str)):
            if str[i] == "L":
                production = str[0]
                lambda_index = i
                lambda_str = str
                print("\nProduction Variable containing lambda: " + production)
                break
    
    null_vars = find_nullable_variables(test_case, production)
    print("Nullable variables:")
    print(null_vars)
    
    # Cases to remove lambda
    if not production:
        print("Lambda does not exist")
    elif lambda_str[lambda_index] == "L" and lambda_str[lambda_index-1] != "|" and lambda_index+1 == len(lambda_str):
        print("No bars on left or right")
        
                    
            
    elif (lambda_str[lambda_index] == "L" and lambda_str[lambda_index-1] == "|"):
        print("1 bar on left")
    else:
        print("ERROR")
        
def remove_unit_productions(test_case):
    print("")
    
def remove_useless_productions(test_case):
    print("")
    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    Conversion Functions               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
def convert_to_chomsky_normal_form(test_case):
    print("")

def convert_to_greibach_normal_form(test_case):
    print("")

# Utilizes each simplification function then uses a conversion function
def simplify_convert(test_case):
    remove_lambda_productions(test_case)
    # remove_useless_productions(test_case)
    # remove_unit_productions(test_case)
    # choose_a_form(test_case)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            Menus               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# A menu to choose between Chomsky and Greibach Normal Forms
def choose_a_form(test_case):
    while True:
        print("Choose a form:")
        print("1. Chomsky Normal Form")
        print("2. Greibach Normal Form")
        
        choice = input("\nEnter 1 or 2")
        
        try:
            choice = int(choice)
            if choice == 1:
                print("\n\tConversion to Chomsky Normal Form:")
                print("-----------------------------------------------------")
                convert_to_chomsky_normal_form(test_case)
                break
            elif choice == 2:
                print("\nConversion to Greibach Normal Form")
                print("-----------------------------------------------------")
                convert_to_greibach_normal_form(test_case)
                break
        except ValueError:
            print("Invalid input. Enter 1 or 2")       

# STARTING MENU
def menu():
    while True:
        print("Choose a test case to run:")
        print("\nTEST CASE 1: \nS->A|B \nA->L \nB->ABb|b")
        print("\nTEST CASE 2: \nS->a|aA|B|C \nA->aB|L \nB->Aa \nC->cCD \nD->ddd|Cd")        
        
        choice = input("\nEnter 1 or 2: ")

        try:
            choice = int(choice)
            if choice == 1:
                print("\n\tTEST CASE 1:")
                print("----------------------------")
                print("S->A|B \nA->L \nB->ABb|b")
                simplify_convert(test_case_1)
                break
            elif choice == 2:
                print("\n\tTEST CASE 2:")
                print("----------------------------")
                print("S->a|aA|B|C \nA->aB|L \nB->Aa \nC->cCD \nD->ddd|Cd")
                simplify_convert(test_case_2)
                break
            else:
                print("Invalid choice. Please enter 1 or 2")
        except ValueError:
            print("Invalid input. Enter 1 or 2")
            
            
            

def driver():
    menu()
    
# if __name__ == '__main__':
#     menu()