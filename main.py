import tkinter as Tk
import random


class Card_GUI:
    def __init__(self):
        # Common format for all buttons
        button_font = ("Arial", 12, "bold")
        button_width = 12

        # Set up GUI frame
        self.temp_frame = Tk.Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Tk.Label(
            self.temp_frame,
            text="Recycling Card Game",
            font=("Arial", 16, "bold")
        )
        self.temp_heading.grid(row=0, column=0, columnspan=2, pady=10, sticky="W")

        self.points = 0  # Initialize points

        self.points_label = Tk.Label(
            self.temp_frame,
            text="Points: 0",
            font=("Arial", 12, "bold")
        )
        self.points_label.grid(row=0, column=1, pady=10, sticky="E")

        card_frame = Tk.Frame(self.temp_frame)
        card_frame.grid(row=1, column=0, padx=10, pady=10)

        self.card_labels = []  # Store card labels in a list
        self.material_labels = []  # Store material labels in a list

        # Recycling button
        recycle_button = Tk.Button(
            self.temp_frame,
            text="Recycle",
            command=self.recycle,
            font=button_font,
            width=button_width
        )
        recycle_button.grid(row=2, column=0, pady=10)

        # Rarity buttons
        rarities = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
        rarity_buttons_frame = Tk.Frame(self.temp_frame)
        rarity_buttons_frame.grid(row=2, column=1)

        for i, rarity in enumerate(rarities):
            rarity_button = Tk.Button(
                rarity_buttons_frame,
                text=rarity,
                command=lambda rarity=rarity: self.convert_materials(rarity),
                font=button_font,
                width=button_width
            )
            rarity_button.grid(row=0, column=i, padx=5, pady=5)

        self.generate_cards(card_frame)  # Generate initial set of cards

    #Display cards on screen
    def generate_cards(self, frame):
        card_deck = []
        for suit in ["clubs", "diamonds", "hearts", "spades"]:
            for rank in range(1, 14):
                card_deck.append(f"{rank} of {suit}")
        random.shuffle(card_deck)

        self.card_pile = []
        for i in range(7):
            self.card_pile.append(card_deck.pop())

        self.card_labels = []  # Clear the existing card labels

        for i in range(7):
            card_label = Tk.Label(frame, text=self.card_pile[i], font=("Arial", 12))
            card_label.grid(row=i, column=0, pady=5)
            self.card_labels.append(card_label)  # Add card label to the list

    #Display materials on screen
    def generate_material_labels(self, frame):
        materials = []

        for i in range(len(self.card_pile)):
            card = self.card_pile[i]
            rank, suit = card.split(" of ")

            #rarities for the materials
            if int(rank) < 1:
                rarity = "Legendary"
            elif int(rank) < 2:
                rarity = "Epic"
            elif int(rank) < 5:
                rarity = "Rare"
            elif int(rank) < 8:
                rarity = "Uncommon"
            else:
                rarity = "Common"

            materials.append(f"{rarity} {suit}")

        self.material_labels = []  # Clear the existing material labels

        for i, material in enumerate(materials):
            material_label = Tk.Label(frame, text=material, font=("Arial", 12))
            material_label.grid(row=i, column=0, pady=5)
            self.material_labels.append(material_label)  # Add material label to the list

    #Recycles cards when recycle button pressed
    def recycle(self):
        random.shuffle(self.card_pile)  # Shuffle the card pile

        for material_label in self.material_labels:
            material_label.destroy()

        material_frame = Tk.Frame(self.temp_frame)
        material_frame.grid(row=1, column=1, padx=10, pady=10)

        self.generate_material_labels(material_frame)  # Generate new material labels

    #Converts materials into points
    def convert_materials(self, rarity):
        found_material = False

        for material_label in self.material_labels:
            material_text = material_label.cget("text")

            #Add points based on rarities
            if "Legendary" == rarity in material_text:
                found_material = True
                self.material_labels.remove(material_label)
                material_label.destroy()
                self.add_points(50)
                break

            elif "Epic" == rarity in material_text:
                found_material = True
                self.material_labels.remove(material_label)
                material_label.destroy()
                self.add_points(25)
                break

            elif "Rare" == rarity in material_text:
                found_material = True
                self.material_labels.remove(material_label)
                material_label.destroy()
                self.add_points(5)
                break

            elif "Uncommon" == rarity in material_text:
                found_material = True
                self.material_labels.remove(material_label)
                material_label.destroy()
                self.add_points(2)
                break

            elif "Common" == rarity in material_text:
              found_material = True
              self.material_labels.remove(material_label)
              material_label.destroy()
              self.add_points(1)
              break

        if not found_material:
            self.display_message("Insufficient resources.")

    def add_points(self, points):
        self.points += points
        self.points_label.config(text=f"Points: {self.points}")

    def display_message(self, message):
        message_label = Tk.Label(
            self.temp_frame,
            text=message,
            font=("Arial", 12),
            fg="red"
        )
        message_label.grid(row=3, column=0, columnspan=2, pady=10)


# Main routine
if __name__ == "__main__":
    root = Tk.Tk()
    root.title("Recycling Card Game")
    root.geometry("600x400")
    Card_GUI()
    root.mainloop()