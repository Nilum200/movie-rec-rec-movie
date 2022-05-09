# Going to set up the design first...
# We'll use this space to test nodes and linked lists, so import both.
# We'll ultimately refactor once the basic concept works.
from mov_node import Node
# from mov_linked_list import linked_list

# Testing node code, to make sure I got it right.
alien = Node("Alien", 1)
aliens = Node("Aliens", 2)
aliens_3 = Node("Alien 3", 3)
aliens_4 = Node("Alien 4", 4)

alien.set_next_node(aliens)
aliens.set_next_node(aliens_3)
aliens_3.set_next_node(aliens_4)

current_node = alien
while current_node:
    print(current_node.get_film())
    current_node = current_node.get_next_node()

# Success!
