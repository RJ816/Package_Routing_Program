# Used to store graph vertex objects
class Vertex:

    # constructor
    def __init__(self, index, label):
        self.index = index
        self.label = label

    # Override string method.
    def __str__(self):
        return f"index: {self.index}\n" \
               f"label: {self.label}"
