"""Scene 10: Real-world application - warehouse robot navigation."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, RoundedRectangle, Text, VGroup

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

        # Left panel: warehouse as a gridworld-like map.
        world = GridWorld(rows=5, cols=6, cell_size=0.72).shift(LEFT * 2.15 + DOWN * 0.05)
        world.mark_start(4, 0)
        world.mark_goal(0, 5, "+1")
        world.mark_bad(2, 3, "-1")
        agent = world.spawn_agent(4, 0)
        agent.set_stroke("#FFFFFF", width=1.2).set_z_index(30).set_opacity(1)
        goal_lbl = Text("Delivery goal", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.goal)
        goal_lbl.next_to(world.cells[(0, 5)], LEFT, buff=0.1).shift(UP * 0.02)

        # Mark a single collision zone band instead of repeating text labels.
        collision_cells = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
        collision_zone = world.flash_path(collision_cells, color=PALETTE.bad)
        collision_zone.set_z_index(5)
        collision_label = Text("Collision-risk zone", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.bad)
        collision_label.next_to(world, LEFT, buff=0.08).shift(UP * 0.18)

        # Right panel: compact state/action/reward mapping card.
        side = VGroup(
            Text("State: location + traffic", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_primary),
            Text("Action: move / wait / reroute", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_primary),
            Text("Reward: +delivery, -collision, -time", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        side_panel = RoundedRectangle(width=6.0, height=2.2, corner_radius=0.1)
        side_panel.set_fill("#161B22", opacity=0.9).set_stroke(PALETTE.text_muted, width=1.1)
        side.move_to(side_panel.get_center()).align_to(side_panel, LEFT).shift(RIGHT * 0.25)
        side_group = VGroup(side_panel, side).to_edge(RIGHT, buff=0.4).shift(UP * 0.45)

        self.play(FadeIn(world), FadeIn(agent), FadeIn(goal_lbl), FadeIn(collision_zone), FadeIn(collision_label))
        self.play(FadeIn(side_group))

        risky = [(3, 0), (2, 0), (2, 1), (2, 2)]
        safe = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (2, 5), (1, 5), (0, 5)]
        risky_overlay = world.flash_path(risky, color=PALETTE.bad)
        safe_overlay = world.flash_path(safe, color=PALETTE.goal)
        risky_overlay.set_z_index(6)
        safe_overlay.set_z_index(6)
        risky_lbl = Text("Naive risky route", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.bad).next_to(world, UP, buff=0.16)
        safe_lbl = Text("Learned safer route", font_size=TYPOGRAPHY.small_size, color=PALETTE.goal).move_to(risky_lbl)

        self.play(FadeIn(risky_overlay), FadeIn(risky_lbl))
        self.play(world.path_animation(risky, run_time_per_step=0.28))
        self.play(agent.animate.move_to(world.cell_center(4, 0)), FadeOut(risky_overlay), run_time=0.45)

        self.play(FadeIn(safe_overlay), risky_lbl.animate.become(safe_lbl), run_time=0.4)
        self.play(world.path_animation(safe, run_time_per_step=0.23))

        takeaway = Text("Same RL loop as gridworld, now in a real warehouse.", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_muted)
        takeaway.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(takeaway))
        self.pause_for("long")
