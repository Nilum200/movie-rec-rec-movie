# Going to set up the design first...
# We'll use this space to test nodes and linked lists, so import both.
# We'll ultimately refactor once the basic concept works.
from mov_node import Node
from mov_linked_list import LinkedList

test_list = LinkedList()
test_list.add_film("Alien", "Sci-Fi")
test_list.add_film("Alien 2", "Sci-Fi")
test_list.add_film("Alien 3", "Sci-Fi")

print(test_list.search_tag("Sci-Fi"))
