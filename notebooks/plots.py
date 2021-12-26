#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid:   22439f0c-60dc-11ec-9f1c-59bf937234c8
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


from matplotlib import figure

import matplotlib.pyplot as plt


# ------------
# Custom Modules

# -------------

def set_axis_labels(
    ax,
    title=None,
    x_label=None,
    y_label=None,
    z_label=None,
    **kwargs,
):
    """
    Given an axis (ax), set the title, x, y and z axis labels.

    NOTE: It will only set the values if they are not None.

    # Parameters

    ax:matplotlib.axis
        - The axis to set the

    title:str
        - The title to apply to the axis. If None, it will not be applied
        - DEFAULT - None

    x_label:str
        - The title to apply to the x-axis. If None, it will not be applied
        - DEFAULT - None

    y_label:str
        - The title to apply to the y-axis. If None, it will not be applied
        - DEFAULT - None

    z_label:str
        - The title to apply to the z-axis. If None, it will not be applied
        - DEFAULT - None

    """

    if title:
        ax.set_title(title)

    if x_label:
        ax.set_xlabel(x_label)

    if y_label:
        ax.set_ylabel(y_label)

    if z_label:
        ax.set_zlabel(z_label)


def standardize_axis(
    ax,
    title=None,
    x_label=None,
    y_label=None,
    z_label=None,
    **kwargs,
):
    """
    Given an axis, standardize it by setting grid lines for the major
    and minor axes. In addition, you can set the axis labels
    (titles, x-axis, y-axis, z-axis)

    NOTE: If the title and labels are None, they will not be set.

    # Parameters

    ax:matplotlib.axis
        - The axis to set the

    title:str
        - The title to apply to the axis. If None, it will not be applied
        - DEFAULT - None

    x_label:str
        - The title to apply to the x-axis. If None, it will not be applied
        - DEFAULT - None

    y_label:str
        - The title to apply to the y-axis. If None, it will not be applied
        - DEFAULT - None

    z_label:str
        - The title to apply to the z-axis. If None, it will not be applied
        - DEFAULT - None

    # Parameters (kwargs)

    major_grid_color:str
        - The color of the grid for the major axes (x,y and z)
        - DEFAULT - 'k'

    minor_grid_color:str
        - The color of the grid for the minor axes (x,y and z)
        - DEFAULT - 'k'

    major_grid_linestyle:str
        - The line style of the grid for the major axes
        - DEFAULT - '-'

    minor_grid_linestyle:str
        - The line style of the grid for the minor axes
        - DEFAULT - '-'

    major_grid_alpha:float
        - The transparency of the grid for the major axes
        - DEFAULT - 0.6

    minor_grid_alpha:float
        - The transparency of the grid for the minor axes
        - DEFAULT - 0.2

    """

    ax.grid(
        b=True,
        which="major",
        color=kwargs.get("major_grid_color", "k"),
        linestyle=kwargs.get("major_grid_linestyle", "-"),
        alpha=kwargs.get("major_grid_alpha", 0.6),
    )

    ax.grid(
        b=True,
        which="minor",
        color=kwargs.get("minor_grid_color", "k"),
        linestyle=kwargs.get("minor_grid_linestyle", "-"),
        alpha=kwargs.get("minor_grid_alpha", 0.2),
    )

    ax.minorticks_on()

    set_axis_labels(ax, title, x_label, y_label, z_label)


def create_figure(**kwargs):
    """
    Create a matplotlib.Figure object suitable for a single plot.

    # Parameters (kwargs)

    interactive_mode:bool

        - When True, it will create a Figure from matplotlib.pyplot if
          the intention is to display it interactively. If the
          intention is batch plotting to a file, set it to False. If
          the intention is to write the images to a file, set this to
          False, otherwise you will see a memory leak.

        - DEFAULT - True

    # Parameters (kwargs)

    These are the available options used in the Figure/figure
    constructor:

    - axes_rect
    - projection
    - polar
    - num
    - figsize
    - dpi
    - facecolor
    - edgecolor
    - frameon
    - FigureClass
    - clear

    For more details about these options see:

    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    - https://matplotlib.org/stable/api/figure_api.html

    For details on the memory leak:

    - https://stackoverflow.com/a/12300012

    """

    valid_kwargs = [
        'num',
        'figsize',
        'dpi',
        'facecolor',
        'edgecolor',
        'frameon',
        'FigureClass',
        'clear',
    ]

    figure_switches = {k:v for k,v in kwargs.items() if k in valid_kwargs}

    if kwargs.get('interactive_mode', True):

        fig = plt.figure(**figure_switches)

    else:

        fig = figure.Figure(**figure_switches)

    axes_rect = kwargs.get("axes_rect", (0, 0, 1, 1))
    projection = kwargs.get("projection", None)
    polar = kwargs.get("polar", False)

    ax = fig.add_axes(
        axes_rect,
        projection=projection,
        polar=polar,
    )

    return fig, ax


def create_standard_figure(
    title=None,
    x_label=None,
    y_label=None,
    z_label=None,
    **kwargs,
):
    """

    Create a standard figure and axis object suitable for one plot.

    # Parameters

    title:str
        - The title to apply to the axis. If None, it will not be applied
        - DEFAULT - None

    x_label:str
        - The title to apply to the x-axis. If None, it will not be applied
        - DEFAULT - None

    y_label:str
        - The title to apply to the y-axis. If None, it will not be applied
        - DEFAULT - None

    z_label:str
        - The title to apply to the z-axis. If None, it will not be applied
        - DEFAULT - None

    # Parameters (kwargs)

    standard_axis:bool
        - Apply the standard axis transformations.
        - DEFAULT - True

    NOTE: For additional kwargs, see create_figure()

    """

    standard_axis = kwargs.get('standard_axis', True)

    fig, ax = create_figure(**kwargs)

    if standard_axis:
        standardize_axis(
            ax,
            title,
            x_label,
            y_label,
            z_label,
            **kwargs,
        )

    return fig, ax


def axis_legend_remove_duplicates(
    ax=None,
    **kwargs,
):
    """

    Remove duplicates items from axis legends

    # Args

    ax

    # Kwargs (Optional)

    normalize:bool
        - If true, set all the labels to title case.

    # Example

    labels = axis_legend_remove_duplicates(ax)
    ax.legend(
        labels.values(),
        labels.keys(),
        loc='lower right',
    )

    """

    handles, labels = ax.get_legend_handles_labels()

    if kwargs.get('normalize', False):
        labels = [l.title() for l in labels]

    return dict(zip(labels, handles))

