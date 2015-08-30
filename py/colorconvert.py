#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this must come first
from __future__ import print_function, unicode_literals, division

# standard library imports
from colormath.color_objects import xyYColor, sRGBColor
from colormath.color_conversions import convert_color
import numpy as np
# import matplotlib.pyplot as plt
from matplotlib.mlab import griddata

# # lab = LabColor(0.903, 16.296, -2.22)
# # sRGBColor(rgb_r, rgb_g, rgb_b, is_upscaled=False)
# xyY = xyYColor(0.1, 0.7, 1, observer='2', illuminant='d65')
# rgb = convert_color(xyY, sRGBColor)
# print(rgb, rgb.get_upscaled_value_tuple())

# print(rgb.clamped_rgb_r)
# print(rgb.clamped_rgb_g)
# print(rgb.clamped_rgb_b)

# xyY = xyYColor(0.5, 0.35, 1., observer='2', illuminant='d65')
# rgb = convert_color(xyY, sRGBColor)
# print(rgb, rgb.get_upscaled_value_tuple())

# rgb = sRGBColor(1., 0., 0.)
# xyY = convert_color(rgb, xyYColor, target_illuminant='d65')
# print(rgb, xyY)

# rgb = sRGBColor(0., 1., 0.)
# xyY = convert_color(rgb, xyYColor, target_illuminant='d65')
# print(rgb, xyY)

# rgb = sRGBColor(0., 0., 1.)
# xyY = convert_color(rgb, xyYColor, target_illuminant='d65')
# print(rgb, xyY)


def drange(start, stop, step):
  r = start
  while r < stop:
    yield r
    r = r + step


def grid(x, y, z, resX=100, resY=100):
  "Convert 3 column data to matplotlib grid"
  xi = np.linspace(min(x), max(x), resX)
  yi = np.linspace(min(y), max(y), resY)
  Z = griddata(x, y, z, xi, yi)
  X, Y = np.meshgrid(xi, yi)
  return X, Y, Z


if __name__ == "__main__":

  # N = 50
  # x = np.random.rand(N)
  # y = np.random.rand(N)
  # colors = np.random.rand(N)
  # area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

  # plt.scatter(x, y, s=area, c=colors, alpha=0.5)
  # plt.show()

  xmin = 0.00
  xmax = 0.74
  ymin = 0.00
  ymax = 0.84
  valinc = 5.0e-3

  Y = 0.5
  obs = "2"
  ill = "d65"

  fmtstrttl = 5 * "{:12s}  " + "\n"
  fmtstr    = 5 * "{:12.10f}  " + "\n"

  with open("PaV.dat", "w") as fileout:

    fileout.write(
      fmtstrttl.format(
        "x", "y", "r", "g", "b"
      )
    )

    for x in drange(xmin, xmax, valinc):
      for y in drange(ymin, ymax, valinc):
        xyY = xyYColor(x, y, Y, observer=obs, illuminant=ill)
        rgb = convert_color(xyY, sRGBColor)
        rgb_clamped = sRGBColor(
          rgb.clamped_rgb_r,
          rgb.clamped_rgb_g,
          rgb.clamped_rgb_b
        )

        r, g, b = rgb_clamped.get_value_tuple()

        fileout.write(
          fmtstr.format(
            x, y, r, g, b,
          )
        )
