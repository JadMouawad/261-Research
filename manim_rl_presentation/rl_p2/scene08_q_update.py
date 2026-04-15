"""Scene 8: Q-learning update process."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, MathTex, RoundedRectangle, Text, VGroup

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
        header = SceneHeader("8. How Q-learning Updates Knowledge")
        self.play(FadeIn(header))

        grid = GridWorld(rows=4, cols=4).scale(0.75).to_edge(LEFT, buff=1.0).shift(DOWN * 0.4)
        grid.mark_start(3, 0)
        grid.mark_goal(0, 3)
        grid.mark_bad(1, 2)
        agent = grid.spawn_agent(3, 0)
        self.play(FadeIn(grid), FadeIn(agent))

        eq_panel = RoundedRectangle(width=7.2, height=2.6, corner_radius=0.12).set_fill("#161B22", opacity=0.92)
        eq_panel.set_stroke(PALETTE.text_muted, width=1.2).to_edge(RIGHT, buff=0.6).shift(UP * 0.6)
        eq = MathTex(
            r"Q(s,a)\leftarrow Q(s,a)+\alpha\left[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\right]",
            color=PALETTE.text_primary,
        ).scale(0.65)
        eq.move_to(eq_panel.get_center() + UP * 0.15)
        hint = Text("new = old + correction", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        hint.next_to(eq, DOWN, buff=0.22)
        self.play(FadeIn(eq_panel), FadeIn(eq), FadeIn(hint))
        self.pause_for("short")

        # Single transition demonstration.
        trans = Text("One step: (s, a, r, s')", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary)
        trans.next_to(eq_panel, DOWN, buff=0.35).align_to(eq_panel, LEFT)
        self.play(FadeIn(trans))

        self.play(grid.path_animation([(2, 0), (2, 1)], run_time_per_step=0.45))
        before = Text("Q old = 0.30", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_muted).next_to(trans, DOWN, aligned_edge=LEFT)
        after = Text("Q new = 0.42", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).next_to(before, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(before))
        self.pause_for("beat")
        self.play(FadeIn(after))
        self.pause_for("short")

        params = VGroup(
            Text("alpha controls update size", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
            Text("gamma controls future weight", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        params.next_to(after, DOWN, aligned_edge=LEFT, buff=0.24)
        self.play(FadeIn(params))
        self.pause_for("long")
