"""Draw a neighborhood before the earthquake.
"""

import turtle
from house import *
from pre_quake import *


def main(t):
    """Generate the post-earthquake scene.
    """
    t.speed(0)
    draw_bounding_box(t)
    nominal_scale_factor = 0.3
    reduced_scale_factor = 0.9
    nominal_offset = 400
    single_house_scene(
        t, tilt=0, scale=nominal_scale_factor, right_offset=nominal_offset, crack=True
    )
    single_house_scene(
        t, tilt=5, scale=nominal_scale_factor * reduced_scale_factor, right_offset=0, crack=True
    )
    single_house_scene(
        t, tilt=0, scale=nominal_scale_factor, right_offset=-nominal_offset, crack= True
    )


if __name__ == "__main__":
    t = turtle.Turtle()
    main(t)
    turtle.done()
