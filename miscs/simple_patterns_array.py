#!/usr/bin/env python3

# This file is to generate outputs for simple patterns: snake, simple (multiple) circles

from typing import Union, List, Tuple, Iterable, Iterator, TextIO
import math
import logging
import numpy as np
import numpy.typing as npt

sim_logger = logging.getLogger("sim_logger")

sim_logger.setLevel(logging.INFO)
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
   
    float_eps = 1e-12
    bound_x, bound_y = 0, 0
    # conditions for checking cross with right edge
    if x0 != w and dir_x > 0 and \
        ( (dir_y >= 0 and dir_y / dir_x <= (h-y0) / (w-x0) + float_eps) or \
          (dir_y < 0 and -dir_y / dir_x <= y0 / (w-x0) + float_eps) ):
        # cross with right edge
        bound_x = w
        bound_y = dir_y / dir_x * (w-x0) + y0 
    elif x0 != 0 and dir_x < 0 and \
        ( (dir_y >= 0 and dir_y / -dir_x <= (h-y0) / x0 + float_eps) or \
          (dir_y < 0 and dir_y / dir_x <= y0 / x0  + float_eps) ):
        # cross with left edge
        bound_x = 0 
        bound_y = dir_y / -dir_x * x0 + y0
    elif y0 != h and dir_y > 0 and \
        ( (dir_x >= 0 and dir_x / dir_y <= (w-x0) / (h-y0) + float_eps) or \
          (dir_x < 0 and -dir_x / dir_y <= x0 / (h-y0) + float_eps) ):
        # cross with top edge
        bound_y = h
        bound_x = dir_x / dir_y * (h-y0) + x0
    elif y0 != 0 and dir_y < 0 and \
        ( (dir_x >= 0 and dir_x / -dir_y <= (w-x0) / y0 + float_eps) or \
          (dir_x < 0 and dir_x / dir_y <= x0 / y0 + float_eps) ):
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


def gen_points_snake(canvas_size: Iterable[float], start_pt: Iterable[float], start_dir: Iterable[float],
        angles_it: Iterator[float], dist_it: Iterator[float], len_margins_it: Iterator[float]):
    # ref to pattern_snake.png in the folder.
    # canvas always anchored at (0.0, 0.0) and goes to (canvas_width, canvas_height) must be positive (first quadrant)
    # shift / rotate of canvas can be done afterwards using transform matrix
    # e.g. shift due to origin of canvas bound to fixed margin

    # unpacking parameters
    canvas_width, canvas_height = canvas_size
    start_x, start_y = start_pt
    start_dir_x, start_dir_y = start_dir

    seg_idx = 0
    dir_x, dir_y = start_dir_x, start_dir_y
    curr_x, curr_y = start_x, start_y
    acc_degree = 0

    sim_logger.debug(f"snake starts at ({curr_x:.4f}, {curr_y:.4f})")
    while True:
        len_margin = next(len_margins_it)
        dist =  next(dist_it)

        sim_logger.debug(f"trying to bound in box from ({curr_x:.4f}, {curr_y:.4f}) in "
                f"direction ({dir_x:.4f}, {dir_y:.4f}) with len_margin {len_margin:.4f}")
        bound, next_x, next_y = bound_line_in_box(canvas_width, canvas_height, curr_x, curr_y, dir_x, dir_y, len_margin)

        if bound is None:
            # Can't go on, break now
            sim_logger.info(f"snake can't go on, stopping at ({curr_x:.4f}, {curr_y:.4f})")
            break
        else:
            sim_logger.debug(f"snake goes to ({next_x:.4f}, {next_y:.4f}){':boop!' if bound else ''}")
            curr_x, curr_y = next_x, next_y

        yield (curr_x, curr_y, seg_idx)

        acc_degree += next(angles_it)

        # use acc_degree and do rotate on start_dir MAY be better than doing rotation over rotation for precision issue
        # WARNING: can't % 360 and degree could be negative and %360 will generate wrong degree
        if acc_degree > 360:
            acc_degree -= 360
        elif acc_degree < -360:
            acc_degree += 360

        dir_x, dir_y = rotate_point(start_dir_x, start_dir_y, acc_degree)
        sim_logger.debug(f"snake turns as ({dir_x:.4f}, {dir_y:.4f}) - {acc_degree:.4f}")
        sim_logger.debug(f"trying to bound in box from ({curr_x:.4f}, {curr_y:.4f}) "
                f"in direction ({dir_x:.4f}, {dir_y:.4f}) with len_margin {dist:.4f}")
        bound, next_x, next_y = bound_line_in_box(canvas_width, canvas_height, curr_x, curr_y, dir_x, dir_y, dist)

        if bound is None:
            # Can't go on, break now
            sim_logger.info(f"snake can't go on, stopping at ({curr_x:.4f}, {curr_y:.4f})")
            break
        else:
            if bound:
                # dist line, must not be clipped
                sim_logger.info(f"snake turn seg must be satisfied, stopping at ({curr_x:.4f}, {curr_y:.4f})")
                # FIXME: This can be optimized/fixed/resolved by back the previous line a bit, but requires more calculation
                #   may not be worth to do it anyway
                # This will happen if the direction is not horizontal or vertical
                break
            sim_logger.debug(f"snake goes to ({next_x:.4f}, {next_y:.4f}){':boop!' if bound else ''}")
            curr_x, curr_y = next_x, next_y

        yield (curr_x, curr_y, seg_idx)

        acc_degree += next(angles_it)
        if acc_degree > 360:
            acc_degree -= 360
        elif acc_degree < -360:
            acc_degree += 360

        dir_x, dir_y = rotate_point(start_dir_x, start_dir_y, acc_degree)
        sim_logger.debug(f"snake turns as ({dir_x:.4f}, {dir_y:.4f}) - {acc_degree:.4f}")
        seg_idx += 1


