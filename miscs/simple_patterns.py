#!/usr/bin/env python3

# This file is to generate outputs for simple patterns: snake, simple (multiple) circles

from typing import Union, List, Tuple, Iterable
import math
import logging

sim_logger = logging.getLogger("sim_logger")

sim_logger.setLevel(logging.DEBUG)
sim_logger_fh = logging.FileHandler("sim_patterns.log")
sim_logger_formatter = logging.Formatter('%(asctime)s  %(levelname)s - %(message)s')
sim_logger_fh.setFormatter(sim_logger_formatter)
sim_logger.addHandler(sim_logger_fh)

sim_logger_ch = logging.StreamHandler()
sim_logger_ch.setFormatter(sim_logger_formatter)
sim_logger.addHandler(sim_logger_ch)


def bound_line_in_box(w: float, h: float,
        x0: float, y0: float, dir_x: float, dir_y: float,
        length_margin: float) -> Tuple[Union[None, bool], float, float]:
    """start from x0, y0 towards the direction (dir_x, dir_y), find the x1, y1 so that the distance of 
    (x0, y0) to (x1, y1) is length_margin if positive, or distance of (x1, y1) to canvas boundary is -length_margin 
    if negative, unless it reaches the boundary before then (x1, y1) is the point on boundary"""
    # length_margin: positive for length, negative for margin to boundary
    # make sure x0, y0 is in the box
    assert( 0 <= x0 <= w and 0 <= y0 <= h)
    # check possible boundary points
    # make sure dir_x, dir_y is valid
    assert( not (dir_x == 0 and dir_y == 0) )
    
    bound_x, bound_y = 0, 0

    # conditions for checking cross with right edge
    if x0 != w and dir_x > 0 and \
        ( (dir_y >= 0 and dir_y / dir_x <= (h-y0) / (w-x0)) or \
          (dir_y < 0 and -dir_y / dir_x <= y0 / (w-x0)) ):
        # cross with right edge
        bound_x = w
        bound_y = dir_y / dir_x * (w-x0) + y0 
    elif x0 != 0 and dir_x < 0 and \
        ( (dir_y >= 0 and dir_y / -dir_x <= (h-y0) / x0) or \
          (dir_y < 0 and dir_y / dir_x <= y0 / x0 ) ):
        # cross with left edge
        bound_x = 0 
        bound_y = dir_y / -dir_x * x0 + y0
    elif y0 != h and dir_y > 0 and \
        ( (dir_x >= 0 and dir_x / dir_y <= (w-x0) / (h-y0)) or \
          (dir_x < 0 and -dir_x / dir_y <= x0 / (h-y0)) ):
        # cross with top edge
        bound_y = h
        bound_x = dir_x / dir_y * (h-y0) + x0
    elif y0 != 0 and dir_y < 0 and \
        ( (dir_x >= 0 and dir_x / -dir_y <= (w-x0) / y0) or \
          (dir_x < 0 and dir_x / dir_y <= x0 / y0) ):
        # cross with bottom edge
        bound_y = 0
        bound_x = dir_x / -dir_y * y0 + x0
    else:
        # impossible to bound 
        return None, -x0, -y0

    bound_dist = math.sqrt((x0 - bound_x) ** 2 + (y0 - bound_y) ** 2)
    dir_dist = math.sqrt(dir_x ** 2 + dir_y ** 2)
    if length_margin > 0:
        if bound_dist >= length_margin:
            # clip to length
            okay_x = x0 + dir_x / dir_dist * length_margin
            okay_y = y0 + dir_y / dir_dist * length_margin
            return False, okay_x, okay_y
        else:
            return True, bound_x, bound_y # clipped
    else:
        a_length = bound_dist + length_margin
        if a_length <= 0:
            # can't satisfy the margin, stop
            return None, -x0, -y0
        else:
            okay_x = x0 + dir_x / dir_dist * a_length
            okay_y = y0 + dir_y / dir_dist * a_length
            return False, okay_x, okay_y


