"""Generate reference images for tests.

Notes
-----
Run this function to generate reference images to compare against for future
tests.
"""
import os
import turtle
from house import *
from pre_quake import single_house_scene
import post_quake as post
from PIL import Image


def convert_to_png(ps_path: str):
    """Convert a postscript file to a png file.

    Parameters
    ----------
    ps_path : str
        The path to the postscript file to convert

    Notes
    -----
    Embedded function from: https://stackoverflow.com/questions/62053750
    """
    img = Image.open(ps_path)
    img.save(ps_path.replace(".ps", ".png"), "png")


def generate_scale_test_image(save_name: str):
    """Create a scene with two houses, one twice the scale of the other

    Parameters
    ----------
    save_name : str
        The name of the image to save, without an extension
    """

    scale_1 = 0.5
    scale_2 = 0.25
    offset = 300
    t = turtle.Turtle()
    t.speed(0)
    draw_bounding_box(t)
    single_house_scene(t, scale=scale_1, right_offset=offset)
    single_house_scene(t, scale=scale_2, right_offset=-offset)
    canvas = turtle.getcanvas()
    canvas.postscript(file=f"testdata/{save_name}.ps", colormode="color")
    convert_to_png(f"testdata/{save_name}.ps")
    os.remove(f"testdata/{save_name}.ps")
    t.done()


def generate_post_earthquake_test_image(save_name: str):
    t = turtle.Turtle()
    post.main(t)
    canvas = turtle.getcanvas()
    canvas.postscript(file=f"testdata/{save_name}.ps", colormode="color")
    convert_to_png(f"testdata/{save_name}.ps")
    os.remove(f"testdata/{save_name}.ps")


if __name__ == "__main__":
    save_name = "scaled_houses"
    generate_scale_test_image(save_name)

    save_name = "post_earthquake"
    generate_post_earthquake_test_image(save_name)

