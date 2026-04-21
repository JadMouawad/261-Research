"""Scene 11: Strengths, limitations, and recap."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, Arrow, Circle, FadeIn, LaggedStart, Line, MoveAlongPath, RoundedRectangle, Text, VGroup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from .components.comparison_layouts import ComparisonColumns
    from .components.headers import SceneHeader
    from .constants import PALETTE, TYPOGRAPHY
    from .scene_base import P2BaseScene
except ImportError:
    from manim_rl_presentation.rl_p2.components.comparison_layouts import ComparisonColumns
    from manim_rl_presentation.rl_p2.components.headers import SceneHeader
    from manim_rl_presentation.rl_p2.constants import PALETTE, TYPOGRAPHY
    from manim_rl_presentation.rl_p2.scene_base import P2BaseScene


class Scene11StrengthsLimitations(P2BaseScene):
    """Balanced comparison plus recap to set up the final conclusion."""

    def construct(self):
        header = SceneHeader("Strengths and Limitations", "Powerful idea, with practical tradeoffs")
        header.animate_in(self)
        self.wait(0.8)

        # Compact RL loop at top for recap context.
        state = Text("State", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).move_to(LEFT * 3.3 + UP * 1.33)
        action = Text("Action", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).move_to(LEFT * 0.9 + UP * 1.33)
        reward = Text("Reward", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).move_to(RIGHT * 1.5 + UP * 1.33)
        next_state = Text("Next state", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).move_to(RIGHT * 4.2 + UP * 1.33)

        edge_1 = Arrow(state.get_right() + RIGHT * 0.08, action.get_left() + LEFT * 0.08, buff=0, stroke_width=3, color=PALETTE.text_muted)
        edge_2 = Arrow(action.get_right() + RIGHT * 0.08, reward.get_left() + LEFT * 0.08, buff=0, stroke_width=3, color=PALETTE.text_muted)
        edge_3 = Arrow(reward.get_right() + RIGHT * 0.08, next_state.get_left() + LEFT * 0.08, buff=0, stroke_width=3, color=PALETTE.text_muted)
        edge_back = Arrow(next_state.get_bottom() + DOWN * 0.2, state.get_bottom() + DOWN * 0.2, buff=0, stroke_width=2.5, color=PALETTE.text_muted)

        loop_dot = Circle(radius=0.055, color=PALETTE.agent, fill_opacity=1).move_to(edge_1.get_start())
        loop_path = VGroup(
            Line(edge_1.get_start(), edge_1.get_end()),
            Line(edge_2.get_start(), edge_2.get_end()),
            Line(edge_3.get_start(), edge_3.get_end()),
            Line(edge_back.get_start(), edge_back.get_end()),
        )

        loop_group = VGroup(state, action, reward, next_state, edge_1, edge_2, edge_3, edge_back)
        self.play(FadeIn(loop_group), FadeIn(loop_dot), run_time=1.0)
        self.play(MoveAlongPath(loop_dot, loop_path[0]), run_time=0.5)
        self.play(MoveAlongPath(loop_dot, loop_path[1]), run_time=0.5)
        self.play(MoveAlongPath(loop_dot, loop_path[2]), run_time=0.5)
        self.play(MoveAlongPath(loop_dot, loop_path[3]), run_time=0.7)
        self.wait(0.8)
        self.play(MoveAlongPath(loop_dot, loop_path[0]), run_time=0.4)
        self.play(MoveAlongPath(loop_dot, loop_path[1]), run_time=0.4)
        self.play(MoveAlongPath(loop_dot, loop_path[2]), run_time=0.4)
        self.play(MoveAlongPath(loop_dot, loop_path[3]), run_time=0.6)
        self.wait(1.2)

        strengths = [
            "Optimizes long-term decisions",
            "Learns from interaction",
            "Adapts when rules are hard to code",
        ]
        limitations = [
            "Needs many training episodes",
            "Reward design is sensitive",
            "Training can be unstable",
        ]
        columns = ComparisonColumns("Strengths", strengths, "Limitations", limitations).shift(DOWN * 0.71)
        left_col = columns[0][0]
        right_col = columns[0][1]

        self.play(FadeIn(left_col[0]), run_time=0.7)
        left_title = left_col[1][0]
        left_items = left_col[1][1]
        self.play(FadeIn(left_title), run_time=0.35)
        self.play(FadeIn(left_items[0]), run_time=0.35)
        self.play(FadeIn(left_items[1]), run_time=0.35)
        self.play(FadeIn(left_items[2]), run_time=0.35)
        self.wait(1.2)

        self.play(FadeIn(right_col[0]), run_time=0.7)
        right_title = right_col[1][0]
        right_items = right_col[1][1]
        self.play(FadeIn(right_title), run_time=0.35)
        self.play(FadeIn(right_items[0]), run_time=0.35)
        self.play(FadeIn(right_items[1]), run_time=0.35)
        self.play(FadeIn(right_items[2]), run_time=0.35)
        self.wait(1.5)

        self.wait(6.8)

        recap_lines = VGroup(
            Text("Recap", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent, weight="BOLD"),
            Text("RL improves through repeated feedback-driven interaction.", font_size=TYPOGRAPHY.small_size - 3, color=PALETTE.text_primary),
            Text("Best results come from balancing strengths and limits.", font_size=TYPOGRAPHY.small_size - 3, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        recap_panel = RoundedRectangle(width=12.0, height=1.42, corner_radius=0.12)
        recap_panel.set_fill("#161B22", opacity=0.92).set_stroke(PALETTE.text_muted, width=1.1)
        recap_lines.move_to(recap_panel.get_center()).align_to(recap_panel, LEFT).shift(RIGHT * 0.25)
        recap_group = VGroup(recap_panel, recap_lines).to_edge(DOWN, buff=0.19)

        self.play(FadeIn(recap_panel), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(item) for item in recap_lines], lag_ratio=0.22), run_time=1.1)
        self.wait(20.0)
