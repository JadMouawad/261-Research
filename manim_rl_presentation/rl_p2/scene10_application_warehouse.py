"""Scene 10: Real-world application - warehouse robot navigation."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, Text, VGroup

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


class Scene10WarehouseApplication(P2BaseScene):
    """Maps the gridworld setup to a coherent warehouse routing application."""

    def construct(self):
        header = SceneHeader("10. Real-world RL Application", "Warehouse robot navigation")
        self.play(FadeIn(header))

        # Reuse the gridworld idea, but style the middle row as shelf obstacles.
        world = GridWorld(rows=5, cols=6, cell_size=0.75).shift(LEFT * 1.6 + DOWN * 0.15)
        world.mark_start(4, 0)
        world.mark_goal(0, 5, "+Delivery")
        world.mark_bad(2, 2, "-Collision")
        world.mark_bad(2, 3, "-Collision")
        world.mark_bad(2, 4, "-Collision")
        agent = world.spawn_agent(4, 0)

        side = VGroup(
            Text("State: location + traffic", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
            Text("Action: move / wait / reroute", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
            Text("Reward: +delivery, -collision, -time", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.5).shift(UP * 0.1)

        self.play(FadeIn(world), FadeIn(agent), FadeIn(side))

        risky = [(3, 0), (2, 0), (2, 1), (2, 2)]
        safe = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (2, 5), (1, 5), (0, 5)]
        risky_overlay = world.flash_path(risky, color=PALETTE.bad)
        safe_overlay = world.flash_path(safe, color=PALETTE.goal)
        risky_lbl = Text("Naive risky route", font_size=TYPOGRAPHY.small_size, color=PALETTE.bad).next_to(world, UP, buff=0.2)
        safe_lbl = Text("Learned safer route", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).move_to(risky_lbl)

        self.play(FadeIn(risky_overlay), FadeIn(risky_lbl))
        self.play(world.path_animation(risky, run_time_per_step=0.3))
        self.play(agent.animate.move_to(world.cell_center(4, 0)), run_time=0.5)

        self.play(FadeIn(safe_overlay), risky_lbl.animate.become(safe_lbl))
        self.play(world.path_animation(safe, run_time_per_step=0.25))

        takeaway = Text("Same RL loop as gridworld, now in a real setting.", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        takeaway.next_to(world, DOWN, buff=0.25).align_to(world, LEFT)
        self.play(FadeIn(takeaway))
        self.pause_for("long")
