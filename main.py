# Basic functions now work.
# Now we need to design something that accepts user input and uses it to return movies.

from mov_films import movies_list
from mov_chooser import Chooser

print("The movie recommender recommends movies!\n")
print("The movie recommender which recommends movies has a number of films to search for, arranged by genre!")
genre = Chooser.choose()
# Calls chooser function from mov_chooser to filter a genre the user wants to search.

film_list = movies_list.search_tag(genre)
# Produce a list of films based on user search conditions.

for index in film_list:
    print(index)
# print list of recommended films below.
