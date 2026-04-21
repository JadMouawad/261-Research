"""Scene 10: Real-world RL applications."""

from pathlib import Path
import sys

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    AnimationGroup,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MoveAlongPath,
    RoundedRectangle,
    Square,
    Text,
    VMobject,
    VGroup,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from .components.headers import SceneHeader
    from .constants import PALETTE, TYPOGRAPHY
    from .scene_base import P2BaseScene
except ImportError:
    from manim_rl_presentation.rl_p2.components.headers import SceneHeader
    from manim_rl_presentation.rl_p2.constants import PALETTE, TYPOGRAPHY
    from manim_rl_presentation.rl_p2.scene_base import P2BaseScene


def build_card(title: str, accent: str) -> VGroup:
    """Create a consistent application card container."""
    panel = RoundedRectangle(width=3.9, height=3.3, corner_radius=0.14)
    panel.set_fill("#161B22", opacity=0.92).set_stroke(PALETTE.text_muted, width=1.1)
    heading = Text(title, font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary, weight="BOLD")
    heading.next_to(panel.get_top(), DOWN, buff=0.2)
    underline = Line(LEFT * 1.45, RIGHT * 1.45, color=accent, stroke_width=2).next_to(heading, DOWN, buff=0.1)
    return VGroup(panel, heading, underline)


