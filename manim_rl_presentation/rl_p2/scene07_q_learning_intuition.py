"""Scene 7: Maze learning starts (Q-learning intuition)."""

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
        header = SceneHeader("Maze Learning Starts", "Random trials begin to reveal better actions")
        header.animate_in(self)
        self.wait(0.8)

        grid = GridWorld(rows=4, cols=4)
        grid.scale(1.02).shift(RIGHT * 0.75 + DOWN * 0.05)
        grid.mark_start(3, 0)
        goal_marker = grid.mark_goal(0, 3, "+1")
        bad_marker = grid.mark_bad(1, 2, "-1")
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
        self.wait(3.0)

        # Early random trials.
        label = Text("Early episodes: mostly random moves", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary)
        label.next_to(grid, UP, buff=0.18)
        fail_path = [(2, 0), (1, 0), (1, 1), (1, 2)]
        near_miss_path = [(3, 1), (3, 2), (2, 2), (2, 3), (1, 3)]
        success_path = [(2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)]

        fail_overlay = grid.flash_path(fail_path, color=PALETTE.bad)
        near_overlay = grid.flash_path(near_miss_path, color=PALETTE.accent)
        success_overlay = grid.flash_path(success_path, color=PALETTE.goal)

        self.play(FadeIn(label), FadeIn(fail_overlay), run_time=0.6)
        self.play(grid.path_animation(fail_path, run_time_per_step=0.52))
        self.play(Indicate(bad_marker, color=PALETTE.bad), run_time=0.6)
        self.wait(1.0)
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), FadeOut(fail_overlay), run_time=0.45)

        # Another brief random attempt keeps the "early chaos" intuition clear.
        retry_text = Text("Another trial can still fail", font_size=TYPOGRAPHY.small_size, color=PALETTE.bad).move_to(label)
        retry_overlay = grid.flash_path([(3, 1), (2, 1), (1, 1), (1, 2)], color=PALETTE.bad)
        self.play(ReplacementTransform(label, retry_text), FadeIn(retry_overlay), run_time=0.45)
        self.play(grid.path_animation([(3, 1), (2, 1), (1, 1), (1, 2)], run_time_per_step=0.48))
        self.play(Indicate(bad_marker, color=PALETTE.bad), run_time=0.5)
        self.wait(0.9)
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), FadeOut(retry_overlay), run_time=0.42)

        near_text = Text("Sometimes close, still inconsistent", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent).move_to(retry_text)
        self.play(ReplacementTransform(retry_text, near_text), FadeIn(near_overlay), run_time=0.5)
        self.play(grid.path_animation(near_miss_path, run_time_per_step=0.46))
        self.wait(1.0)
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), FadeOut(near_overlay), run_time=0.45)

        good_text = Text("Eventually reaches goal and gets reward", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).move_to(near_text)
        self.play(ReplacementTransform(near_text, good_text), FadeIn(success_overlay), run_time=0.5)
        self.play(grid.path_animation(success_path, run_time_per_step=0.42))
        self.play(Indicate(goal_marker, color=PALETTE.goal), run_time=0.6)
        self.wait(1.0)
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), run_time=0.45)

        reinforce_text = Text("With more episodes, this path repeats more often", font_size=TYPOGRAPHY.small_size - 1, color=PALETTE.goal).move_to(good_text)
        self.play(ReplacementTransform(good_text, reinforce_text), run_time=0.4)
        self.play(grid.path_animation(success_path, run_time_per_step=0.34))
        self.play(agent.animate.move_to(grid.cell_center(3, 0)), run_time=0.4)
        self.play(grid.path_animation(success_path, run_time_per_step=0.30))
        self.wait(1.0)

        # Action arrows around one state with improving Q-values.
        q_vals_early = {"U": 0.0, "R": 0.1, "D": -0.1, "L": 0.0}
        q_vals_mid = {"U": 0.2, "R": 0.5, "D": -0.3, "L": -0.1}
        q_vals_late = {"U": 0.4, "R": 0.9, "D": -0.5, "L": -0.2}
        focus_cell = grid.cells[(2, 1)].copy().set_fill(PALETTE.accent, opacity=0.14).set_stroke(PALETTE.accent, width=2.4)
        arrows_early = grid.make_action_arrows(2, 1, q_vals_early, precision=1)
        arrows_mid = grid.make_action_arrows(2, 1, q_vals_mid, precision=1)
        arrows_late = grid.make_action_arrows(2, 1, q_vals_late, precision=1)
        caption = Text("Q-value = expected future reward", color=PALETTE.text_primary, font_size=TYPOGRAPHY.small_size)
        caption.next_to(grid, UP, buff=0.18).align_to(grid, LEFT)

        self.play(
            FadeOut(success_overlay),
            FadeOut(reinforce_text),
            agent.animate.move_to(grid.cell_center(3, 0)).set_opacity(0.65),
            FadeIn(focus_cell),
            FadeIn(arrows_early),
            FadeIn(caption),
            run_time=0.7,
        )
        self.wait(2.2)
        self.play(ReplacementTransform(arrows_early, arrows_mid), run_time=0.8)
        self.wait(1.8)
        self.play(ReplacementTransform(arrows_mid, arrows_late), run_time=0.9)
        self.wait(1.2)
        self.play(Indicate(arrows_late[2], color=PALETTE.goal), run_time=0.8)
        self.wait(2.0)

        takeaway = Text("Learning turns random motion into a preferred route.", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        takeaway.next_to(grid, DOWN, buff=0.35)
        self.play(FadeIn(takeaway))
        self.wait(7.0)
