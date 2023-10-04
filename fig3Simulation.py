import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import pytest

# Global constants

X_INITIAL = 0.01
R_INITIAL = 0.0001
H = 0.05

# Functions


def x1_derivative(x1, r1):
  return 2.5 * x1 - 2 * x1 * r1


def x2_derivative(x2, r2):
  return 2.5 * x2 - 2 * x2 * r2


def r1_derivative(x1, r1, r2):
  return 0.1 * (r1 / (r1 + r2) * x1) - 0.1 * r1


def r2_derivative(x1, x2, r1, r2):
  return 0.1 * (r2 / (r1 + r2) * x1 + x2) - 0.1 * r2


def main():

  # Arrays

  xpoints = np.array([0])
  ypoints = np.array([X_INITIAL])

  x2points = np.array([0])
  y2points = np.array([0])

  rxpoints = np.array([0])
  rypoints = np.array([R_INITIAL])

  r2xpoints = np.array([0])
  r2ypoints = np.array([0])

  # Variables

  x1 = X_INITIAL
  r1 = R_INITIAL
  x2 = 0
  r2 = 0
  i = H

  # print(f"Time 0: x1: {x1} r1: {r1} x2 {x2} r2: {r2} \n")

  while i < 300:
    if i == pytest.approx(125):
      x2 = X_INITIAL
      r2 = R_INITIAL
    x1 = x1 + H * x1_derivative(x1, r1)
    if x1 < 0:
      x1 = 0
    r1 = r1 + H * r1_derivative(x1, r1, r2)
    if r1 < 0:
      r1 = 0
    x2 = x2 + H * x2_derivative(x2, r2)
    if x2 < 0:
      x2 = 0
    r2 = r2 + H * r2_derivative(x1, x2, r1, r2)
    if r2 < 0:
      r2 = 0
    # print(f"Time {i}: x1: {x1} r1: {r1} x2: {x2} r2: {r2} \n")
    xpoints = np.append(xpoints, [i])
    ypoints = np.append(ypoints, [x1])
    x2points = np.append(x2points, [i])
    y2points = np.append(y2points, [x2])
    rxpoints = np.append(rxpoints, [i])
    rypoints = np.append(rypoints, [r1])
    r2xpoints = np.append(r2xpoints, [i])
    r2ypoints = np.append(r2ypoints, [r2])
    i += H

  # Plotting

  x_new = np.linspace(xpoints.min(), xpoints.max(), 500)
  f = interp1d(xpoints, ypoints, kind='quadratic')
  y_smooth = f(x_new)

  x2_new = np.linspace(x2points.min(), x2points.max(), 500)
  f = interp1d(x2points, y2points, kind='quadratic')
  y2_smooth = f(x2_new)

  rx_new = np.linspace(rxpoints.min(), rxpoints.max(), 500)
  f = interp1d(rxpoints, rypoints, kind='quadratic')
  ry_smooth = f(rx_new)

  r2x_new = np.linspace(r2xpoints.min(), r2xpoints.max(), 500)
  f = interp1d(r2xpoints, r2ypoints, kind='quadratic')
  r2y_smooth = f(r2x_new)

  fig, (ax1, ax2) = plt.subplots(1, 2)
  fig.suptitle('Figure 3: A on the left, B on the right')
  ax1.plot(x_new, y_smooth, c='b')
  ax1.plot(x2_new, y2_smooth, color='g')
  ax2.plot(rx_new, ry_smooth, c='b')
  ax2.plot(r2x_new, r2y_smooth, c='g')

  plt.show()

# Execute main

if __name__ == "__main__":
  main()
