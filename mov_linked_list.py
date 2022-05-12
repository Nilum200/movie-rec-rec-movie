# Linked list contains all nodes in order they were inserted.
# A search function should also be added to allow one to find and collect all instances of an item with a specific tag.
# eg: Search for all films with the "sci-fi" tag and then return them as a new list.
from mov_node import Node
# Keep nodes in their own file to keep things easy reading.


class LinkedList:
    def __init__(self):
        self.head = None
        # Important! Sets head of list! Do not lose this!! For the love of god!!!

    def add_film(self, title, tag):
        new_node = Node(title, tag)
        # Establishes a node with film title & film tags.
        if self.head is None:
            self.head = new_node
            # List is empty, so just set new node to be head node.
        else:
            old_node = self.head
            # Redundant step that makes me feel safer until I'm ready to refactor.
            new_node.set_next_node(old_node)
            # Set new node's next node to old node, so we don't lose old node.
            self.head = new_node
            # Replace old node with new node, now that new_node points to old_node.

    def search_tag(self, search_list):
        return_list = []
        # This is an empty list that will contain all relevant films.
        current_node = self.head
        if current_node is None:
            return "This list has no movies to search through."
            # If the movie list is empty, then this informs me of this. The user should, ideally, never see this.
        if len(search_list) < 1:
            return "Search list is empty. Movie recommender cannot recommend movies on an empty list!"
            # If the search list given from mov_chooser is empty, then it would be a waste of time to do anything.
        while current_node:
            for index in current_node.get_tag():
                # Search through node's tags...
                if index in search_list:
                    return_list.append(current_node.get_film())
                    # If node tag is in user search list, add node.
                    break
                    # Get out of this loop so we don't add the same film twice.
            current_node = current_node.get_next_node()
            # this ensures that the while loop will terminate when it runs out of valid nodes.
        if len(return_list) < 1:
            return "No films with that tag were found."
            # This should never happen, but hey, it's here in case it does.
        else:
            return return_list
            # Return the list of films recommended to the user.
