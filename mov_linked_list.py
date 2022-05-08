# Linked list contains all nodes in order they were inserted.
# A search function should also be added to allow one to find and collect all instances of an item with a specific tag.
# eg: Search for all films with the "sci-fi" tag and then return them as a new list.

# from mov_node import node <- Keep nodes in their own file to keep things easy reading.
# Definite improvement from my last project...

# class linked_list
#   def __init__(self):
#       self.head = None <- Important! Sets head of list! Do not lose this!! For the love of god!!!

#   def add_film(self, title, tag):
#       new_node = node(title, tag) <- Establishes a node with film title & film tags.
#       if self.head is None...
#           self.head = new_node <- List is empty, so just set new node to be head node.
#       else...
#           old_node = self.head_node <- Redundant step that makes me feel safer until I'm ready to refactor.
#           new_node.set_next_node(old_node) <- Set new node's next node to old node, so we don't lose old node.
#           self.head = new_node <- Replace old node with new node, now that new_node points to old_node.

#   def search_tag(self, tag):
#       return_list = [] <- This is an empty list that will contain all relevant films.
#       set current_node to self.head.
#       if current_node is None...
#           return a line saying the list is empty.
#       while current_node exists...
#           if current_node tag is equal to search tag...
#               append current_node's title to return list.
#           current_node = get the current node's next node.
#       if return_list is empty...
#           return that no films with that tag were found.
#       else...
#           return return_list
