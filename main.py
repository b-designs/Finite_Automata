
# Main menu for program

import nfa_to_dfa
import simplify_CFG

def menu():
    while True:
        print("Choose a program to run:")
        print("1. NFA to DFA")
        print("2. Simplify Context-Free-Grammars")
        
        choice = input("Enter 1 or 2: ")
        
        try:
            choice = int(choice)
            if choice == 1:
                print("\n\t\tPROGRAM: NFA to DFA")
                print("-------------------------------------------------")
                nfa_to_dfa.driver()
                break
            elif choice == 2:
                print("\n\tProgram: Simplify Context-Free Grammars")
                print("---------------------------------------------------------")
                simplify_CFG.driver()
                break
            else:
                print("Invalid choice. Please enter 1 or 2")
        except ValueError:
            print("Invalid input. Enter 1 or 2")
            
if __name__ == '__main__':
    menu()
    
    