class Scene10WarehouseApplication(P2BaseScene):
    """Shows how the same RL loop appears in multiple real domains."""

    def construct(self):
        header = SceneHeader("Real-world RL Applications", "Same learning loop, different environments")
        header.animate_in(self)
        self.wait(2.0)

        game_card = build_card("Games", "#74C0FC")
        robot_card = build_card("Robot Navigation", "#8CE99A")
        car_card = build_card("Self-driving", "#FFD43B")
        cards = VGroup(game_card, robot_card, car_card).arrange(RIGHT, buff=0.45).shift(DOWN * 0.15)

        # Games icon + motion cue.
        game_screen = RoundedRectangle(width=2.3, height=1.25, corner_radius=0.08)
        game_screen.set_stroke("#74C0FC", width=1.4).set_fill("#0F1720", opacity=0.9)
        game_screen.move_to(game_card[0].get_center() + DOWN * 0.1)
        game_agent = Circle(radius=0.08, color=PALETTE.agent, fill_opacity=1).move_to(game_screen.get_left() + RIGHT * 0.26)
        game_goal = Circle(radius=0.11, color=PALETTE.goal, fill_opacity=0.25).move_to(game_screen.get_right() + LEFT * 0.24)
        game_reward = Text("reward +1", font_size=TYPOGRAPHY.small_size - 6, color=PALETTE.goal, weight="BOLD")
        game_reward.next_to(game_goal, UP, buff=0.08).shift(LEFT * 0.34)
        max_reward_right = game_screen.get_right()[0] - 0.06
        reward_overflow = game_reward.get_right()[0] - max_reward_right
        if reward_overflow > 0:
            game_reward.shift(LEFT * reward_overflow)

        # Robot icon + mini grid.
        mini_grid = VGroup()
        for r in range(3):
            for c in range(3):
                cell = Square(side_length=0.36)
                cell.set_stroke(PALETTE.text_muted, width=1.0).set_fill("#1C212B", opacity=0.65)
                cell.move_to(robot_card[0].get_center() + LEFT * 0.36 + c * RIGHT * 0.38 + (1 - r) * UP * 0.38)
                mini_grid.add(cell)
        robot_agent = Circle(radius=0.07, color=PALETTE.agent, fill_opacity=1).move_to(mini_grid[6].get_center())
        robot_goal = Circle(radius=0.09, color=PALETTE.goal, fill_opacity=0.25).move_to(mini_grid[2].get_center())

        # Driving icon.
        road = RoundedRectangle(width=2.45, height=1.2, corner_radius=0.08)
        road.set_stroke("#FFD43B", width=1.2).set_fill("#151A22", opacity=0.85)
        road.move_to(car_card[0].get_center() + DOWN * 0.08)
        lane_1 = Line(road.get_left() + RIGHT * 0.25 + UP * 0.17, road.get_right() + LEFT * 0.25 + UP * 0.17, color=PALETTE.text_muted)
        lane_2 = Line(road.get_left() + RIGHT * 0.25 + DOWN * 0.17, road.get_right() + LEFT * 0.25 + DOWN * 0.17, color=PALETTE.text_muted)
        car = RoundedRectangle(width=0.45, height=0.22, corner_radius=0.04)
        car.set_fill("#FFD43B", opacity=0.95).set_stroke("#E0A800", width=1.0)
        car.move_to(road.get_left() + RIGHT * 0.45 + DOWN * 0.17)

        self.play(FadeIn(game_card), run_time=0.7)
        self.play(FadeIn(game_screen), FadeIn(game_agent), FadeIn(game_goal), run_time=0.5)
        game_status = Text("Explores,\nthen improves", font_size=TYPOGRAPHY.small_size - 5, color=PALETTE.text_primary)
        game_status.move_to(game_card[0].get_bottom() + UP * 0.55)
        self.play(FadeIn(game_status), run_time=0.4)
        game_start = game_agent.get_center()
        game_explore_mid_1 = game_screen.get_center() + LEFT * 0.16 + UP * 0.22
        game_explore_mid_2 = game_screen.get_center() + RIGHT * 0.22 + UP * 0.04
        game_explore_end = game_screen.get_center() + RIGHT * 0.06 + DOWN * 0.2
        game_explore_path = VMobject().set_points_as_corners(
            [game_start, game_explore_mid_1, game_explore_mid_2, game_explore_end]
        )

        game_improve_mid = game_screen.get_center() + RIGHT * 0.28 + DOWN * 0.04
        game_improve_path = VMobject().set_points_as_corners(
            [game_explore_end, game_improve_mid, game_goal.get_center()]
        )

        self.play(MoveAlongPath(game_agent, game_explore_path), run_time=1.0)
        self.play(MoveAlongPath(game_agent, game_improve_path), FadeIn(game_reward), run_time=1.0)
        self.wait(2.5)

        self.play(FadeIn(robot_card), run_time=0.7)
        self.play(FadeIn(mini_grid), FadeIn(robot_agent), FadeIn(robot_goal), run_time=0.55)
        robot_path = VGroup(
            Line(mini_grid[6].get_center(), mini_grid[7].get_center()),
            Line(mini_grid[7].get_center(), mini_grid[8].get_center()),
            Line(mini_grid[8].get_center(), mini_grid[5].get_center()),
            Line(mini_grid[5].get_center(), mini_grid[2].get_center()),
        )
        self.play(
            AnimationGroup(
                *[MoveAlongPath(robot_agent, seg, run_time=0.35) for seg in robot_path],
                lag_ratio=1,
            )
        )
        robot_status = Text("Finds safer,\nshorter paths", font_size=TYPOGRAPHY.small_size - 5, color=PALETTE.goal)
        robot_status.next_to(mini_grid, DOWN, buff=0.12)
        self.play(FadeIn(robot_status), run_time=0.4)
        self.play(robot_agent.animate.move_to(mini_grid[6].get_center()), run_time=0.35)
        self.play(
            AnimationGroup(
                *[MoveAlongPath(robot_agent, seg, run_time=0.25) for seg in robot_path],
                lag_ratio=1,
            )
        )
        self.wait(2.5)

        self.play(FadeIn(car_card), run_time=0.7)
        self.play(FadeIn(road), FadeIn(lane_1), FadeIn(lane_2), FadeIn(car), run_time=0.55)
        self.play(car.animate.shift(RIGHT * 1.35), run_time=1.2)
        car_status = Text("Balances speed\nand safety", font_size=TYPOGRAPHY.small_size - 5, color="#FFD43B")
        car_status.next_to(road, DOWN, buff=0.12)
        self.play(FadeIn(car_status), run_time=0.4)
        self.play(car.animate.shift(LEFT * 1.35), run_time=0.8)
        self.play(car.animate.shift(RIGHT * 1.35), run_time=0.8)
        self.wait(2.2)

        takeaway = Text(
            "Machines learn from interaction in games, robots, and driving.",
            font_size=TYPOGRAPHY.small_size,
            color=PALETTE.accent,
        ).to_edge(DOWN, buff=0.32)
        self.play(FadeIn(takeaway), run_time=0.7)
        self.wait(7.0)

        self.play(FadeOut(game_reward), run_time=0.3)
        self.play(FadeOut(game_status), FadeOut(robot_status), FadeOut(car_status), run_time=0.45)
        closing = Text("Same RL idea, different real environments.", font_size=TYPOGRAPHY.small_size - 1, color=PALETTE.text_primary)
        closing.next_to(takeaway, UP, buff=0.12)
        self.play(FadeIn(closing), run_time=0.5)
        self.wait(16.0)
