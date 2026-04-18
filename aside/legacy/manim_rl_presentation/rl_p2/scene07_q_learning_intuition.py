"""Scene 7: Q-learning intuition."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, Indicate, ReplacementTransform, Text

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from .components.gridworld import GridWorld
    from .components.headers import SceneHeader
    from .components.legends import make_legend
    from .constants import PALETTE, TYPOGRAPHY
    from .scene_base import P2BaseScene
except ImportError:
    from manim_rl_presentation.rl_p2.components.gridworld import GridWorld
    from manim_rl_presentation.rl_p2.components.headers import SceneHeader
    from manim_rl_presentation.rl_p2.components.legends import make_legend
    from manim_rl_presentation.rl_p2.constants import PALETTE, TYPOGRAPHY
    from manim_rl_presentation.rl_p2.scene_base import P2BaseScene


class Scene07QLearningIntuition(P2BaseScene):
    """Builds intuitive understanding of Q-values in the gridworld."""

    def construct(self):
        header = SceneHeader("7. Q-learning Intuition", "Action quality is learned over time")
        self.play(FadeIn(header))
        self.wait(2.0)

        grid = GridWorld(rows=4, cols=4)
        grid.scale(1.02).shift(RIGHT * 0.75 + DOWN * 0.05)
        grid.mark_start(3, 0)
        grid.mark_goal(0, 3, "+1")
        grid.mark_bad(1, 2, "-1")
        agent = grid.spawn_agent(3, 0)

        legend = make_legend(
            [
                (PALETTE.agent, "Agent"),
                (PALETTE.goal, "Goal reward"),
                (PALETTE.bad, "Bad state"),
            ]
        )
        legend.next_to(grid, LEFT, buff=0.75).align_to(grid, DOWN)

        self.play(grid.intro_animation(), run_time=1.2)
        self.play(grid.markers_animation(), FadeIn(agent), FadeIn(legend), run_time=0.8)
        self.wait(4.0)

        # Show one bad trial and one good trial to demonstrate value learning signal.
        bad_path = [(2, 0), (1, 0), (1, 1), (1, 2)]
        good_path = [(2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)]
        bad_overlay = grid.flash_path(bad_path, color=PALETTE.bad)
        good_overlay = grid.flash_path(good_path, color=PALETTE.goal)
        bad_label = Text("Unfavorable path", font_size=TYPOGRAPHY.small_size, color=PALETTE.bad).next_to(grid, UP, buff=0.18)
        good_label = Text("Better path after learning", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).move_to(bad_label)

        self.play(FadeIn(bad_overlay), FadeIn(bad_label), run_time=0.5)
        self.play(grid.path_animation(bad_path, run_time_per_step=0.55))
        self.wait(3.0)
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), FadeOut(bad_overlay), run_time=0.45)
        self.play(FadeIn(good_overlay), bad_label.animate.become(good_label), run_time=0.45)
        self.wait(1.5)
        self.play(grid.path_animation(good_path, run_time_per_step=0.50))
        self.wait(4.0)

        # Action arrows around one state with improving Q-values.
        q_vals_early = {"U": 0.1, "R": 0.2, "D": -0.1, "L": 0.0}
        q_vals_late = {"U": 0.4, "R": 0.9, "D": -0.5, "L": -0.2}
        focus_cell = grid.cells[(2, 1)].copy().set_fill(PALETTE.accent, opacity=0.14).set_stroke(PALETTE.accent, width=2.4)
        arrows_early = grid.make_action_arrows(2, 1, q_vals_early, precision=1)
        arrows_late = grid.make_action_arrows(2, 1, q_vals_late, precision=1)
        caption = Text("Q-value: future reward score", color=PALETTE.text_primary, font_size=TYPOGRAPHY.small_size)
        caption.next_to(grid, UP, buff=0.18).align_to(grid, LEFT)

        self.play(
            FadeOut(good_overlay),
            FadeOut(bad_label),
            agent.animate.move_to(grid.cell_center(3, 0)).set_opacity(0.65),
            FadeIn(focus_cell),
            FadeIn(arrows_early),
            FadeIn(caption),
            run_time=0.7,
        )
        self.wait(4.0)
        self.play(ReplacementTransform(arrows_early, arrows_late), run_time=0.9)
        self.wait(2.5)
        self.play(Indicate(arrows_late[2], color=PALETTE.goal), run_time=0.8)

        takeaway = Text("Policy: usually choose the highest Q-value", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        takeaway.next_to(grid, DOWN, buff=0.35)
        self.play(FadeIn(takeaway))
        self.wait(6.5)
