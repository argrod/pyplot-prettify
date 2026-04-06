"""
Functions for converting pyplot figure colours to reflect colourblindness using
DaltonLens.

Authors: Aran Garrod <aran.garrod@gmail.com>
"""

import PIL
import numpy as np
from matplotlib.figure import Figure
from daltonlens import simulate


def fig_to_nparray(fig: Figure):
    fig.canvas.draw()
    buf = fig.canvas.buffer_rgba()
    w, h = fig.canvas.get_width_height()
    img = np.frombuffer(buf, dtype=np.uint8).reshape(h, w, 4)
    return img[:, :, :3]


def convert_colours(
    fig: Figure,
    simulator: simulate.Simulator = simulate.Simulator_Machado2009,
    deficiency: simulate.Deficiency = simulate.Deficiency.DEUTAN,
    severity: float = 1.0,
):
    """Convert pyplot Figure colours to reflect respective colour deficiency.

    Parameters
    ----------
    fig: Figure
    simulator: simulate.Simulator
    deficiency: simulate.Deficiency
    severity: float

    Returns
    -------
    Figure
    np.ndarray
    """
    # convert figure to rgb array
    img_array = fig_to_nparray(fig)
    sim = simulator()
    img_sim = sim.simulate_csd(
        img_array,
        deficiency,
        severity=severity,
    )
    output = PIL.Image.formarray(img_sim)
    out_array = np.asarray(output.convert("RGB"))
    return output, out_array
