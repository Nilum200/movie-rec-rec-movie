# The node class contains the name of the film, genre tags for the film, and a link to the next node.

class Node:
    def __init__(self, film, tag):
        # film should be the film's title. The "tag" is used as a search filter.
        self.film = film
        self.tag = tag
        # next node creates the daisy chain effect within linked lists so we don't lose old nodes.
        self.next_node = None

    # function fetches film title.
    def get_film(self):
        return self.film

    # function fetches film's genre tag.
    def get_tag(self):
        return self.tag

    # function SETS a film's tags, in case they require updating for some reason.
    # might later change this to handle multiple tags within lists. Not sure yet--basics getting done first.
    def set_tag(self, tag):
        self.tag = tag

    # Used in linked list search functions.
    def get_next_node(self):
        return self.next_node

    # Used to set one node as linked to another, creating a linear chain of nodes.
    def set_next_node(self, next_node):
        self.next_node = next_node
