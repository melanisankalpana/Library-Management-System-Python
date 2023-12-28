from C_for_Books import Codeforbooks
from lecturecdfunction import LectureCDFunction

book_func = Codeforbooks()
lecture_cd_func = LectureCDFunction()
eternal_dvd_func = Codeforbooks()   # change it later with your class
magazine_func = Codeforbooks()   # change it later with your class


def submenu(function_name, selected_resource):
    selected_operation = 1
    while selected_operation > 0:
        print("Please select the operation menu")
        print("--------------------------------")
        print(f"1 - Add a {selected_resource}")
        print(f"2 - Remove a {selected_resource}")
        print(f"3 - Display Available {selected_resource}")
        print(f"4 - Display Unavailable {selected_resource}")
        print(f"5 - Lend {selected_resource}")
        print(f"6 - Receive {selected_resource}")
        print("7 - Back to Main Menu")
        print("0 - Quit")
        selected_operation = int(input("Please type the number of your choice: ").strip())

        if selected_operation == 1:
            function_name.add()
        elif selected_operation == 2:
            function_name.remove()
        elif selected_operation == 3:
            function_name.display_available()
        elif selected_operation == 4:
            function_name.display_unavailable()
        elif selected_operation == 5:
            function_name.lend()
        elif selected_operation == 6:
            function_name.receive()
        elif selected_operation == 7:
            mainmenu()  # back to main menu
        else:
            print("Invalid selection")

        if 1 <= selected_operation <= 7:
            input("Press any key to continue...")


def mainmenu():
    print("Main Menu")
    print("---------")
    print("1 - Books")
    print("2 - Magazine")
    print("3 - Exeternal DVD")
    print("4 - Lecture CD")
    print("0 - Quit")


print("WELCOME TO OUSL LIBRARY SYSTEM")
print("==============================")
selected_resource = 1
while selected_resource > 0:
    mainmenu()
    try:
        selected_resource = int(input("Please select your option: "))
    except ValueError:
        print("Invalid Entry")
        mainmenu()

    if selected_resource == 0:
        print("Thank you for using library system.")
        quit()
    elif selected_resource == 1:
        function_name = book_func
        submenu(function_name, "Book")
        break
    elif selected_resource == 2:
        function_name = magazine_func
        submenu(function_name, "Magazine")
        break
    elif selected_resource == 3:
        function_name = eternal_dvd_func
        submenu(function_name, "External DVD")
        break
    elif selected_resource == 4:
        function_name = lecture_cd_func
        submenu(function_name, "Lecture CD")
        break



