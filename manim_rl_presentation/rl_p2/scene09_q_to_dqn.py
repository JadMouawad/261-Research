"""Scene 9: From Q-table to DQN."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, Arrow, Circle, FadeIn, LaggedStart, Line, Rectangle, ReplacementTransform, Text, VGroup

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


def build_q_table_mock(rows: int = 7, cols: int = 7) -> VGroup:
    """Dense table to visually communicate scaling limitations."""
    table = VGroup()
    for r in range(rows):
        for c in range(cols):
            cell = Rectangle(width=0.45, height=0.28)
            cell.set_fill("#1C212B", opacity=0.85).set_stroke(PALETTE.text_muted, width=0.6)
            cell.move_to((c - (cols - 1) / 2) * 0.48 * RIGHT + ((rows - 1) / 2 - r) * 0.31 * UP)
            table.add(cell)
    label = Text("Q-table", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary)
    label.next_to(table, UP, buff=0.2)
    return VGroup(table, label)


def build_dqn_block() -> VGroup:
    """Simple neural-network block: state in, Q-values out."""
    layers = VGroup()
    for x in [-1.2, -0.2, 0.8]:
        col = VGroup()
        for y in [0.9, 0.3, -0.3, -0.9]:
            n = Circle(radius=0.09).set_fill("#22324A", opacity=1).set_stroke(PALETTE.agent, width=1.2)
            n.move_to(x * RIGHT + y * UP)
            col.add(n)
        layers.add(col)

    edges = VGroup()
    for left_col, right_col in [(layers[0], layers[1]), (layers[1], layers[2])]:
        for a in left_col:
            for b in right_col:
                edges.add(Line(a.get_center(), b.get_center(), stroke_width=0.6, color=PALETTE.text_muted))

    block = VGroup(edges, layers)
    in_lbl = Text("state", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).next_to(block, LEFT, buff=0.35)
    out_lbl = Text("Q(s,a)", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).next_to(block, RIGHT, buff=0.35)
    return VGroup(block, in_lbl, out_lbl)


class Scene09QTableToDQN(P2BaseScene):
    """Connects RL intuition to deep learning through DQN."""

    def construct(self):
        header = SceneHeader("9. From Q-learning to DQN", "Same objective, better representation")
        self.play(FadeIn(header))

        q_table = build_q_table_mock().to_edge(LEFT, buff=1.0).shift(DOWN * 0.2)
        overflow = Text("Does not scale to large state spaces", font_size=TYPOGRAPHY.small_size, color=PALETTE.bad)
        overflow.next_to(q_table, DOWN, buff=0.25)
        self.play(FadeIn(q_table))
        self.play(FadeIn(overflow))

        dqn = build_dqn_block().to_edge(RIGHT, buff=1.1).shift(DOWN * 0.15)
        arrow = Arrow(q_table.get_right(), dqn.get_left(), buff=0.25, color=PALETTE.accent)
        arrow_lbl = Text("Use a neural network to estimate Q", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        arrow_lbl.next_to(arrow, UP, buff=0.15)
        compact_table = q_table.copy().scale(0.6).move_to(dqn.get_left() + LEFT * 1.0)
        self.play(ReplacementTransform(q_table.copy(), compact_table), run_time=0.8)
        self.play(FadeIn(dqn), FadeIn(arrow), FadeIn(arrow_lbl))

        badges = VGroup(
            Text("Experience Replay", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
            Text("Target Network", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        badges.next_to(dqn, DOWN, buff=0.3).align_to(dqn, LEFT)
        self.play(LaggedStart(*[FadeIn(b) for b in badges], lag_ratio=0.2))
        self.pause_for("long")
