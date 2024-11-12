
test_case_1 = ["SA|B", "AL", "BABb|b"]
test_case_2 = ["Sa|aA|B|C", "AaB|L", "CcCD", "Dddd|Cd"]
    
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
                break
            elif choice == 2:
                print("\n\tTEST CASE 2:")
                print("----------------------------")
                print("S->a|aA|B|C \nA->aB|L \nB->Aa \nC->cCD \nD->ddd|Cd")
                break
            else:
                print("Invalid choice. Please enter 1 or 2")
        except ValueError:
            print("Invalid input. Enter 1 or 2")

def driver():
    menu()