import read_functions


def what_to_do():
    while True:
        check = (input("\nAll students:s\tMainMenu:menu\tExit:exit\n")).upper()
        if check == "S":
            print(*read_functions.all_students(), sep=" ,")
        if check == "EXIT":
            exit()
        if check == "MENU":
            break
