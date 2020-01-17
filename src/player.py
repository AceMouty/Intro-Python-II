# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room: Room):
        self.name = name
        self. current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f"Player({self.name}, {self.current_room})"

    def travel(self, direction):
        # Player should be able to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("You cannot move in that direction.")

    def drop_item(self, item):
        # print("Dropped item")
        for player_item in self.inventory:
            if player_item.name == item:
                self.inventory.remove(player_item)
                self.current_room.items.append(player_item)
                player_item.dropped_item()

    def get_item(self, item):
        for roomitem in self.current_room.items:
            if roomitem.name == item:
                self.current_room.items.remove(roomitem)
                self.inventory.append(roomitem)
                roomitem.taken_item()
        print("Items in inventory")
        for player_item in self.inventory:
            print(f"{player_item}")

    def get_inventory(self):
        if len(self.inventory) > 0:
            print("Currently in your inventory")
            for item in self.inventory:
                print(f"{item.name}")
        else:
            print("\n\n\n\n\nYou do not currently have items in your inventory\n\n")
