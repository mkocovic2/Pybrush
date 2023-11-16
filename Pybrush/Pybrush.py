from tkinter import *
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pybrush")

        self.canvas = Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.current_color = "black" 

        self.brush_button = Button(root, text="Brush", command=self.set_brush)
        self.brush_button.pack(side=LEFT)
        
        self.eraser_button = Button(root, text="Eraser", command=self.set_eraser)
        self.eraser_button.pack(side=LEFT)

        self.reset_button = Button(root, text="Reset Page", command=self.reset_canvas)
        self.reset_button.pack(side=LEFT)

        self.brush_size = 2
        self.eraser_size = 10

        self.brush_size_label = Label(root, text="Brush Size:")
        self.brush_size_label.pack(side=LEFT)
        self.brush_size_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, command=self.update_brush_size)
        self.brush_size_slider.pack(side=LEFT)
        self.brush_size_slider.set(self.brush_size)

        # Eraser size slider
        self.eraser_size_label = Label(root, text="Eraser Size:")
        self.eraser_size_label.pack(side=LEFT)
        self.eraser_size_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, command=self.update_eraser_size)
        self.eraser_size_slider.pack(side=LEFT)
        self.eraser_size_slider.set(self.eraser_size)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.last_x = None
        self.last_y = None

    def set_brush(self):
        self.canvas.configure(cursor="pencil")
        self.current_color = "black"  # Set the current_color to black

    def set_eraser(self):
        self.canvas.configure(cursor="circle")
        self.current_color = "white"  # Set the current_color to white

    def update_brush_size(self, value):
        self.brush_size = int(value)

    def update_eraser_size(self, value):
        self.eraser_size = int(value)

    def start_drawing(self, event):
        self.is_drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            if self.last_x and self.last_y:
                self.canvas.create_line(
                    self.last_x, self.last_y, x, y,
                    fill=self.current_color,
                    width=self.brush_size if self.current_color != "white" else self.eraser_size,
                    capstyle=ROUND,
                    smooth=TRUE
                )
            self.last_x = x
            self.last_y = y

    def stop_drawing(self, event):
        self.is_drawing = False
        self.last_x = None
        self.last_y = None

    def reset_canvas(self):
        self.canvas.delete("all")  # Clear the canvas

if __name__ == "__main__":
    root = Tk()
    icon = PhotoImage(file="paintBrush.png")
    root.iconphoto(True, icon)
    app = DrawingApp(root)
    root.mainloop()