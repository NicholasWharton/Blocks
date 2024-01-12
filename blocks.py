from tkinter import *
from pynput import keyboard
from random import randint

def randomFlash():
    global blues
    for i in range(1, 8):
            for j in range(1, 10):
                if i != 4 or j != 5:
                    if blues == 0:
                        canvas.itemconfig(rectangles[f"{i}_{j}"], fill=colorwheel[randint(0,15)], outline='')
                    else:
                        canvas.itemconfig(rectangles[f"{i}_{j}"], fill=blueswheel[randint(0,10)], outline='')

    if blues == 0:
        canvas.itemconfig(rectangles["4_5"], fill="white", outline='')
    else:
        canvas.itemconfig(rectangles["4_5"], fill="black", outline='')
    root.update()

def rainbowFlash():
    global blues
    for i in range(1, 8):
            for j in range(1, 10):
                if i != 4 or j != 5:
                    canvas.itemconfig(rectangles[f"{i}_{j}"], fill=colorwheel[randint(0,10)], outline='')

    canvas.itemconfig(rectangles["4_5"], fill="white", outline='')
    root.update()

def blue():
    global blues
    for i in range(1, 8):
            for j in range(1, 10):
                if i != 4 or j != 5:
                    canvas.itemconfig(rectangles[f"{i}_{j}"], fill="#7CB9E8", outline='')

    canvas.itemconfig(rectangles["4_5"], fill="#7CB9E8", outline='')
    root.update()

def on_press(key):
    global enters
    global endscreen
    global image_item
    global blues
    if key == keyboard.Key.enter:
        if endscreen == 0:
            enters += 1
            if enters == 4:
                for i in range(100):
                    randomFlash()
                enters = 0
                image_item = canvas.create_image(canvas.winfo_width() // 2, canvas.winfo_height() // 2, anchor=CENTER, image=image1)
                canvas.itemconfig(image_item, image=image1)
                endscreen = 1
            randomFlash()
        else:
            canvas.delete(image_item)
            endscreen = 0
    if key == keyboard.Key.shift_l:
        if blues == 0:
            blues = 1
        else:
            blues = 0
        randomFlash()
    if key == keyboard.Key.shift_r:
        for i in range(100):
            rainbowFlash()
        blue()
    else:
        if endscreen != 1:
            randomFlash()

root = Tk()

canvas = Canvas(root, bg="black", highlightthickness="0")
canvas.pack(fill=BOTH, expand=True)
root.attributes("-fullscreen", True)

# Create a rectangle on the canvas with a blue fill color
rectangles = {}

for i in range(1, 8):
    for j in range(1, 10):
        name = f"{i}_{j}"
        x1 = 213.333*(j-1)
        y1 = 154*(i-1)
        x2 = 213.333*j
        y2 = 154*i
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="")
        rectangles[name] = rectangle

colorwheel = ["#EF5350", "#EC407A", "#AB47BC", "#7E57C2", "#5C6BC0", "#42A5F5", "#29B6F6", "#26C6DA", "#26A69A", "#66BB6A", "#9CCC65", "#D4E157", "#FFEE58", "#FFCA28", "#FFA726", "#FF7043"]
blueswheel = ["#7CB9E8", "#00308F", "#72A0C1", "#F0F8FF", "#6CB4EE", "#002D62", "#007FFF", "#89CFF0", "#0066b2", "#0000FF", "#B9D9EB"]
enters = 0
endscreen = 0
blues = 0
image1 = PhotoImage(file="endscreen.png")
image_item = None 
randomFlash()

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    root.mainloop()