def gen_circle_from_point(canvas_size: Iterable[float], center_pt: Iterable[float], start_pt: Iterable[float], 
        step_degree: float, cover_degree: float = 360, min_step: float = 0, distri_leftover_degree: bool = False):
    assert(cover_degree > 0)
    canvas_width, canvas_height = canvas_size
    center_x, center_y = center_pt
    start_x, start_y = start_pt

    radius = math.sqrt( (start_x - center_x)**2 + (start_y - center_y)**2 )
    step_dist = math.sin(step_degree/360 * math.pi) * radius * 2
    min_degree = math.asin(abs(min_step)/2/radius) / math.pi *360

    if abs(step_dist) < min_step:
        n_steps = int(cover_degree/min_degree)
        step_degree = (-cover_degree if step_degree < 0 else cover_degree)/n_steps
        # adjust to even it out
        sim_logger.warning(f"can't move a distance of {abs(step_dist):.4f} < {min_step:.4f}, "
                f"adjusting step_degree to {step_degree:.4f}")

    step_degree_abs = abs(step_degree)

    if distri_leftover_degree:
        degree_leftover = cover_degree - int(cover_degree / step_degree_abs) * step_degree_abs
        if degree_leftover > 1e-12:
            # we have leftover, distribute it by increasing the step_degree
            n_steps = int(cover_degree / step_degree_abs)
            if cover_degree / (n_steps + 1) + 1e-12 >= min_degree:
                n_steps += 1
            step_degree = (-cover_degree if step_degree < 0 else cover_degree)/n_steps
            step_degree_abs = abs(step_degree)
            sim_logger.warning(f"to distribute last leftover degree, adjusting step_degree to {step_degree:.4f}")


    curr_x, curr_y = start_x, start_y
    curr_degree = math.asin((start_y - center_y) / radius) / math.pi * 180
    if start_x < center_x:
        if curr_degree >= 0:
            curr_degree = 180 - curr_degree
        else:
            curr_degree = -180 - curr_degree

    sim_logger.info(f"circle starts at {curr_degree:.4f} at ({curr_x:.4f}, {curr_y:.4f})")

    acc_degree = 0

    while True:
        degree_left = cover_degree - acc_degree
        if degree_left < step_degree_abs + 1e-9:
            leftover_dist = radius * 2 * math.sin(degree_left / 360 * math.pi)
            if leftover_dist < min_step:
                raise ValueError(f"can't move even smaller than adjusted degree {step_degree:.4f}")
            else:
                move_degree = degree_left if step_degree > 0 else -degree_left
        elif step_degree_abs < degree_left < 2*step_degree_abs:
            leftover_dist = radius * 2 * math.sin( (degree_left - step_degree_abs) / 360 * math.pi)
            if leftover_dist < min_step:
                move_degree = degree_left if step_degree > 0 else -degree_left
                sim_logger.warning(f"circle goes by {move_degree:.4f} towards finish, instead of {step_degree:.4f}, "
                        f"diff {move_degree - step_degree}")
            else:
                # it is okay to leave the leftover as it is
                move_degree = step_degree
        else:
            move_degree = step_degree
        n_x, n_y = rotate_point(curr_x - center_x, curr_y - center_y, move_degree)
        n_x += center_x
        n_y += center_y
        acc_degree += abs(move_degree)
        curr_degree += move_degree
        sim_logger.debug(f"circle going by {move_degree if step_degree > 0 else -move_degree:.4f} degree to "
                f"({n_x:.4f}, {n_y:.4f}), now at {curr_degree:.4f}")
        if 0 <= n_x <= canvas_width and 0 <= n_y <= canvas_height:
            yield (n_x, n_y, curr_degree)
            curr_x, curr_y = n_x, n_y
        else: 
            sim_logger.info(f"circle going outside canvas ({n_x:.4f}, {n_y:.4f}), stopping at ({curr_x:.4f}, {curr_y:.4f})")
            break
        # 1e-12 is added as eps to allow float point calculation error margin
        if acc_degree + 1e-12 >= cover_degree:
            return curr_x, curr_y, curr_degree


