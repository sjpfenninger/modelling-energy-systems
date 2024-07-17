import matplotlib.pyplot as plt

SAVETO_KWARGS = dict(
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.5,
)


def plot_function(x, f, axis=None, **plot_specs):
    if axis is None:
        axis = plt.gca()

    line = axis.plot(x, f(x), **plot_specs)
    return line[0]


def plot_x_range(x_min, x_max, axis=None, **plot_specs):
    if axis is None:
        axis = plt.gca()

    lower_x_range = axis.axvline(x_min, **plot_specs)
    upper_x_range = axis.axvline(x_max, **plot_specs)
    return lower_x_range, upper_x_range


def plot_y_range(y_min, y_max, axis=None, **plot_specs):
    if axis is None:
        axis = plt.gca()

    lower_y_range = axis.axhline(y_min, **plot_specs)
    upper_y_range = axis.axhline(y_max, **plot_specs)
    return lower_y_range, upper_y_range


def find_intersection(line1, line2):
    """
    Find the intersection point of two lines specified by their slopes and y-intercepts.

    Parameters:
        line1 (tuple): Tuple containing the slope and y-intercept of the first line.
        line2 (tuple): Tuple containing the slope and y-intercept of the second line.

    Returns:
        tuple: Intersection point as a tuple (x, y).
    """
    # Extract slope and y-intercept from the input tuples
    m1, c1 = line1
    m2, c2 = line2

    # Check if line1 has infinite slope
    if m1 == float("inf"):
        x = c1
        y = m2 * x + c2
    # Check if line2 has infinite slope
    elif m2 == float("inf"):
        x = c2
        y = m1 * x + c1
    else:
        # Calculate x-coordinate of intersection point
        x = (c2 - c1) / (m1 - m2)

        # Calculate y-coordinate of intersection point
        y = m1 * x + c1

    return x, y


def draw_line_segment(
    point1, point2, axis=None, color="grey", line_weight=5, dot_size=10, **line_specs
):
    if axis is None:
        axis = plt.gca()

    x1, y1 = point1
    x2, y2 = point2

    axis.plot([x1, x2], [y1, y2], color=color, linewidth=line_weight, **line_specs)

    axis.plot(x1, y1, "o", color=color, markersize=dot_size)
    axis.plot(x2, y2, "o", color=color, markersize=dot_size)


def repeat_line(
    x,
    f,
    obj_val,
    ax,
    num_copies,
    offset_distance,
    arrow_length=100,
    labels=True,
    **kwargs
):
    """
    Plot parallel lines to a given function at constant offsets in both directions on a specified axis.

    """

    annotation_fontstyle = {
        "family": "serif",
        "color": "black",
        "weight": "normal",
        "size": 14,
        "ha": "center",
        "va": "center",
    }

    # Calculate the slope of the original line
    x_mid = (x[0] + x[-1]) / 2
    slope = (f(x[-1]) - f(x[0])) / (x[-1] - x[0])

    # Plot the original line
    ax.plot(x, f(x), **kwargs)
    if labels:
        ax.text(
            1.1 * x[-1],
            f(x[-1]),
            "$J = $" + str(int(obj_val(x[-1], f(x[-1])))),
            fontdict=annotation_fontstyle,
        )

    # Plot parallel lines on the positive side
    for i in range(1, num_copies + 1):
        offset = i * offset_distance
        ax.plot(x, f(x) + offset, **kwargs)
        if i == 1 and labels:
            ax.text(
                1.1 * x[-1],
                f(x[-1]) + offset,
                "$J = $" + str(int(obj_val(x[-1], f(x[-1]) + offset))),
                fontdict=annotation_fontstyle,
            )

    # Plot parallel lines on the negative side
    for i in range(1, num_copies + 1):
        offset = i * offset_distance
        ax.plot(x, f(x) - offset, **kwargs)
        if i == 1 and labels:
            ax.text(
                1.1 * x[-1],
                f(x[-1]) - offset,
                "$J = $" + str(int(obj_val(x[-1], f(x[-1]) - offset))),
                fontdict=annotation_fontstyle,
            )

    # Calculate perpendicular slopes
    perpendicular_slope = -1 / slope

    # Calculate points for arrows
    x1 = x_mid + arrow_length / 2
    y1 = f(x_mid) + offset + perpendicular_slope * arrow_length / 2
    x1_text = x_mid
    y1_text = f(x_mid) + offset

    x2_text, y2_text = find_intersection(
        (slope, f(0) - offset),
        (perpendicular_slope, f(x_mid) + offset - perpendicular_slope * x_mid),
    )
    x2 = x2_text - arrow_length / 2
    y2 = f(x2_text) - offset - perpendicular_slope * arrow_length / 2

    # Draw arrows
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x1_text, y1_text),
        arrowprops=dict(
            facecolor="black",
            linewidth=0.5,
            headwidth=10,
            headlength=10,
            mutation_scale=10,
            shrink=0.1,
        ),
    )

    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x2_text, y2_text),
        arrowprops=dict(
            facecolor="black",
            linewidth=0.5,
            headwidth=10,
            headlength=10,
            mutation_scale=10,
            shrink=0.1,
        ),
    )

    return (x1, y1), (x2, y2)
