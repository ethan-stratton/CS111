class Link:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"({self.val}) --> {self.next}"


Link(5, None) # first value 5, next value None. It's like a circle with a 5 in it pointing to another circle with nothing in it.

link = Link(5, (Link(3, (Link(2, (Link(7, None))))))) # first value 5 points to 3 which points to None

print(link)


        