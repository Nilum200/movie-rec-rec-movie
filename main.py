# Basic functions now work.
# Now we need to design something that accepts user input and uses it to return movies.

from mov_films import movies_list
from mov_chooser import Chooser

print("The movie recommender recommends movies!\n")
print("The movie recommender which recommends movies has the following genres to choose from: ")
print("1) Sci-Fi 2) Fantasy 3) Horror 4) Comedy 5) Superheroes")
print("Type the number associated to the genre you'd like to be recommended.\n")
genre = Chooser.choose()
# Calls chooser function from mov_chooser to filter a genre the user wants to search.
print(movies_list.search_tag(genre))
# Returns a list of films which meets the user's search qualifications.
