#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Verify slide sequence and boundaries without external services."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from names_of_Allah import MAX_SLIDE, MIN_SLIDE, slide_path


class SlidesTests(unittest.TestCase):
    def test_all_historical_slides_exist(self):
        for index in range(MIN_SLIDE, MAX_SLIDE + 1):
            with self.subTest(index=index):
                self.assertTrue(slide_path(index).is_file())

    def test_reject_invalid_indices(self):
        for index in (-1, 0, 101, 999):
            with self.subTest(index=index), self.assertRaises(ValueError):
                slide_path(index)

    def test_path_does_not_depend_on_current_directory(self):
        self.assertEqual(slide_path(1).name, "1.png")


if __name__ == "__main__":
    unittest.main()