def gen_circle_from_radius(canvas_size: Iterable[float], center_pt: Iterable[float], radius: float, start_degree: float, 
        step_degree: float, cover_degree: float = 360, min_step: float = 0, distri_leftover_degree: bool = False):
    center_x, center_y = center_pt
    start_x = center_x + radius * math.cos(start_degree/180*math.pi)
    start_y = center_y + radius * math.sin(start_degree/180*math.pi)
    yield (start_x, start_y, start_degree)
    res = yield from gen_circle_from_point(canvas_size, center_pt, (start_x, start_y), step_degree, 
            cover_degree, min_step, distri_leftover_degree)
    return res


def gen_circle_from_degree(canvas_size: Iterable[float], start_pt: Iterable[float], radius: float, start_degree: float, 
        step_degree: float, cover_degree: float = 360, min_step: float = 0, distri_leftover_degree: bool = False):
    start_x, start_y = start_pt
    center_x = start_x - radius * math.cos(start_degree/180*math.pi)
    center_y = start_y - radius * math.sin(start_degree/180*math.pi)
    sim_logger.debug(f"gen_circle_from_degree ({start_x:.4f}, {start_y:.4f}), start_degree {start_degree:.4f}, "
            f"radius {radius:.4f}, center at ({center_x:.4f}, {center_y:.4f})") 

    res = yield from gen_circle_from_point(canvas_size, (center_x, center_y), start_pt, step_degree, 
            cover_degree, min_step, distri_leftover_degree)
    return res


def gen_spiral(canvas_size: Iterable[float], start_pt: Iterable[float], radius_it: Iterator[float], 
        start_degree: float, step_degree: float, cover_degree_it: Iterator[float], min_step: float = 0):
    circle_idx = 0
    circle_radius = next(radius_it)
    circle_startdegree = start_degree
    circle_start_x, circle_start_y = start_pt

    while True:
        circle_coverdegree = next(cover_degree_it)

        try:
            res_gen = yield from gen_circle_from_degree(canvas_size, (circle_start_x, circle_start_y), 
                    circle_radius, circle_startdegree, step_degree, circle_coverdegree, min_step)
            if res_gen is None:
                # circle gen stopped due to out of canvas
                break
            curr_x, curr_y, curr_degree = res_gen
            circle_startdegree = curr_degree
            circle_start_x, circle_start_y = curr_x, curr_y
            circle_radius = next(radius_it)
            circle_idx += 1
        except StopIteration:
            pass


# TODO: multiple circles are different
def dump_pattern_to_file(points_gen: Iterator[Tuple[float]], offset_v: Iterable[float], f_output: TextIO, first_is_start: bool):
    offset_x, offset_y = offset_v[:2]
    ja_to_start=False
    while True:
        try:
            pt_x, pt_y, extra_info = next(points_gen)
            if type(extra_info) is float:
                extra_s = f"{extra_info:.4f}"
            else:
                extra_s = f"{extra_info}"

            if first_is_start and not ja_to_start:
                print('#include "DrawInactive.txt"', file=f_output)
                print(f"ja ( {pt_x+offset_x:.4f}, {pt_y+offset_y:.4f} ); // {extra_s} ", file=f_output)
                print('#include "DrawActive.txt"', file=f_output)
                print('MovingSpeed (1); // <----- YOU MAY WANT TO CHANGE THIS', file=f_output)
                ja_to_start=True
            else:
                print(f"ma ( {pt_x+offset_x:.4f}, {pt_y+offset_y:.4f} ); // {extra_s} ", file=f_output)
        except StopIteration:
            break


