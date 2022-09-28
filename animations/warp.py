#!/usr/bin/python3

import random
import tkinter as tk

# configure window and canvas size
width = 1000
height = width
# configure amount of stars to display
star_cnt = 500
# configure star movement speed (bigger number = faster)
star_speed = 20
# configure max star size in pixel
star_size_max = 7
# configure update rate of canvas in ms
fps = 1

stars = []


class Star:
    def __init__(self) -> None:
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        self.z = random.randint(1, width)

        self.sx = self.x
        self.sy = self.y
        self.px = self.x
        self.py = self.y

        self.pz = self.z

        self.r = 0

        # randomly make star red, green or blue
        c = random.randint(1, 3)
        if (c == 1):
            self.color = [255, 0, 0]
        elif (c == 2):
            self.color = [0, 255, 0]
        else:
            self.color = [0, 0, 255]

    def update(self):
        # change color of star when it's moving
        self.update_color()

        # re-calculate last position
        self.px = map(self.x / self.pz, 0, 1, (width / 2), width)
        self.py = map(self.y / self.pz, 0, 1, (height / 2), height)
        # calculate new position
        self.sx = map(self.x / self.z, 0, 1, (width / 2), width)
        self.sy = map(self.y / self.z, 0, 1, (height / 2), height)

        # increase star size if it's closer to the window edges
        self.r = map(self.z, 0, width, star_size_max, 1)

        # move star
        self.pz = self.z
        self.z = self.z - star_speed
        # if star moved out of the window set it back to a random location inside the window
        if (self.z < 1):
            self.x = random.randint(-width, width)
            self.y = random.randint(-height, height)
            self.z = random.randint(1, width)
            self.pz = self.z

    def update_color(self):
        color_step = random.randint(1, 25)

        r = self.color[0]
        g = self.color[1]
        b = self.color[2]

        if r == 255 and g <= 255 and b == 0:     # 1
            g = g + color_step
            if g >= 255:
                g = 255
                r = r - color_step
        elif r >= 0 and g == 255 and b == 0:     # 2
            r = r - color_step
            if r <= 0:
                r = 0
                b = b + color_step
        elif r == 0 and g == 255 and b <= 255:   # 3
            b = b + color_step
            if b >= 255:
                b = 255
                g = g - color_step
        elif r == 0 and g >= 0 and b == 255:     # 4
            g = g - color_step
            if g <= 0:
                g = 0
                r = r + color_step
        elif r >= 0 and g == 0 and b == 255:     # 5
            r = r + color_step
            if r >= 255:
                r = 255
                b = b - color_step
        elif r == 255 and g == 0 and b >= 0:     # 6
            b = b - color_step
            if b <= 0:
                b = 0
                g = g + color_step
        else:  # should never happen
            pass

        self.color[0] = r
        self.color[1] = g
        self.color[2] = b

    def get_star_color_rgb_tuple(self):
        c = (self.color[0], self.color[1], self.color[2])
        return c


def covert_rgb_tuple_to_tkinter_rgb(rgb):
    # translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb


def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


def update_canvas():
    canvas.delete("all")

    for s in stars:
        s.update()
        # canvas.create_oval(sx, sy, sx + r, sy + r, fill="white")
        canvas.create_line(s.sx, s.sy, s.px, s.py, width=s.r,
                           fill=covert_rgb_tuple_to_tkinter_rgb(s.get_star_color_rgb_tuple()))

    canvas.pack(expand=1)
    window.after(fps, update_canvas)


if __name__ == "__main__":
    # create star objects
    for d in range(0, star_cnt):
        stars.append(Star())

    # create window and canvas
    window = tk.Tk()
    window.title("Starfield")
    window.geometry(f"{width}x{height}")
    canvas = tk.Canvas(width=width, height=height, bg="black")

    # let's go
    update_canvas()
    window.mainloop()
