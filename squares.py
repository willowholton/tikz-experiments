import random

# size of cells, number of rows/cols, and spacing:
size = 3
n = 8
gap = 0.2
rows = 3
cols = 3
spacing = size + gap

# set up document preamble and tikz picture:
document = [r"\documentclass[tikz, border=10pt]{standalone}", r"\begin{document}", r"\begin{tikzpicture}"]

# make cells:
for row in range(rows):
    for col in range(cols):
        # name this cell rc:
        name = f"{row}{col}"

        # get center point of this cell
        center_x = col * spacing
        center_y = -row * spacing

        # pick random point for the cell
        point_x = random.uniform(-(size/2) + 0.5 , (size/2) - 0.5)
        point_y = random.uniform(-(size/2) + 0.5 , (size/2) - 0.5)

        # pick random rgb value for this cell, will be set using \definecolor
        (r, g, b) = (random.randint(0, 255) for _ in range(3))
        defined_color = rf"\definecolor{{{name}}}{{RGB}}{{{r},{g},{b}}}" # f string needs {{ to produce one {
        document.append(defined_color)

        # draw concentric squares:
        for i in range(n):
            t = i / n
            # calculate four points of the square to draw
            x_0 = center_x - ((size/2) * (1 - t)) + (t * point_x)
            x_1 = center_x + ((size/2) * (1 - t)) + (t * point_x)
            y_0 = center_y - ((size/2) * (1 - t)) + (t * point_y)
            y_1 = center_y + ((size/2) * (1 - t)) + (t * point_y)

            # get shade value, concentric squares get lighter towards the center point:
            shade = 100 - 90 * t

            # draw individual square:
            document.append(rf"\draw[thick, {name}!{shade}] ({x_0},{y_0}) rectangle ({x_1},{y_1});")

document.append(r"\end{tikzpicture}")
document.append(r"\end{document}")

with open("squares.tex", "w") as f:
    f.write("\n".join(document) + "\n")