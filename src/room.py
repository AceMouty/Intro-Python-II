# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    # class vars

    def __init__(self, name, description, items=[]):
        # Name, description
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        display_string = ""
        display_string += f"----------------"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"{self.get_exits_string()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def get_items(self):
        if len(self.items) > 0:
            print(f"Items in the room: ")
            for item in self.items:
                print(item)
        else:
            print("There are no items in the room")

    def get_exits_string(self):
        return f"Moves: {', '.join(self.get_exits())}"

    def add_item(self, item):
        self.items.append(item)
