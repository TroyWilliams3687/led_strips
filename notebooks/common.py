#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid:   d9d00492-60e3-11ec-9f1c-59bf937234c8
# author: Troy Williams
# email:  troy.williams@bluebill.net
# date:   2021-12-19
# -----------

"""
"""

# ------------
# System Modules - Included with Python

# ------------
# 3rd Party - From PyPI

import numpy as np

# ------------
# Custom Modules

# -------------


def plot_cone(ax, r:float, h:float):
    """
    Given a matplotlib.axes object, set for 3D plotting, plot a
    right-cone approximation using circles

    # args

    ax: matplotlib.axes
        - The axes to draw the cone on

    r - The radius of the base of the cone

    h - The height of the cone from the base

    NOTE: The radius and height should be the same unit.

    """

    # Define an array of angles that define the circles.
    phi = np.linspace(0.0, 2*np.pi, 50)

    cone_label = f'Cone r={r:.2f} h={h:.2f}'

    handles = []

    # Create a circle for each point along the z axis so that it looks
    # like a cone
    for z in np.linspace(0.0, h, 50):

        x = (r-z*(r/h))*np.cos(phi)
        y = (r-z*(r/h))*np.sin(phi)

        handle, = ax.plot(x, y, z, '-', color='blue', label=cone_label, alpha=0.25)

        handles.append(handle)

        # Are we at the last point, draw a point because a zero radius
        # circle will not be displayed
        if np.all((x == 0)) and np.all((y == 0)):
            handle, ax.plot(0, 0, z, '-', color='blue', label=cone_label, marker='o', alpha=0.15)

            handles.append(handle)

    return handles


def plot_spiral(ax, r:float, h:float, d:float):
    """
    Plot an Archimedean spiral traced around a right-cone.

    # args

    ax: matplotlib.axes
        - The axes to draw the cone on

    r - The radius of the base of the cone

    h - The height of the cone from the base

    d - The horizontal distance between spiral loops on the XY plane.
    Basically this is the distance between intersection points of the
    spiral on the XY plane with the X-axis.

    NOTE: The radius and height should be the same unit.

    """


    # calculate b based on our d value, the distance between loops in the spiral
    b = d/(2*np.pi)

    # Calculate the limit of our theta angle, that is how for do we
    # need to sweep the curve to get it to the base

    theta_limit = r/b

    z0 = h
    m = -z0*(b/r)

    theta = np.linspace(0.0, theta_limit, 400)

    x = b*theta*np.cos(theta)
    y = b*theta*np.sin(theta)
    z = m*theta + z0

    spiral_label = f'Spiral r={r:.2f} h={h:.2f} d={d:.2f}'

    handle, = ax.plot(
        x, y, z,
        '-',
        color='red',
        label=spiral_label,
    )

    return handle

def plot_center_pole(ax, h: float):
    """
    Plot a center pole for the spiral/cone of height h.
    """


    z = np.arange(0.0, h, step=1.0)
    z = np.append(z, h)
    x = np.zeros(z.shape)
    y = np.zeros(z.shape)

    handle, = ax.plot(x,y,z, '-', color='black', marker='o')

    return handle


def plot_cone_and_sprial(ax, r:float, h:float, d:float):
    """
    Plot a right-cone approximation using circles with an Archimedean
    spiral traced around it. It will also plot a center pole line.

    # args

    ax - matplotlib axis

    r - The radius of the base of the cone

    h - The height of the cone from the base

    d - The horizontal distance between spiral loops on the XY plane.
    Basically this is the distance between intersection points of the
    spiral on the XY plane with the X-axis.

    """

    print(f'Cone Radius (r) = {r:.4f}')
    print(f'Cone Height (h) = {h:.4f}')
    print(f'Sprial Distance (d) = {d:.4f}')

    cone_handle = plot_cone(ax, r, h)[0] # Grab the first handle - the rest will be duplicates

    spiral_handle = plot_spiral(ax, r, h, d)

    plot_center_pole(ax, h)

    al = spiral_arc_length_range(r, h, d)

    ax.legend(
        handles=[cone_handle, spiral_handle],
        labels=[f'Cone r={r:.2f} h={h:.2f}', f'Spiral d={d:.2f} length={al:.2f}'],
        loc='best',
        shadow=True,
        fancybox=True,
        prop={'family': 'monospace', 'size':12},
        frameon=True,
    )


def spiral_arc_length(b:float, k:float, t:float) -> float:
    """
    This is an implementation of the integral soltion to calculating the arc length of the 3D conic
    spiral.

    b - 2*pi*d is the distance between successive turns in the spiral
    k - This is a constant applied to the z axis so that it can expand or shrink the curve. If it is 1, then
        the curve z portion will be defined by the theta value
    t - The length of the curve to a particular angle in radians


    Returns the length of the curve at angle t
    """

    sqr = np.sqrt(b**2*(t**2 + 1) + k**2)

    return ((k**2 + b**2)*np.log(sqr + b*t) + b*t*sqr)/(2*b)


def spiral_arc_length_range(r:float, h:float, d:float) -> float:
    """
    Given the radius, r, and height, h, of a right-cone,
    determine the arc length of the spiral wrapping
    around the outside of the cone from the base to the tip.

    # args

    r - radius of the base of the cone.
    h - height of the cone.
    d - distance between loops of the spiral projected
        onto the XY plane. These are measured from the
        intersections with the x-axis on the XY plane.

    # Return

    The arc length of the spiral.

    """

    b = d/(2*np.pi)
    m = -h*(b/r)
    theta_limit = r/b

    l_min = spiral_arc_length(b, m, 0)
    l_max = spiral_arc_length(b, m, theta_limit)

    return l_max - l_min

def calculate_support_points(r, h, d, delta_h=1.0):

    b = d/(2*np.pi)
    theta_limit = r/b
    m = -h*(b/r)

    z = np.arange(0.0, h, step=delta_h)

    theta = (z - h)/m

    x = b*theta*np.cos(theta)
    y = b*theta*np.sin(theta)
    z = m*theta + h

    return x, y, z
