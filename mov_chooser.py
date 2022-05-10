# Here is the class/function that handles grabbing tags from the user.
# Those tags are then fed into mov_films to return a list of films which fit the user's tag preferences.

class Chooser:
    @staticmethod
    # Sci-Fi = 1, Fantasy = 2, Horror = 3, Comedy = 4, Superheroes = 5.
    def choose():
        valid_choices = ["1", "2", "3", "4", "5"]
        choice = None
        count = 0
        while choice not in valid_choices:
            count += 1
            choice = input("Choose: ")
            if count == 2:
                print("A number between 1 to 5 is valid. Try again.\n")
            elif count == 5:
                print("1, not one.\n")
            elif count == 10:
                print("You'll figure it out, I'm sure!\n")
            elif count == 9000:
                print("Very funny. Won't you get bored at some point?\n")
        # choice will loop until a valid choice is presented.
        return int(choice)
        # convert choice into an integer, which is then returned for use in the linked_list film search function.
