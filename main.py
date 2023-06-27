from tkinter import *


class Card_GUI:
  def __init__(self):
    # common format for all buttons
    # Arial size 14 bold with white text
    button_font = ("Arial", "14", "bold")
    button_fg = "#FFFFFF"

    # set up GUI frame
    self.temp_frame = Tk.Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.temp_heading = Tk.Label(self.temp_frame,
                                text="Recycling Card Game",
                                font=("Arial", "16", "bold"))
    self.temp_heading.grid(row=0, columnspan=2)

    card_frame = Tk.Frame(self.temp_frame)
    card_frame.grid(row=1, column=0, padx=10, pady=10)

    material_frame = Tk.Frame(self.temp_frame)
    material_frame.grid(row=1, column=0, padx=10, pady=10)

    self.card_labels = []  # store card labels in a list
    self.materials_labels = []  # store material labels in a list

    recycling_bin = Tk.Button(self.temp_frame, text="Recycle", command=self.recycle)
    recycleing_bin.grid(row=2, columnspan=2, pady=10)

    self.generate_cards(card_frame)
    self.generate_material_labels(material_frame)