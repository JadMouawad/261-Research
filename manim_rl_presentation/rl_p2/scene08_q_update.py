"""Scene 8: Maze learning improves through Q-updates."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, WHITE, Arrow, FadeIn, FadeOut, Indicate, MathTex, RoundedRectangle, Text, VGroup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from .components.gridworld import GridWorld
    from .components.headers import SceneHeader
    from .constants import PALETTE, TYPOGRAPHY
    from .scene_base import P2BaseScene
except ImportError:
    from manim_rl_presentation.rl_p2.components.gridworld import GridWorld
    from manim_rl_presentation.rl_p2.components.headers import SceneHeader
    from manim_rl_presentation.rl_p2.constants import PALETTE, TYPOGRAPHY
    from manim_rl_presentation.rl_p2.scene_base import P2BaseScene


class Scene08QUpdateProcess(P2BaseScene):
    """Conceptual walkthrough of the Q-learning update rule."""

    def construct(self):
        header = SceneHeader("Maze Learning Improves", "Q-updates make good moves more likely")
        header.animate_in(self)
        self.wait(0.8)

        grid = GridWorld(rows=4, cols=4).scale(0.8).to_edge(LEFT, buff=0.95).shift(DOWN * 0.25)
        grid.mark_start(3, 0)
        goal_marker = grid.mark_goal(0, 3)
        bad_marker = grid.mark_bad(1, 2)
        agent = grid.spawn_agent(3, 0)
        agent.set_stroke(WHITE, width=1.2).set_z_index(20)

        self.play(grid.intro_animation(), run_time=1.0)
        self.play(grid.markers_animation(), FadeIn(agent), run_time=0.8)
        self.wait(1.6)

        early = [(2, 0), (1, 0), (1, 1), (1, 2)]
        improved = [(2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)]
        early_overlay = grid.flash_path(early, color=PALETTE.bad)
        improved_overlay = grid.flash_path(improved, color=PALETTE.goal)
        status = Text("Before updates:\nmore mistakes", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.bad)
        status.next_to(grid, UP, buff=0.22)

        self.play(FadeIn(early_overlay), FadeIn(status), run_time=0.5)
        self.play(grid.path_animation(early, run_time_per_step=0.50))
        self.play(Indicate(bad_marker, color=PALETTE.bad), run_time=0.6)
        self.wait(0.9)
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), FadeOut(early_overlay), run_time=0.4)

        improved_status = Text("After updates:\nbetter, safer path", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.goal).move_to(status)
        self.play(status.animate.become(improved_status), FadeIn(improved_overlay), run_time=0.45)
        self.play(grid.path_animation(improved, run_time_per_step=0.40))
        self.play(Indicate(goal_marker, color=PALETTE.goal), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(improved_overlay), FadeOut(status), agent.animate.move_to(grid.cell_center(3, 0)), run_time=0.5)

        eq_panel = RoundedRectangle(width=8.6, height=3.0, corner_radius=0.12).set_fill("#161B22", opacity=0.92)
        eq_panel.set_stroke(PALETTE.text_muted, width=1.2).to_edge(RIGHT, buff=0.45).shift(UP * 0.45)
        eq = MathTex(
            r"Q(s,a)\leftarrow Q(s,a)+\alpha\left[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\right]",
            color=PALETTE.text_primary,
        ).scale(0.67)
        eq.move_to(eq_panel.get_center() + UP * 0.22)
        hint = Text("new = old + correction", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        hint.next_to(eq, DOWN, buff=0.24)
        self.play(FadeIn(eq_panel), FadeIn(eq), FadeIn(hint))
        self.wait(3.8)

        # Conceptual term-by-term interpretation (speech-friendly pacing).
        legend_title = Text("What each symbol means:", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        term_font = TYPOGRAPHY.small_size - 3
        term_1 = Text("Q(s,a): current score for action a at state s", font_size=term_font, color=PALETTE.text_muted)
        term_2 = Text("r: immediate reward after the action", font_size=term_font, color=PALETTE.goal)
        term_3 = Text("max Q(s',a'): best future score at next state", font_size=term_font, color=PALETTE.accent)
        term_4 = Text("alpha: learning rate (update size)", font_size=term_font, color=PALETTE.text_primary)
        term_5 = Text("gamma: discount factor (future weight)", font_size=term_font, color=PALETTE.text_primary)
        term_group = VGroup(legend_title, term_1, term_2, term_3, term_4, term_5).arrange(DOWN, aligned_edge=LEFT, buff=0.11)
        term_group.next_to(eq_panel, DOWN, buff=0.12).align_to(eq_panel, LEFT).shift(RIGHT * 0.12)
        self.play(FadeIn(legend_title), run_time=0.55)
        self.wait(1.05)
        self.play(FadeIn(term_1), run_time=0.55)
        self.wait(1.05)
        self.play(FadeIn(term_2), run_time=0.55)
        self.wait(1.05)
        self.play(FadeIn(term_3), run_time=0.55)
        self.wait(1.05)
        self.play(FadeIn(term_4), run_time=0.55)
        self.wait(1.05)
        self.play(FadeIn(term_5), run_time=0.55)
        self.wait(15.0)

        trans = Text("One step: (s, a, r, s')", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary)
        trans.next_to(eq_panel, DOWN, buff=0.32).align_to(eq_panel, LEFT).shift(RIGHT * 0.2)
        self.play(FadeIn(trans), FadeOut(legend_title), FadeOut(term_1), FadeOut(term_2), FadeOut(term_3), FadeOut(term_4), FadeOut(term_5))
        self.wait(2.0)

        src_cell = grid.cells[(3, 0)].copy().set_fill(PALETTE.accent, opacity=0.22).set_stroke(PALETTE.accent, width=2)
        dst_cell = grid.cells[(2, 0)].copy().set_fill(PALETTE.goal, opacity=0.16).set_stroke(PALETTE.goal, width=2)
        step_arrow = Arrow(
            start=grid.cell_center(3, 0) + UP * 0.1,
            end=grid.cell_center(2, 0) + DOWN * 0.1,
            buff=0,
            color=PALETTE.accent,
            stroke_width=4,
        )
        self.play(FadeIn(src_cell), FadeIn(dst_cell), FadeIn(step_arrow), run_time=0.5)
        self.wait(1.4)
        self.play(grid.path_animation([(2, 0)], run_time_per_step=0.95))
        self.wait(1.4)
        self.play(FadeOut(src_cell), FadeOut(dst_cell), FadeOut(step_arrow), run_time=0.3)
        before = Text("Q old = 0.30", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_muted).next_to(trans, DOWN, aligned_edge=LEFT, buff=0.1)
        after = Text("Q new = 0.42", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).next_to(before, DOWN, aligned_edge=LEFT, buff=0.08)
        self.play(FadeIn(before))
        self.wait(1.4)
        self.play(FadeIn(after))
        self.wait(1.6)

        # A second step reinforces the "update happens repeatedly" idea.
        src2_cell = grid.cells[(2, 0)].copy().set_fill(PALETTE.accent, opacity=0.20).set_stroke(PALETTE.accent, width=2)
        dst2_cell = grid.cells[(2, 1)].copy().set_fill(PALETTE.goal, opacity=0.16).set_stroke(PALETTE.goal, width=2)
        step2_arrow = Arrow(
            start=grid.cell_center(2, 0) + RIGHT * 0.08,
            end=grid.cell_center(2, 1) + LEFT * 0.08,
            buff=0,
            color=PALETTE.accent,
            stroke_width=4,
        )
        before2 = Text("Q old = 0.42", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_muted).move_to(before)
        after2 = Text("Q new = 0.56", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).move_to(after)
        self.play(FadeIn(src2_cell), FadeIn(dst2_cell), FadeIn(step2_arrow), run_time=0.45)
        self.play(grid.path_animation([(2, 1)], run_time_per_step=0.9))
        self.play(FadeOut(src2_cell), FadeOut(dst2_cell), FadeOut(step2_arrow), run_time=0.3)
        self.play(before.animate.become(before2), after.animate.become(after2), run_time=0.5)
        self.wait(1.8)

        params = VGroup(
            Text("alpha controls update size (learning rate)", font_size=TYPOGRAPHY.small_size - 1, color=PALETTE.text_primary),
            Text("gamma controls future weight (discount)", font_size=TYPOGRAPHY.small_size - 1, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        params.next_to(after, DOWN, aligned_edge=LEFT, buff=0.12)
        self.play(FadeIn(params))
        self.wait(12.0)
