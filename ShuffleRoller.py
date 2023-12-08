# Importing the required libraries
import random
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variable to store the shuffled deck and the current index
shuffled_deck = []
current_index = 0
last_20=[]
# Global variable to store the count of each number drawn
number_counts = [0] * 20  # A list of 20 zeros

# Create the main application window and set its title
window = tk.Tk()
window.title("Shuffle Deck Die Roller")
window.geometry("620x300")  # Resize the window

# Matplotlib Figure and Canvas Setup
fig, ax = plt.subplots(figsize=(5, 3))  # This will hold our plot
histogram_canvas = FigureCanvasTkAgg(fig, master=window)  # This creates the Tkinter canvas containing the Matplotlib figure
histogram_canvas_widget = histogram_canvas.get_tk_widget()  # This gets the Tkinter widget that will display the Matplotlib figure
histogram_canvas_widget.pack()  # Pack the Matplotlib canvas onto the Tkinter window

# Function to update the histogram
def update_histogram():
    ax.clear()  # Clear the previous histogram
    ax.bar(range(1, 21), number_counts, tick_label=range(1, 21))
    # Create a bar chart with numbers 1 to 20 on the x-axis and their corresponding counts on the y-axis
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Drawn Numbers')
    histogram_canvas.draw_idle()  # Redraw the histogram canvas

# Insert this function just before defining the `shuffle_deck` function


# Function to shuffle a deck of numbers from 1 to 20
def shuffle_deck():
    global shuffled_deck
    global current_index
    global last_20
    shuffled_deck = list(range(1, 21))
    random.shuffle(shuffled_deck)
    current_index = 0
    deck_label.config(text="Deck has been shuffled.")
    update_histogram() 

# Function to draw the next number from the shuffled deck
def draw_number():
    global shuffled_deck
    global current_index
    if current_index >= len(shuffled_deck):
        shuffle_deck()  # Refill the deck if empty
    drawn_number = shuffled_deck[current_index]
    number_counts[drawn_number - 1] += 1
    update_histogram() 
    last_20.append(drawn_number)
    if len(last_20) > 20:
        last_20.pop(0)
        
    current_index += 1
    
    existing_text = drawn_numbers_label.cget("text")
    
    drawn_numbers_label.config(text=last_20)
    

# Create buttons to shuffle the deck and draw a number
shuffle_button = tk.Button(window, text="Shuffle Deck", command=shuffle_deck)
shuffle_button.pack(pady=20)

draw_button = tk.Button(window, text="Draw Number", command=draw_number)
draw_button.pack(pady=20)

# Create labels to display the deck status and drawn numbers
deck_label = tk.Label(window, text="Deck is empty.")
deck_label.pack(pady=10)

drawn_numbers_label = tk.Label(window, text="Drawn Numbers:")
drawn_numbers_label.pack(pady=10)

# Start the main GUI loop
window.mainloop()
