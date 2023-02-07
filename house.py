#!/usr/bin/env python3

import turtle
import math

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700
DOOR_WIDTH = HOUSE_WIDTH / 8
DOOR_HEIGHT = HOUSE_HEIGHT / 4
GARAGE_DOOR_WIDTH = HOUSE_WIDTH / 5
GARAGE_DOOR_HEIGHT = HOUSE_HEIGHT / 4
TREE_HEIGHT = 250
TREE_WIDTH = 30
STARTING_X = -550
STARTING_Y = -400
WINDOW_SIZE = 80
FIRST_STORY = 250
SECOND_STORY = 150
N_WINDOWS = 8
CLOUD_X = [400, 450, 350, -400, -350]
CLOUD_HEIGHT = 250
ZAG_NUMBER = 8
ZAG_DEGREE = 200
FULL_TREE_WIDTH = 4 * TREE_WIDTH

TRUNCK_COLOR = "brown"
BRANCH_COLOR = "green"
BRANCH_ANGLE = 180 - 45
HOUSE_COLOR = "#f571cb"
SKY_COLOR = "lightblue"
PEN_COLOR = "black"
CLOUD_COLOR = "white"
WINDOW_COLOR = "darkgray"
DOOR_COLOR = "#03a9fc"
DOORKNOB_COLOR = "#f5d60f"
GARAGE_COLOR = "grey"
GARAGE_WINDOW_COLOR = "white"


def draw_circle(t, radius, color=CLOUD_COLOR):
    """Draw a circle.

    Params:
        t: the Turtle object
        radius: radius of the circle
        color: color of the circle
    """
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.pencolor(PEN_COLOR)


def draw_bounding_box(t):
    """Draw bounding box to put house in.

    Params:
        t: the Turtle object
    """
    t.fillcolor(SKY_COLOR)
    t.penup()
    t.goto(STARTING_X, STARTING_Y)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.left(90)
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.end_fill()


def draw_house(t, scale=1, right_offset=0, tilt=0):
    """Draw outline of house and make it pink.

    Params:
        t: the Turtle object
        scale: scale of the house, default is 1
        right_offset: rightward offset from the center of the bounding box
            (negative values denote leftward offset), default is 0
    """
    house_height = scale * HOUSE_HEIGHT
    house_width = scale * HOUSE_WIDTH

    t.penup()
    t.goto(
        STARTING_X + right_offset +
        (BOUNDING_WIDTH - house_width) / 2, STARTING_Y
    )
    t.seth(90+tilt)
    t.fillcolor(HOUSE_COLOR)
    t.begin_fill()
    t.pendown()
    t.forward(house_height)
    t.right(90)
    t.forward(house_width)
    t.right(90)
    t.forward(house_height)
    t.end_fill()


def draw_branches(t, tree_width):
    """Draw branches for the tree

    Params:
        t: the Turtle object.
        tree_width: width of the tree
    """
    # isosceles right triangle length
    length = tree_width * math.sqrt(2)

    t.fillcolor(BRANCH_COLOR)
    t.begin_fill()
    t.forward(tree_width)
    t.left(BRANCH_ANGLE)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(BRANCH_ANGLE)
    t.forward(tree_width)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(tree_width)
    t.right(90)
    t.pendown()


def draw_tree(t, scale=1):
    """Draw a tree 

    Params:
        t: the Turtle object.
    """
    tree_width = scale * TREE_WIDTH
    tree_height = scale * TREE_HEIGHT

    # tree trunk
    t.fillcolor(TRUNCK_COLOR)
    t.begin_fill()
    t.left(90)
    t.forward(tree_height)
    t.right(90)
    t.forward(tree_width)
    t.right(90)
    t.forward(tree_height)
    t.right(90)
    t.forward(tree_width / 2)
    t.end_fill()

    # move to branch location
    t.penup()
    t.right(90)
    t.forward(tree_height)
    t.right(90)
    t.pendown()

    # draw branches
    draw_branches(t, tree_width * 4)
    draw_branches(t, tree_width * 3)
    draw_branches(t, tree_width * 2)


def draw_all_trees(t):
    """Draw two trees, one on each side of the house

    Params:
        t: the Turtle object.
    """

    # get width space for the two sides of the house
    side_widths = BOUNDING_WIDTH - HOUSE_WIDTH

    # get half the width space for one of the side
    half_w = side_widths / 4

    # set starting point to half of side width - half tree width
    gap = half_w - TREE_WIDTH / 2

    # move to starting point
    t.left(90)
    t.forward(gap)

    # draw right tree
    draw_tree(t)

    # move to the other side (1/2 side width + house width)
    gap = half_w + HOUSE_WIDTH

    # move to left tree
    t.penup()
    t.goto(400.00, -400.00)
    t.pendown()
    t.right(180)
    t.forward(gap)
    t.right(180)

    # draw left tree
    draw_tree(t)



