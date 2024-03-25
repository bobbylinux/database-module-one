from dependencies import dependencies_preservation
from keys import keys

if __name__ == '__main__':
    print("Welcome to the database module one tool utility.\n")
    choice = input("select what you want to do:\n\n"
                   "0. Calc the keys of a schema\n"
                   "1. Calc a determinant closure\n"
                   "2. Determinate if a decomposition preservers dependencies\n"
                   "3. Determinate if a decomposition has a lossless join\n"
                   "4. Calc a valid decomposition\n\n"
                   "Enter your input (ex. 0 or 1 or 2 or 3 or 4): ")
    if choice == '0':
        keys()
    elif choice == '1':
        print("function not yet implemented")
    elif choice == '2':
        dependencies_preservation()
    elif choice == '3':
        print("function not yet implemented")
    elif choice == '4':
        print("function not yet implemented")
    else:
        print("input not valid")
