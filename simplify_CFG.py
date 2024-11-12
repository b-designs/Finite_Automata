
# Test cases
# Program only accounts for test cases and does not solve any test_case
test_case_1 = ["SA|B", "AL", "BABb|b"]
test_case_2 = ["Sa|aA|B|C", "AaB|L", "CcCD", "Dddd|Cd"]

# Function to find lambda in a string. Once lambda is found, 
# the staring char in string will be stored.
# It will be referenced later to further adjustments out-side of the string.
# The starting character is the variable that can produce the following
# characters in the string. Let this variable be called production.

def remove_lambda(test_case):
    production = ""
    
    # Finds lambda
    for str in test_case:
        for i in range(len(str)):
            if str[i] == "L":
                production = str[0]
                print("\nProduction Variable containing lambda: " + production + "\n")
                break
    
    # Cases to remove lambda
    if not production:
        print("Lambda does not exist")
        

        
    
def menu():
    while True:
        print("Choose a test case to run:")
        print("TEST CASE 1: S->A|B, A->L, B->ABb|b")
        print("\nTEST CASE 1: \nS->A|B \nA->L \nB->ABb|b")
        print("\nTEST CASE 2: \nS->a|aA|B|C \nA->aB|L \nB->Aa \nC->cCD \nD->ddd|Cd")        
        
        choice = input("\nEnter 1 or 2: ")

        try:
            choice = int(choice)
            if choice == 1:
                print("\n\tTEST CASE 1:")
                print("----------------------------")
                print("S->A|B \nA->L \nB->ABb|b")
                remove_lambda(test_case_1)
                break
            elif choice == 2:
                print("\n\tTEST CASE 2:")
                print("----------------------------")
                print("S->a|aA|B|C \nA->aB|L \nB->Aa \nC->cCD \nD->ddd|Cd")
                remove_lambda(test_case_2)
                break
            else:
                print("Invalid choice. Please enter 1 or 2")
        except ValueError:
            print("Invalid input. Enter 1 or 2")

def driver():
    menu()