def cracked_window(t, num_zag, scale=1, tilt=0):
    """Draws a window with a zigzag shaped crack.

    Params:
        t: the Turtle object.
        num_zag: the number of individual zags in the zigzag
        scale: scaling size of window
        tilt: tilt of window
    """
    window_size= scale * WINDOW_SIZE 
    window_diagonal = window_size / math.cos(ZAG_DEGREE - 180)  # find length of diagonal across window at desired angle
    diagonal_zag_length = window_diagonal / num_zag # finding the total displacement of the zag line
    zag_line_length = diagonal_zag_length / (2 * 2**(1/2)) # size of each individual zag
    draw_window(t, scale)  # using the original window function
    
    t.seth(200)
    zag_back = 0
    for h in range(2):  # create zig zag line and return turtle to start location
        if zag_back == 1:
            t.penup()
        for i in range(num_zag - 1):
            t.forward(zag_line_length * (-1) ** h)
            t.left(90)
            t.forward(zag_line_length * (-1) ** h)
            t.right(90)
        zag_back = zag_back + 1
        t.pendown()
    t.seth(180)


def draw_all_cracked_windows(t, right_offset=0, scale=1, tilt=0):
    """Draws all the windows from the original pre-earthquake state, but adds a crack through each of them".
    Params:
        t: the Turtle object.
        right_offset: right_offset of window
        scale: size scaling of window
        tilt: tilt of window
    """
    start_loc = t.pos()

    house_width = scale * HOUSE_WIDTH
    window_size = scale * WINDOW_SIZE
    first_story = scale * FIRST_STORY
    second_story = scale * SECOND_STORY

    # distance between window and edge of house to be nicely spaced
    margin = (house_width - (N_WINDOWS - 1) * window_size) / 2

    t.penup()
    t.goto(STARTING_X + right_offset + BOUNDING_WIDTH / 2 + house_width / 2, STARTING_Y)
    t.seth(90)
    t.forward(first_story)
    t.left(90)
    t.forward(margin)
    t.pendown()

    t.seth(180 + tilt)
    # First row of windows
    cracked_window(t, ZAG_NUMBER, scale=scale)

    t.seth(180+tilt)
    for i in range(int(N_WINDOWS / 2) - 1):
        if i // 2 == 1:
            t.penup()
            t.forward(2 * window_size)
            t.pendown()
            cracked_window(t, 10, scale=scale)
        else:
            t.penup()
            t.forward(2 * window_size)
            t.pendown()

           # move to location of second window row
            draw_window(t, scale=scale)
      
    t.penup()
    t.seth(90)
    t.forward(second_story)
    t.right(90)
    t.forward(2 * (N_WINDOWS / 2 - 1) * window_size)
    t.left(180)
    t.pendown()

    t.seth(180 + tilt)
    cracked_window(t, ZAG_NUMBER, scale=scale)
    for i in range(int(N_WINDOWS / 2) - 1):
        if i // 2 == 1:
            t.penup()
            t.seth(180+tilt)
            t.forward(2 * window_size)
            t.pendown()
            cracked_window(t, ZAG_NUMBER, scale=scale)
        else:
            t.penup()
            t.seth(180+tilt)
            t.forward(2 * window_size)
            t.pendown()
            draw_window(t, scale=scale)

    # move turtle to the start location
    t.penup()
    t.goto(start_loc)
    t.pendown()
    t.seth(270)


def draw_window(t, scale=1):
    """Draw a row of 4 windows

    Params:
        t: the Turtle object.
    """
    window_size = scale * WINDOW_SIZE

    t.fillcolor(WINDOW_COLOR)
    t.begin_fill()
    for i in range(4):
        t.forward(window_size)
        t.left(90)
    t.end_fill()


def draw_all_windows(t, windows_per_row, scale=1, right_offset=0, tilt=0):
    """Draw four windows on the house

    Params:
        t: the Turtle object.
        windows_per_row: number of windows per row
        scale: scale of the house, default is 1
        right_offset: rightward offset from the center of the bounding box
            (negative values denote leftward offset), default is 0
    """
    start_loc = t.pos()

    house_width = scale * HOUSE_WIDTH
    window_size = scale * WINDOW_SIZE
    first_story = scale * FIRST_STORY
    second_story = scale * SECOND_STORY

    # distance between window and edge of house to be nicely spaced
    margin = (house_width - (2 * windows_per_row - 1) * window_size) / 2

    t.penup()
    t.goto(
        STARTING_X + right_offset +
        BOUNDING_WIDTH / 2 + house_width / 2, STARTING_Y)
    t.seth(90)
    t.forward(first_story)
    t.left(90)
    t.forward(margin)
    t.pendown()
    t.seth(180+tilt)

    draw_window(t, scale=scale)
    for _ in range(windows_per_row - 1):
        t.penup()
        t.forward(2 * window_size)
        t.pendown()
        draw_window(t, scale=scale)

    t.penup()
    t.seth(90)
    t.forward(second_story)
    t.right(90)
    t.forward(2 * (windows_per_row - 1) * window_size)
    t.left(180)
    t.pendown()
    t.seth(180 + tilt)

    draw_window(t, scale=scale)
    for _ in range(windows_per_row - 1):
        t.penup()
        t.seth(180+tilt)
        t.forward(2 * window_size)
        t.pendown()
        draw_window(t, scale=scale)

    t.penup()
    t.goto(start_loc)
    t.pendown()
    t.seth(270)


