# items in the game


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}\n\n"

    def taken_item(self):
        print("{} has been picked up".format(self.name))

    def dropped_item(self):
        print("{} has been dropped".format(self.name))
