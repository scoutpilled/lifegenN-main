class Clan:
    def __init__(self, name):
        self.name = name
        self.cats = []  # Initialize the cats attribute as an empty list

    def add_cat(self, cat):
        """
        Add a cat to the clan.
        """
        self.cats.append(cat)

    def remove_cat(self, cat_id):
        """
        Remove a cat from the clan by its ID.
        """
        self.cats = [cat for cat in self.cats if cat.id != cat_id]

    # ...existing code...
