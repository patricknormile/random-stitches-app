import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from create_random_stitches import random_stitch

class DirectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Direction App")
        
        # Current direction label
        self.direction_label = tk.Label(root, text="", font=("Helvetica", 76))
        self.direction_label.pack(pady=20)
        
        # Last 5 directions label
        self.history_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.history_label.pack(pady=10)

        self.counter_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.counter_label.pack(padx=100)
        
        # Button to generate a new direction
        self.button = tk.Button(root, text="Get Random Direction", command=self.show_random_direction, font=("Helvetica", 18))
        self.button.pack(pady=20)
        
        # List to store last 5 directions
        self.history = [" "*5]*5
        self.counter = 0
        self.y_axis = [0]

         # Create a figure and axis
        self.figure, self.axis = plt.subplots(figsize=(6, 4))
        self.axis.set_title('Counter vs Y-Axis')
        self.axis.set_xlabel('Counter')
        self.axis.set_ylabel('Y-Axis')
        
        # Add the plot to the window
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    
    def show_random_direction(self):
        # Generate random direction
        direction = random_stitch()
        self.counter += 1
        
        # Update current direction label
        self.direction_label.config(text=direction)
        
        # Update history label
        history_text = "Last 5 Directions:\n" + "\n".join(self.history[-5:][::-1])
        self.history_label.config(text=history_text)

        # Update counter label
        counter_text = f"Counter: {self.counter}"
        self.counter_label.config(text=counter_text)

        # Add direction to history and maintain only last 5 directions
        self.history.append(direction)
        if direction == "Front":
            self.y_axis.append(self.y_axis[-1] + 1)
        else : 
            self.y_axis.append(self.y_axis[-1] - 1)

        # Update the plot
        self.axis.clear()
        self.axis.set_title('Counter vs Y-Axis')
        self.axis.set_xlabel('Counter')
        self.axis.set_ylabel('Y-Axis')
        self.axis.plot(range(self.counter+1), self.y_axis)
        self.canvas.draw()

        
# Set up the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = DirectionApp(root)
    root.mainloop()
