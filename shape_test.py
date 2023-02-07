#!/usr/bin/env python3

from PIL import Image
import matplotlib.testing.compare as mpcompare
import unittest
import house
import tempfile
import os.path
import svg_turtle
import inspect
import post_quake as post

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

CANVAS_SIZE = (1400, 1000)
HOUSE_WIDTH = 700
HOUSE_HEIGHT = 500
N_WINDOWS = 8


class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename, override_tmpdir=None):
        """ compares the current canvas to an expected file.
        Returns None if and only if the files are identical.
        
        If override_tmpdir is set, use that directory for temporary files 
        (useful for generating known good testdata images.
        """

        TOLERANCE = 1.0  # somewhere between 0 and 255, higher is more lax.

        with tempfile.TemporaryDirectory() as tmp_dirname:
            calling_function = inspect.stack()[1][3]
            tmp_dirname = tmp_dirname if not override_tmpdir else override_tmpdir

            actual_svg = os.path.join(tmp_dirname, "%s.svg" % calling_function)
            actual_png = os.path.join(tmp_dirname, "%s.png" % calling_function)

            self._turtle.save_as(actual_svg)

            # canvas generates a svg file, but we have to convert it to a png in
            # order to compare it using matplotlib's library
            drawing = svg2rlg(actual_svg)
            renderPM.drawToFile(drawing, actual_png, fmt="PNG")
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)

    def setUp(self):
        # this is run before every test
        self._turtle = svg_turtle.SvgTurtle(*CANVAS_SIZE)
        self._turtle.reset()
        self._turtle.speed("fastest")
        # self._turtle.tracer(0,0)

    def test_full_image(self):
        # generate full house drawing
        house.main(self._turtle)
        # compare this house drawing to the correct house.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/house.png")
        )

    def test_trees(self):
        # generate full house drawing
        house.draw_all_trees(self._turtle)

        # compare this house drawing to the correct house.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/trees.png")
        )


    def test_garages(self):
        # draw two garages with house.py
        house.draw_all_garages(
            self._turtle, HOUSE_WIDTH / 5, HOUSE_HEIGHT / 4
        )
        # compare these garages to the correct garages.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/garages.png")
        )
    
    def test_clouds(self):
    # draw clouds with house.py
        house.draw_all_clouds(
            self._turtle, house.CLOUD_X, house.CLOUD_HEIGHT
        )
        # compare these clouds to the correct clouds.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/clouds.png")
        )

    def test_door(self):
        # draw door with house.py
        house.draw_door(
            self._turtle, HOUSE_WIDTH / 8, HOUSE_HEIGHT / 4
        )
        # compare door to the correct door.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/door.png")
        )

    def test_windows(self):
        # draw eight windows with house.py
        house.draw_all_windows(
            self._turtle, N_WINDOWS // 2
        )
        # compare these windows to the correct windows.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/windows.png")
        )

    def test_post_earthquake(self):
        # generate full house drawing
        post.main(self._turtle)
        # compare this house drawing to the correct house.png
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename="testdata/post_earthquake.png")
        )

    def scaling(self):
        from pre_quake import *
        single_house_scene(t, tilt = 0, scale = 0.5, right_offset=300)
        single_house_scene(t, tilt = 0, scale = 0.25, right_offset=-300)
        self.assertIsNone(
            self._compare_canvas_to_expected(expected_filename = "testdata/scaled_houses.png")
        )


if __name__ == "__main__":
    unittest.main()