def draw_door(t, door_width, door_height, scale=1, right_offset=0, tilt=0):
    """Draw door of house, touching the bottom

    Params:
        t: the Turtle object.
        door_width: width of door
        door_height: height of door
        scale: scale factor, default is 1
        right_offset: rightward offset from the center of the bounding box
            (negative values denote leftward offset), default is 0
    """
    door_width = scale * door_width
    door_height = scale * door_height
    house_width = scale * HOUSE_WIDTH

    doorknob = door_width / 15

    # save starting position for later
    start_loc = t.pos()

    # after drawing house, get to door starting point
    t.penup()
    t.goto(
        STARTING_X + right_offset +
        BOUNDING_WIDTH / 2 - house_width / 4, STARTING_Y
    )
    t.seth(90+tilt)

    # draw door
    t.pendown()
    t.fillcolor(DOOR_COLOR)
    t.begin_fill()
    t.forward(door_height)
    t.left(90)
    t.forward(door_width)
    t.left(90)
    t.forward(door_height)
    t.end_fill()

    # draw doorknob
    t.left(90)
    t.forward(door_width * 0.8)
    t.left(90)
    t.penup()
    t.forward(door_height / 2)
    t.pendown()
    draw_circle(t, doorknob, DOORKNOB_COLOR)
    t.penup()
    t.left(180)
    t.forward(door_height / 2)
    t.pendown()
    t.left(90)
    t.forward(door_width * 0.2)
    t.penup()

    # go back to position before drawing door
    t.goto(start_loc)


def draw_rectangle(t, width, height, color, tilt=0):
    """Draw a rectangle starting at the bottom left corner

    Params:
        t: the Turtle object.
        width: the width of the rectangle
        height: the height of the rectangle
        color: the color of the rectangle
    """
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.seth(90+tilt)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.penup()
    t.end_fill()


def draw_garage_windows(t, window_width, window_height, garage_width, garage_height, tilt=0):
    """Draw two garage windows 

    Params:
        t: the Turtle object.
        window_width: the width of each window
        window_height: the height of each window
        garage_width: the width of the garage
        garage_height: the height of the garage
    """
    # set starting location for window 1
    window_x = garage_width / 2.2
    window_y = 3 * garage_height / 4

    # move to window 1 location
    t.penup()
    t.right(180)
    t.forward(window_x)
    t.right(90)
    t.forward(window_y)

    # draw window 1
    draw_rectangle(t, window_width, window_height, GARAGE_WINDOW_COLOR, tilt=tilt)

    # move to window 2 location
    t.forward(window_x)

    # draw window 2
    draw_rectangle(t, window_width, window_height, GARAGE_WINDOW_COLOR, tilt=tilt)


def draw_all_garages(t, garage_width, garage_height, scale=1, right_offset=0, tilt=0):
    """Draw two garages next to each other

    Params:
        t: the Turtle object.
        garage_width: the width of the garage
        garage_height: the height of the garage
        scale: scale factor, default is 1
        right_offset: rightward offset from the center of the bounding box
            (negative values denote leftward offset), default is 0
    """
    garage_width *= scale
    garage_height *= scale
    window_width = garage_width / 3
    window_height = garage_height / 7
    t.penup()
    garage_x_start = STARTING_X + right_offset + BOUNDING_WIDTH / 2
    garage_x_locations = [0, 6 * garage_width / 5]

    # draw garages at garage_x_locations
    for x_value in garage_x_locations:
        t.goto(garage_x_start + x_value, STARTING_Y)
        t.seth(90 - tilt)
        draw_rectangle(t, garage_width, garage_height, GARAGE_COLOR, tilt=tilt)
        t.right(180)
        t.forward(garage_width)
        t.seth(tilt)
        draw_garage_windows(
            t, window_width, window_height, garage_width, garage_height, tilt=tilt
        )


def draw_cloud(t, radius=30, color=CLOUD_COLOR, x_start=0, y_start=0):
    """Draw a cloud.

    Params:
        t: the Turtle object
        radius: radius of the circle
        color: color of the circle
        x_start: x coordinate for starting pos
        y_start: y coordinate for starting pos
    """
    t.penup()
    t.goto(x_start, y_start)
    t.pendown()
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)


def draw_all_clouds(t, cloud_x, cloud_height):
    """Draw two clouds.
    Params:
        t: the Turtle object.
        cloud_x: starting x positions
        cloud_height: starting cloud height
    """
    for position in cloud_x:
        draw_cloud(t, x_start=position, y_start=cloud_height)


def main(t):
    draw_bounding_box(t)
    draw_house(t)
    draw_door(t, DOOR_WIDTH, DOOR_HEIGHT)
    draw_all_windows(t, N_WINDOWS // 2)
    draw_all_trees(t)
    draw_all_clouds(t, CLOUD_X, CLOUD_HEIGHT)
    draw_all_garages(t, GARAGE_DOOR_WIDTH, GARAGE_DOOR_HEIGHT)


if __name__ == "__main__":
    t = turtle.Turtle()
    main(t)
    turtle.done()
