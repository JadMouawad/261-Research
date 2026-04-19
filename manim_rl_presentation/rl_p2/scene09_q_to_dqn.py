"""Scene 9: From Q-learning to DQN."""

from pathlib import Path
import sys

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Indicate,
    LaggedStart,
    Line,
    Rectangle,
    RoundedRectangle,
    SurroundingRectangle,
    Text,
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


def build_q_table_mock(rows: int = 6, cols: int = 6) -> VGroup:
    """Dense table to visually communicate scaling limitations."""
    table = VGroup()
    for r in range(rows):
        for c in range(cols):
            cell = Rectangle(width=0.42, height=0.28)
            cell.set_fill("#1C212B", opacity=0.85).set_stroke(PALETTE.text_muted, width=0.6)
            cell.move_to((c - (cols - 1) / 2) * 0.45 * RIGHT + ((rows - 1) / 2 - r) * 0.31 * UP)
            table.add(cell)
    label = Text("Q-table", font_size=TYPOGRAPHY.body_size, color=PALETTE.text_primary)
    label.next_to(table, UP, buff=0.2)
    return VGroup(table, label)


def build_dqn_block() -> VGroup:
    """Simple neural-network block: state in, Q-values out."""
    layers = VGroup()
    for x in [-1.2, -0.2, 0.8]:
        col = VGroup()
        for y in [0.9, 0.3, -0.3, -0.9]:
            node = Circle(radius=0.09).set_fill("#22324A", opacity=1).set_stroke(PALETTE.agent, width=1.2)
            node.move_to(x * RIGHT + y * UP)
            col.add(node)
        layers.add(col)

    edges = VGroup()
    for left_col, right_col in [(layers[0], layers[1]), (layers[1], layers[2])]:
        for a in left_col:
            for b in right_col:
                edges.add(Line(a.get_center(), b.get_center(), stroke_width=0.6, color=PALETTE.text_muted))

    block = VGroup(edges, layers)
    in_lbl = Text("state", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).next_to(block, LEFT, buff=0.2).shift(UP * 0.18)
    out_lbl = Text("Q-values", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary).next_to(block, RIGHT, buff=0.2).shift(UP * 0.18)
    return VGroup(block, in_lbl, out_lbl)


class Scene09QTableToDQN(P2BaseScene):
    """Connects RL intuition to deep learning through DQN."""

    def construct(self):
        header = SceneHeader("From Q-learning to DQN", "Same objective, better representation")
        header.animate_in(self)
        self.wait(0.8)

        # Left: tabular approach.
        q_table = build_q_table_mock().move_to(LEFT * 4.1 + DOWN * 0.05)
        cols = 6

        def make_row_highlight(row_idx: int, start_col: int = 2, end_col: int = 5) -> SurroundingRectangle:
            row_cells = VGroup(*[q_table[0][row_idx * cols + c] for c in range(start_col, end_col + 1)])
            box = SurroundingRectangle(row_cells, buff=0.02)
            box.set_stroke(PALETTE.accent, width=2.2).set_fill(PALETTE.accent, opacity=0.06)
            return box

        sample_row = make_row_highlight(0)
        sample_note = Text("one state -> action scores", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.accent)
        sample_note.next_to(q_table, DOWN, buff=0.18).align_to(q_table, LEFT)
        overflow = Text("Hard to scale to many states", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.bad)
        overflow.next_to(sample_note, DOWN, buff=0.12).align_to(sample_note, LEFT)

        self.play(FadeIn(q_table), run_time=0.8)
        self.play(FadeIn(sample_row), FadeIn(sample_note), run_time=0.5)
        self.play(Indicate(sample_row, color=PALETTE.accent), run_time=0.7)
        self.play(FadeIn(overflow), run_time=0.4)
        self.wait(1.5)

        row_2 = make_row_highlight(2)
        row_3 = make_row_highlight(4)
        self.play(FadeIn(row_2), run_time=0.35)
        self.play(FadeIn(row_3), run_time=0.35)
        self.play(Indicate(row_2, color=PALETTE.accent), run_time=0.6)
        self.play(Indicate(row_3, color=PALETTE.accent), run_time=0.6)
        many_note = Text("More states => many more rows", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.bad)
        many_note.next_to(overflow, DOWN, buff=0.10).align_to(overflow, LEFT)
        self.play(FadeIn(many_note), run_time=0.45)
        self.wait(3.5)

        # Center: representation shift.
        bridge = Arrow(
            start=LEFT * 1.15 + DOWN * 0.05,
            end=RIGHT * 1.05 + DOWN * 0.05,
            buff=0,
            color=PALETTE.accent,
            stroke_width=5,
        )
        bridge_lbl = Text("Replace table with neural net", font_size=TYPOGRAPHY.small_size - 3, color=PALETTE.accent)
        bridge_lbl.next_to(bridge, UP, buff=0.18).shift(LEFT * 0.2)
        self.play(FadeIn(bridge), FadeIn(bridge_lbl), run_time=0.7)
        self.wait(4.0)

        # Right: DQN representation.
        dqn = build_dqn_block().move_to(RIGHT * 4.35 + DOWN * 0.05)
        self.play(FadeIn(dqn), run_time=0.9)
        self.wait(1.2)

        # Simulate changing Q-value outputs for one state.
        q_out_1 = Text("Q(s,.) = [0.2, 0.1, -0.1, 0.3]", font_size=TYPOGRAPHY.small_size - 3, color=PALETTE.text_primary)
        q_out_1.next_to(dqn, UP, buff=0.16)
        q_out_2 = Text("Q(s,.) = [0.4, 0.2, -0.2, 0.8]", font_size=TYPOGRAPHY.small_size - 3, color=PALETTE.goal).move_to(q_out_1)
        q_out_3 = Text("Best action stands out over training", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.goal).move_to(q_out_1)
        self.play(FadeIn(q_out_1), run_time=0.45)
        self.play(Indicate(dqn[2], color=PALETTE.goal), run_time=0.7)
        self.play(q_out_1.animate.become(q_out_2), run_time=0.65)
        self.wait(1.5)
        self.play(Indicate(dqn[0], color=PALETTE.accent), run_time=0.7)
        self.play(q_out_1.animate.become(q_out_3), run_time=0.55)
        self.wait(2.8)

        tips_title = Text("Stability tricks", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent)
        tips = VGroup(
            Text("- Experience Replay", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
            Text("- Target Network", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        tips_panel = RoundedRectangle(width=4.9, height=1.95, corner_radius=0.1)
        tips_panel.set_fill("#161B22", opacity=0.9).set_stroke(PALETTE.text_muted, width=1.1)

        tips_content = VGroup(tips_title, tips).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        tips_content.move_to(tips_panel.get_center()).align_to(tips_panel, LEFT).shift(RIGHT * 0.24)

        tips_group = VGroup(tips_panel, tips_content).next_to(dqn, DOWN, buff=0.25).align_to(dqn, LEFT)
        self.play(FadeIn(tips_panel), run_time=0.35)
        self.play(LaggedStart(*[FadeIn(m) for m in tips_content], lag_ratio=0.2))
        self.wait(7.0)

        closing = Text("DQN keeps Q-learning logic, but scales better.", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_muted)
        closing.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(closing), FadeOut(q_out_1), run_time=0.6)
        self.wait(11.0)
