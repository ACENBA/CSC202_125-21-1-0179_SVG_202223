from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="Image/card_front.jpg")  # Make sure to provide the correct path
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))  # Correct the font name typo ("Ariel" to "Arial")
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))  # Correct the font name typo ("Ariel" to "Arial")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Fix the config argument to set the background color
canvas.grid(row=0, column=0)

window.mainloop()
