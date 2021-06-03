# -*- coding: utf-8 -*-

# AROSICS - Automated and Robust Open-Source Image Co-Registration Software
#
# Copyright (C) 2017-2021  Daniel Scheffler (GFZ Potsdam, daniel.scheffler@gfz-potsdam.de)
#
# This software was developed within the context of the GeoMultiSens project funded
# by the German Federal Ministry of Education and Research
# (project grant code: 01 IS 14 010 A-C).
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np


def _norm(array, normto):
    return [float(i) * (normto / max(array)) for i in array]


def subplot_2dline(XY_tuples, titles=None, shapetuple=None, grid=False):
    from matplotlib import pyplot as plt

    shapetuple = (1, len(XY_tuples)) if shapetuple is None else shapetuple
    assert titles is None or len(titles) == len(XY_tuples), \
        'List in titles keyword must have the same length as the passed XY_tuples.'
    fig = plt.figure(figsize=_norm(plt.figaspect(shapetuple[0] / shapetuple[1] * 1.), 10))
    for i, XY in enumerate(XY_tuples):
        ax = fig.add_subplot(shapetuple[0], shapetuple[1], i + 1)
        X, Y = XY
        ax.plot(X, Y, linestyle='-')
        if titles is not None:
            ax.set_title(titles[i])
        if grid:
            ax.grid(which='major', axis='both', linestyle='-')
    plt.tight_layout()
    plt.show(block=True)

    return fig


def subplot_imshow(ims, titles=None, shapetuple=None, grid=False):
    from matplotlib import pyplot as plt

    ims = [ims] if not isinstance(ims, list) else ims
    assert titles is None or len(titles) == len(ims), 'Error: Got more or less titles than images.'

    shapetuple = (1, len(ims)) if shapetuple is None else shapetuple
    fig, axes = plt.subplots(shapetuple[0], shapetuple[1],
                             figsize=_norm(plt.figaspect(shapetuple[0] / shapetuple[1] * 1.), 20))
    [axes[i].imshow(im, cmap='gray', interpolation='none', vmin=np.percentile(im, 2), vmax=np.percentile(im, 98))
     for i, im in enumerate(ims)]
    if titles is not None:
        [axes[i].set_title(titles[i]) for i in range(len(ims))]
    if grid:
        [axes[i].grid(which='major', axis='both', linestyle='-') for i in range(len(ims))]
    plt.tight_layout()
    plt.show(block=True)

    return fig


def subplot_3dsurface(ims, shapetuple=None):
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  # this is needed for fig.add_subplot(..., projection='3d')

    ims = [ims] if not isinstance(ims, list) else ims
    shapetuple = (1, len(ims)) if shapetuple is None else shapetuple
    fig = plt.figure(figsize=_norm(plt.figaspect((shapetuple[0] / 2.) / shapetuple[1] * 1.), 20))
    for i, im in enumerate(ims):
        ax = fig.add_subplot(shapetuple[0], shapetuple[1], i + 1, projection='3d')
        x = np.arange(0, im.shape[0], 1)
        y = np.arange(0, im.shape[1], 1)
        X, Y = np.meshgrid(x, y)
        Z = im.reshape(X.shape)
        ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('hot'))
        ax.contour(X, Y, Z, zdir='x', cmap=plt.get_cmap('coolwarm'), offset=0)
        ax.contour(X, Y, Z, zdir='y', cmap=plt.get_cmap('coolwarm'), offset=im.shape[1])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show(block=True)

    return fig
