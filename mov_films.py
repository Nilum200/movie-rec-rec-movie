# Here is where films are stored so it doesn't clutter main.py.
from mov_linked_list import LinkedList

movies_list = LinkedList()
movies_list.add_film("Alien", "Sci-Fi")
movies_list.add_film("Star Wars: A New Hope", "Sci-Fi")
movies_list.add_film("The Matrix", "Sci-Fi")
movies_list.add_film("GATTACA", "Sci-Fi")
movies_list.add_film("Contact", "Sci-Fi")
movies_list.add_film("Lord of the Rings", "Fantasy")
movies_list.add_film("Labyrinth", "Fantasy")
movies_list.add_film("Dungeons & Dragons", "Fantasy")
movies_list.add_film("Pirates of the Caribbean", "Fantasy")
movies_list.add_film("Texas Chainsaw Massacre", "Horror")
movies_list.add_film("Get Out", "Horror")
movies_list.add_film("Pitch Black", "Horror")
movies_list.add_film("Parasite", "Horror")
movies_list.add_film("The Nightmare Before Christmas", "Comedy")
movies_list.add_film("Ghostbusters", "Comedy")
movies_list.add_film("Monty Python's Meaning of Life", "Comedy")
# Minor bug: Monty Python's Meaning of Life has an apostrophe in it which makes it appear weird in list.
movies_list.add_film("Airplane", "Comedy")
movies_list.add_film("Spaceballs", "Comedy")
movies_list.add_film("Blade", "Superheroes")
movies_list.add_film("The Avengers", "Superheroes")
movies_list.add_film("Superman", "Superheroes")