if __name__ == "__main__":
    # test with matplotlib visualization
    import matplotlib.pyplot as plt
    import numpy as np
    from random import random
    from itertools import cycle, repeat

    canvas_s = (30, 30)  # 30 um * 30 um canvas
    snake_head = (0, 0)
    snake_first_goes = (1, 0)

    canvas_offsets = (-20, -20)
    points_gen = gen_points_snake(canvas_s, snake_head, snake_first_goes, cycle([90, 90, -90, -90]), repeat(1), repeat(30))
    with open("./snake_30x30_d1.txt", "w") as f_snake:
        print('#include "DrawInactive.txt"', file=f_snake)
        # jump to snake starting point
        print(f'ja ( {snake_head[0] + canvas_offsets[0]:.4f}, {snake_head[1] + canvas_offsets[1]:.4f} );', file=f_snake)
        print('#include "DrawActive.txt"', file=f_snake)
        print('MovingSpeed (4);', file=f_snake)
        # for snake pattern the first point generated is not the start_point
        dump_pattern_to_file(points_gen, canvas_offsets, f_snake, False)

    #p_x, p_y = 500, 400

    #def radius_gen_spiral() -> Iterator[float]:
    #    r_idx = 1
    #    radius = 50
    #    while True:
    #        yield radius
    #        radius += (random()+0.1) * 20
    #        r_idx += 1

    #def cover_degree_gen_spiral() -> Iterator[float]:
    #    r_idx = 1
    #    while True:
    #        yield 60
    #        r_idx += 1

    p_x, p_y = snake_head
    points_gen = gen_points_snake(canvas_s, snake_head, snake_first_goes, cycle([90, 90, -90, -90]), repeat(2), repeat(30))
    # points_gen = gen_spiral(canvas_s, (p_x, p_y), radius_gen_spiral(), 0, 10, cover_degree_gen_spiral(), 0)
    p_x = None # avoid plotting the first center to start_pt

    fig, fig_ax = plt.subplots() 
    fig_ax.set_xlim(left=-1, right=canvas_s[0]+1)
    fig_ax.set_ylim(bottom=-1, top=canvas_s[1]+1)
    fig_ax.set_aspect(1)

    while True:
        try:
            n_x, n_y = next(points_gen)[:2]
            if p_x is not None:
                fig_ax.plot( (p_x, n_x), (p_y, n_y), '-')
            plt.pause(0.1)
            p_x, p_y = n_x, n_y
        except StopIteration:
            break

    plt.pause(3)

    fig_ax.clear()
    fig_ax.set_xlim(left=-1, right=canvas_s[0]+1)
    fig_ax.set_ylim(bottom=-1, top=canvas_s[1]+1)
    fig_ax.set_aspect(1)
    row=[5,10,15,20,25]
    columns=[5,10,15,20,25]
    with open("./circles_30x30_15_15_r0.05_m1.txt", "w") as f_circles:
        for i in row:
            for j in columns:
                circle_center=(i, j)
                points_gen = gen_circle_from_radius(canvas_s, circle_center, radius=0.1, start_degree=0, step_degree=1, cover_degree=360, min_step=0.05)
                dump_pattern_to_file(points_gen, canvas_offsets, f_circles, True)

                #points_gen = gen_circle_from_radius(canvas_s, circle_center, radius=5, start_degree=0, step_degree=10, cover_degree=360, min_step=0.01)
                #p_x = None
                #while True:
                #    try:
                #        n_x, n_y = next(points_gen)[:2]
                #        if p_x is not None:
                #            fig_ax.plot( (p_x, n_x), (p_y, n_y), '-')
                #        plt.pause(0.01)
                #        p_x, p_y = n_x, n_y
                #    except StopIteration:
                #        break

                #plt.pause(1)

                # points_gen = gen_circle_from_radius(canvas_s, circle_center, radius=0.1, start_degree=0, step_degree=-13, cover_degree=360, min_step=36)
                # dump_pattern_to_file(points_gen, canvas_offsets, f_circles, True)

                points_gen = gen_circle_from_radius(canvas_s, circle_center, radius=0.1, start_degree=0, step_degree=1, cover_degree=360, min_step=0.05)
                p_x = None
                while True:
                    try:
                        n_x, n_y = next(points_gen)[:2]
                        if p_x is not None:
                            fig_ax.plot( (p_x, n_x), (p_y, n_y), '-')
                        plt.pause(0.01)
                        p_x, p_y = n_x, n_y
                    except StopIteration:
                        break

                plt.pause(1)

        # points_gen = gen_circle_from_radius(canvas_s, circle_center, radius=8, start_degree=0, step_degree=-13, cover_degree=360, min_step=1.3, distri_leftover_degree=True)
        # dump_pattern_to_file(points_gen, canvas_offsets, f_circles, True)

        # points_gen = gen_circle_from_radius(canvas_s, circle_center, radius=8, start_degree=0, step_degree=-13, cover_degree=360, min_step=1.3, distri_leftover_degree=True)
        # p_x = None
        # while True:
        #     try:
        #         n_x, n_y = next(points_gen)[:2]
        #         if p_x is not None:
        #             fig_ax.plot( (p_x, n_x), (p_y, n_y), '-')
        #         plt.pause(0.01)
        #         p_x, p_y = n_x, n_y
        #     except StopIteration:
        #         break

        # plt.pause(1)
