#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this must come first
from __future__ import print_function, unicode_literals, division

# standard library imports
from colormath.color_objects import xyYColor, sRGBColor
from colormath.color_conversions import convert_color

# lab = LabColor(0.903, 16.296, -2.22)
# sRGBColor(rgb_r, rgb_g, rgb_b, is_upscaled=False)
xyY = xyYColor(0.1, 0.7, 1, observer='2', illuminant='d65')
rgb = convert_color(xyY, sRGBColor)
print(rgb, rgb.get_upscaled_value_tuple())

print(rgb.clamped_rgb_r)
print(rgb.clamped_rgb_g)
print(rgb.clamped_rgb_b)

xyY = xyYColor(0.5, 0.35, 1., observer='2', illuminant='d65')
rgb = convert_color(xyY, sRGBColor)
print(rgb, rgb.get_upscaled_value_tuple())

rgb = sRGBColor(1., 0., 0.)
xyY = convert_color(rgb, xyYColor, target_illuminant='d65')
print(rgb, xyY)

rgb = sRGBColor(0., 1., 0.)
xyY = convert_color(rgb, xyYColor, target_illuminant='d65')
print(rgb, xyY)

rgb = sRGBColor(0., 0., 1.)
xyY = convert_color(rgb, xyYColor, target_illuminant='d65')
print(rgb, xyY)
