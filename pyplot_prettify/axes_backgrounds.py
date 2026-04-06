def style_spines(ax, top=False, right=False):
    """Remove top/right spines (cleaner look)."""
    ax.spines["top"].set_visible(top)
    ax.spines["right"].set_visible(right)
    return ax


def style_grid(ax, axis="y", linestyle="--", alpha=0.5, color="grey"):
    """Add a subtle background grid."""
    ax.grid(True, axis=axis, linestyle=linestyle, alpha=alpha, color=color)
    ax.set_axisbelow(True)  # Grid behind data
    return ax


def style_ticks(ax, direction="out", length=4):
    """Adjust tick style."""
    ax.tick_params(axis="both", direction=direction, length=length)
    return ax