def rotate_point(x: float, y: float, degree: float) -> Tuple[float, float]:
    # ccw -> positive, cw -> negative
    angle = degree / 180.0 * math.pi
    r_x = math.cos(angle) * x - math.sin(angle) * y
    r_y = math.sin(angle) * x + math.cos(angle) * y
    return r_x, r_y


def gen_points_snake(canvas_width: float, canvas_height: float,
        start_x: float, start_y: float, start_dir_x: float, start_dir_y: float,
        snake_angles: Iterable[float] = (90, -90), snake_angle_indvi: bool = False,
        line_dists: Union[float, Iterable[float]] = 1.0, wrap_line_dists : bool = False,
        line_lengths_margins: Union[float, Iterable[float]] = 0.0, wrap_line_lengths_margins: bool = False):
    # ref to pattern_snake.png in the folder.
    # canvas always anchored at (0.0, 0.0) and goes to (canvas_width, canvas_height) must be positive (first quadrant)
    # shift / rotate of canvas can be done afterwards using transform matrix
    # e.g. shift due to origin of canvas bound to fixed margin
    seg_idx = 0
    dir_x, dir_y = start_dir_x, start_dir_y
    curr_x, curr_y = start_x, start_y
    acc_degree = 0

    if len(snake_angles) == 0:
        raise ValueError(f"snake_angles can't be empty")

    if type(line_lengths_margins) in (list, tuple):
        if len(line_lengths_margins) == 0:
            raise ValueError(f"line_lengths_margins can't be an empty list")

    if type(line_dists) is (list, tuple):
        if len(line_dists) == 0:
            raise ValueError(f"line_dists can't be an empty list")

    sim_logger.debug(f"snake starts at ({curr_x:.2f}, {curr_y:.2f})")
    while True:
        if type(line_lengths_margins) in (list, tuple):
            if len(line_lengths_margins) <= seg_idx and not wrap_line_lengths_margins:
                sim_logger.warning(f"length of line_lengths_margins {len(line_lengths_margins)} is shorter than "
                        f"current segment index {seg_idx}, using last one {line_lengths_margins[-1]} as replacement")
                line_length_margin = line_lengths_margins[-1]
            else:
                line_length_margin = line_length_margin[seg_idx % len(line_lengths_margins)]
                sim_logger.debug(f"for segment {seg_idx} using line_length_margin {line_length_margin}")
        else:
            line_length_margin = line_lengths_margins

        if type(line_dists) is (list, tuple):
            if len(line_dists) <= seg_idx and not wrap_line_dists:
                sim_logger.warning(f"length of line_dists {len(line_dists)} is shorter than "
                        f"current segment index {seg_idx}, using last one {line_dists[-1]} as replacement")
                line_dist = line_dists[-1]
            else:
                line_dist = line_dists[seg_idx % len(line_dists)]
                sim_logger.debug(f"for segment {seg_idx} using line_dist {line_dist}")
        else:
            line_dist = line_dists

        bound, next_x, next_y = bound_line_in_box(canvas_width, canvas_height, curr_x, curr_y, dir_x, dir_y, line_length_margin)
        if bound is None:
            # Can't go on, break now
            sim_logger.info(f"snake can't go on, stopping at ({curr_x:.2f}, {curr_y:.2f})")
            break
        else:
            sim_logger.debug(f"snake goes to ({next_x:.2f}, {next_y:.2f}){':boop!' if bound else ''}")
            curr_x, curr_y = next_x, next_y

        yield (curr_x, curr_y)

        if snake_angle_indvi:
            acc_degree += snake_angles[(seg_idx*2) % len(snake_angles)]
        else:
            acc_degree += snake_angles[seg_idx % len(snake_angles)]
        # use acc_degree and do rotate on start_dir MAY be better than doing rotation over rotation for precision issue
        # WARNING: can't % 360 and degree could be negative and %360 will generate wrong degree
        if acc_degree > 360:
            acc_degree -= 360
        elif acc_degree < -360:
            acc_degree += 360

        dir_x, dir_y = rotate_point(start_dir_x, start_dir_y, acc_degree)
        sim_logger.debug(f"snake turns as ({dir_x:.2f}, {dir_y:.2f}) - {acc_degree:.2f}")
        bound, next_x, next_y = bound_line_in_box(canvas_width, canvas_height, curr_x, curr_y, dir_x, dir_y, line_dist)

        if bound is None:
            # Can't go on, break now
            sim_logger.info(f"snake can't go on, stopping at ({curr_x:.2f}, {curr_y:.2f})")
            break
        else:
            if bound:
                # dist line, must not be clipped
                sim_logger.info(f"snake turn seg must be satisfied, stopping at ({curr_x:.2f}, {curr_y:.2f})")
                # FIXME: This can be optimized/fixed/resolved by back the previous line a bit, but requires more calculation
                #   may not be worth to do it anyway
                # This will happen if the direction is not horizontal or vertical
                break
            sim_logger.debug(f"snake goes to ({next_x:.2f}, {next_y:.2f}){':boop!' if bound else ''}")
            curr_x, curr_y = next_x, next_y

        yield (curr_x, curr_y)

        if snake_angle_indvi:
            acc_degree += snake_angles[(seg_idx*2+1) % len(snake_angles)] 
        else:
            acc_degree += snake_angles[seg_idx % len(snake_angles)] 
        if acc_degree > 360:
            acc_degree -= 360
        elif acc_degree < -360:
            acc_degree += 360

        dir_x, dir_y = rotate_point(start_dir_x, start_dir_y, acc_degree)
        sim_logger.debug(f"snake turns as ({dir_x:.2f}, {dir_y:.2f}) - {acc_degree:.2f}")
        seg_idx += 1


