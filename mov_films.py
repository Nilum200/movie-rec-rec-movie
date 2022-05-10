# Here is where films are stored so it doesn't clutter main.py.
from mov_linked_list import LinkedList

# Sci-Fi = 1; Fantasy = 2; Horror = 3; Comedy = 4; Superheroes = 5.
movies_list = LinkedList()
movies_list.add_film("Alien", 1)
movies_list.add_film("Star Wars: A New Hope", 1)
movies_list.add_film("The Matrix", 1)
movies_list.add_film("GATTACA", 1)
movies_list.add_film("Contact", 1)
movies_list.add_film("Lord of the Rings", 2)
movies_list.add_film("Labyrinth", 2)
movies_list.add_film("Dungeons & Dragons", 2)
movies_list.add_film("Pirates of the Caribbean", 2)
movies_list.add_film("Texas Chainsaw Massacre", 3)
movies_list.add_film("Get Out", 3)
movies_list.add_film("Pitch Black", 3)
movies_list.add_film("Parasite", 3)
movies_list.add_film("The Nightmare Before Christmas", 4)
movies_list.add_film("Ghostbusters", 4)
movies_list.add_film("Monty Python's Meaning of Life", 4)
# Minor bug: Monty Python's Meaning of Life has an apostrophe in it which makes it appear weird in list.
movies_list.add_film("Airplane", 4)
movies_list.add_film("Spaceballs", 4)
movies_list.add_film("Blade", 5)
movies_list.add_film("The Avengers", 5)
movies_list.add_film("Superman", 5)
