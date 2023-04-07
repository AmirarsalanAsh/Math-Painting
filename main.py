from canvas import Canvas
from shapes import Rectangle, Square

# get canvas width and height from the user
canvas_height = int(input("Please enter the height of the canvas: "))
canvas_width = int(input("Please enter the width of the canvas: "))

# make a dictionary of colors and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# create a canvas with the user data
canvas = Canvas(a=canvas_height, b=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit ")
    # ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # create the rectangle
        rec1 = Rectangle(x=rec_x, y=rec_y, a=rec_width, b=rec_height, color=(red, green, blue))
        rec1.draw(canvas)

    # ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter the side length of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # create the rectangle
        sq = Square(x=sq_x, y=sq_y, side=sq_side , color=(red, green, blue))
        sq.draw(canvas)

    # break the loop if user entered 'quit'
    if shape_type == 'quit':
        break

canvas.make('canvas.png')