def gen_circle_from_point(canvas_width: float, canvas_height: float,
        center_x: float, center_y: float, start_x: float, start_y: float,
        step_degree: float, cover_degree: float = 360, min_step: float = 0):
    radius = math.sqrt( (start_x - center_x)**2 + (start_y - center_y)**2 )
    step_dist = math.sin(step_degree/360 * math.pi) * radius * 2
    if step_dist < min_step:
        step_degree = math.asin(min_step/2/radius) / pi *360
        sim_logger.warning(f"can't move a distance of {step_dist:.2f} < {min_step:.2f}, adjusting step_degree to {step_degree:.2f}")

    curr_x, curr_y = start_x, start_y
    curr_degree = math.asin((start_y - center_y) / radius) / math.pi * 180
    if start_x < center_x:
        if curr_degree >= 0:
            curr_degree = 180 - curr_degree
        else:
            curr_degree = -180 - curr_degree

    sim_logger.info(f"circle starts at {curr_degree:.2f} at ({curr_x:.2f}, {curr_y:.2f})")

    acc_degree = 0

    while True:
        degree_left = abs(cover_degree) - acc_degree
        if degree_left < step_degree:
            raise ValueError(f"can't move even smaller than adjusted degree {step_degree:.2f}")
        elif step_degree < degree_left < 2*step_degree:
            move_degree = degree_left if step_degree > 0 else -degree_left
            sim_logger.warning(f"circle goes by {move_degree:.2f} towards finish, instead of {step_degree:.2f}")
        else:
            move_degree = step_degree
        n_x, n_y = rotate_point(curr_x - center_x, curr_y - center_y, move_degree)
        n_x += center_x
        n_y += center_y
        acc_degree += abs(move_degree)
        curr_degree += move_degree
        sim_logger.debug(f"circle going by {move_degree if step_degree > 0 else -move_degree:.2f} degree to "
                f"({n_x:.2f}, {n_y:.2f}), now at {curr_degree:.2f}")
        if 0 <= n_x <= canvas_width and 0 <= n_y <= canvas_height:
            yield (n_x, n_y, curr_degree)
            curr_x, curr_y = n_x, n_y
        else: 
            sim_logger.info(f"circle going outside canvas ({n_x:.2f}, {n_y:.2f}), stopping at ({curr_x:.2f}, {curr_y:.2f})")
            break
        if acc_degree >= cover_degree:
            return curr_x, curr_y, curr_degree


