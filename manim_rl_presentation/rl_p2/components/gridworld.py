"""Gridworld primitives reused across scenes 7-10."""

from __future__ import annotations

from manim import (
    Animation,
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    RED,
    RIGHT,
    UP,
    Arrow,
    Circle,
    Create,
    FadeIn,
    MoveAlongPath,
    Square,
    VMobject,
    linear,
    Succession,
    Text,
    VGroup,
)
import numpy as np

from ..constants import LAYOUT, PALETTE, TYPOGRAPHY


DIR_TO_VEC = {
    "U": UP,
    "D": DOWN,
    "L": LEFT,
    "R": RIGHT,
}


class GridWorld(VGroup):
    """A compact and reusable gridworld with cell, marker, and movement helpers."""

    def __init__(self, rows: int = 4, cols: int = 4, cell_size: float = LAYOUT.grid_cell_size):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cells = {}
        self.markers = VGroup()
        self.overlay = VGroup()
        self.agent = None

        grid = VGroup()
        for r in range(rows):
            for c in range(cols):
                sq = Square(side_length=cell_size)
                sq.set_stroke(PALETTE.text_muted, width=1.2)
                sq.set_fill("#1C212B", opacity=0.55)
                sq.move_to(self._logical_to_pos(r, c))
                self.cells[(r, c)] = sq
                grid.add(sq)

        self.add(grid, self.markers, self.overlay)

    def _logical_to_pos(self, row: int, col: int):
        x = (col - (self.cols - 1) / 2) * self.cell_size
        y = ((self.rows - 1) / 2 - row) * self.cell_size
        return ORIGIN + x * RIGHT + y * UP

    def cell_center(self, row: int, col: int):
        return self.cells[(row, col)].get_center()

    def mark_start(self, row: int, col: int):
        tag = Text("S", font_size=TYPOGRAPHY.body_size, color=PALETTE.agent, weight="BOLD")
        tag.move_to(self.cell_center(row, col))
        self.markers.add(tag)
        return tag

    def mark_goal(self, row: int, col: int, label: str = "+1"):
        chip = Circle(radius=self.cell_size * 0.24, color=PALETTE.goal, fill_opacity=0.25)
        chip.move_to(self.cell_center(row, col))
        txt = Text(label, font_size=TYPOGRAPHY.small_size, color=PALETTE.goal, weight="BOLD").move_to(chip)
        grp = VGroup(chip, txt)
        self.markers.add(grp)
        return grp

    def mark_bad(self, row: int, col: int, label: str = "-1"):
        chip = Circle(radius=self.cell_size * 0.24, color=PALETTE.bad, fill_opacity=0.25)
        chip.move_to(self.cell_center(row, col))
        txt = Text(label, font_size=TYPOGRAPHY.small_size, color=PALETTE.bad, weight="BOLD").move_to(chip)
        grp = VGroup(chip, txt)
        self.markers.add(grp)
        return grp

    def spawn_agent(self, row: int, col: int):
        dot = Circle(radius=self.cell_size * 0.17, color=PALETTE.agent, fill_opacity=1)
        dot.move_to(self.cell_center(row, col))
        self.agent = dot
        self.overlay.add(dot)
        return dot

    def path_animation(self, path: list[tuple[int, int]], run_time_per_step: float = 0.38) -> Animation:
        """Return a Manhattan-constrained movement animation for the agent."""
        if self.agent is None:
            raise ValueError("Call spawn_agent before animating a path.")
        step_path = self._expand_to_cardinal_steps(path)
        if not step_path:
            return Succession()

        # Build a polyline that includes every intermediate grid step.
        points = [self.agent.get_center()]
        for row, col in step_path:
            p = self.cell_center(row, col)
            if np.linalg.norm(p - points[-1]) > 1e-6:
                points.append(p)

        if len(points) < 2:
            return Succession()

        path_curve = VMobject()
        path_curve.set_points_as_corners(points)
        total_time = run_time_per_step * (len(points) - 1)
        return MoveAlongPath(self.agent, path_curve, rate_func=linear, run_time=total_time)

    @staticmethod
    def _expand_to_cardinal_steps(path: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """Expand path so each move changes only one coordinate by 1 cell.

        This prevents accidental diagonal/jump motion in gridworld scenes.
        """
        if not path:
            return path

        expanded = [path[0]]
        for (r1, c1), (r2, c2) in zip(path, path[1:]):
            r, c = r1, c1

            # Move row-wise first, then column-wise.
            while r != r2:
                r += 1 if r2 > r else -1
                expanded.append((r, c))
            while c != c2:
                c += 1 if c2 > c else -1
                expanded.append((r, c))

        return expanded

    def make_action_arrows(self, row: int, col: int, q_vals: dict[str, float], precision: int = 2) -> VGroup:
        """Draw directional arrows from one state with compact Q-value labels."""
        center = self.cell_center(row, col)
        arrows = VGroup()
        for key, vec in DIR_TO_VEC.items():
            if key not in q_vals:
                continue
            start = center + vec * 0.08
            end = center + vec * (self.cell_size * 0.52)
            arr = Arrow(start=start, end=end, buff=0, stroke_width=4, max_stroke_width_to_length_ratio=12)
            arr.set_color(GREEN if q_vals[key] > 0 else (RED if q_vals[key] < 0 else BLUE))
            lbl = Text(f"{q_vals[key]:.{precision}f}", font_size=20, color=PALETTE.text_primary)
            lbl.move_to(end + vec * 0.16)
            arrows.add(arr, lbl)
        return arrows

    def flash_path(self, path: list[tuple[int, int]], color=GREEN) -> VGroup:
        """Lightly highlight cells in a path for before/after comparisons."""
        overlays = VGroup()
        for row, col in path:
            sq = self.cells[(row, col)].copy().set_fill(color, opacity=0.22).set_stroke(color, width=2)
            overlays.add(sq)
        return overlays

    def intro_animation(self):
        return Create(self)

    def markers_animation(self):
        return FadeIn(self.markers)
