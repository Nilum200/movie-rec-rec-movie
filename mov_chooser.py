# Here is the class/function that handles grabbing tags from the user.
# Those tags are then fed into mov_films to return a list of films which fit the user's tag preferences.

class Chooser:
    @staticmethod
    # Sci-Fi = 1, Fantasy = 2, Horror = 3, Comedy = 4, Superheroes = 5, Drama = 6.
    def choose():
        valid_choices = [1, 2, 3, 4, 5, 6]
        choices = []
        exit_condition = False
        # Always have a terminator for infinite loops, lest yee be lost in math wilderness...
        while exit_condition is False:
            print("Current user search list: {0}".format(choices))
            print("1) Sci-Fi 2) Fantasy 3) Horror 4) Comedy 5) Superheroes 6) Drama\n")
            print("Enter '0' to stop selecting genres and initiate the search at any time!\n")
            print("Type a number to add or remove it from your search list...")
            choice = input("Input: ")
            int_choice = int(choice)
            # Convert choice to an integer here and clearly mark it with its own variable so I don't forget.
            if int_choice in choices:
                print("Removing {0}".format(choice))
                choices.remove(int_choice)
                # If the choice is already in choices, remove it.
            elif int_choice in valid_choices:
                print("Adding {0}".format(choice))
                choices.append(int_choice)
                # if the choice is not in choices and is a valid choice, add it.
            elif choice == "0":
                exit_condition = True
                # allow user to terminate loop when they see fit.
            else:
                print("Invalid choice--type one number, like 1 for sci-fi, or 3 for horror.\n\n")
                # if none of the above are valid, the user didn't present a valid choice.
        return choices
        # return the list, even if it's empty. The search function in linked list will take care of things from here.