def gen_circle_from_radius(canvas_width: float, canvas_height: float,
        center_x: float, center_y: float, radius: float, start_degree: float,
        step_degree: float, cover_degree: float = 360, min_step: float = 0):
    start_x = center_x + radius * math.cos(start_degree/180*math.pi)
    start_y = center_y + radius * math.sin(start_degree/180*math.pi)
    yield (start_x, start_y, start_degree)
    res = yield from gen_circle_from_point(canvas_width, canvas_height, center_x, center_y, start_x, start_y, step_degree, cover_degree, min_step)
    return res


def gen_circle_from_degree(canvas_width: float, canvas_height: float,
        radius: float, start_x: float, start_y: float, start_degree: float,
        step_degree: float, cover_degree: float = 360, min_step: float = 0):
    center_x = start_x - radius * math.cos(start_degree/180*math.pi)
    center_y = start_y - radius * math.sin(start_degree/180*math.pi)
    res = yield from gen_circle_from_point(canvas_width, canvas_height, center_x, center_y, start_x, start_y, step_degree, cover_degree, min_step)
    return res


def gen_spiral(canvas_width: float, canvas_height: float,
        start_x: float, start_y: float, start_radius: float, radius_steps: Union[float, Iterable[float]],
        start_degree: float, step_degree: float, cover_degrees: Union[float, Iterable[float]] = 180, min_step: float = 0):
    if type(cover_degrees) in (list, tuple):
        if len(cover_degrees) == 0:
            raise ValueError(f"cover_degrees can't be empty")

    if type(radius_steps) in (list, tuple):
        if len(radius_steps) == 0:
            raise ValueError(f"radius_steps can't be empty")

    circle_idx = 0
    circle_radius = start_radius
    circle_startdegree = start_degree
    circle_start_x, circle_start_y = start_x, start_y

    while True:
        if type(cover_degrees) in (list, tuple):
            if len(cover_degrees) <= circle_idx:
                break
            else:
                circle_coverdegree = cover_degress[circle_idx]
        else:
            circle_coverdegree = cover_degrees

        try:
            res_gen = yield from gen_circle_from_degree(canvas_width, canvas_height, 
                     circle_radius, circle_start_x, circle_start_y, circle_startdegree, step_degree, circle_coverdegree, min_step)
            if res_gen is None:
                # circle gen stopped due to out of canvas
                break
            curr_x, curr_y, curr_degree = res_gen
            circle_startdegree = curr_degree
            circle_start_x, circle_start_y = curr_x, curr_y
            if type(radius_steps) in (list, tuple):
                if len(radius_steps) <= circle_idx:
                    break
                else:
                    circle_radius += radius_steps[circle_idx]
            else:
                circle_radius += radius_steps

            circle_idx += 1
        except StopIteration:
            pass


# TODO: multiple circles are different
def dump_pattern_to_file():
    pass


if __name__ == "__main__":
    # test with matplotlib visualization
    import matplotlib.pyplot as plt
    import numpy as np

    #p_x, p_y = 200, 0
    #points_gen = gen_points_snake(1000, 1000, 
    #        p_x, p_y, -0.5, 0.5, 
    #        (-90, 90), False, 
    #        20, False, 
    #        -40, False)

    #p_x, p_y = None, None
    #points_gen = gen_circle_from_radius(1000, 1000, 600, 400, 300, 90, 1, 270)

    p_x, p_y = 500, 400
    points_gen = gen_spiral(1000, 1000, p_x, p_y, 50, 50, 90, 30, 180)

    fig, fig_ax = plt.subplots() 
    fig_ax.set_xlim(left=-1, right=1001)
    fig_ax.set_ylim(bottom=-1, top=1001)
    fig_ax.set_aspect(1)
    
    while True:
        try:
            n_x, n_y = next(points_gen)[:2]
            if p_x is not None:
                fig_ax.plot( (p_x, n_x), (p_y, n_y), '-')
            plt.pause(0.5)
            p_x, p_y = n_x, n_y
        except StopIteration:
            break

    plt.show()

