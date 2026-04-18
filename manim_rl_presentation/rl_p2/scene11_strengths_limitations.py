"""Scene 11: Strengths and limitations."""

from pathlib import Path
import sys

from manim import DOWN, FadeIn, LaggedStart, Text

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
    """Balanced comparison to avoid over-selling RL."""

    def construct(self):
        header = SceneHeader("11. Strengths and Limitations of RL")
        self.play(FadeIn(header))
        self.wait(2.0)

        strengths = [
            "Optimizes long-term decisions",
            "Learns from interaction",
            "Useful when rules are hard to handcraft",
        ]
        limitations = [
            "Data-hungry training",
            "Reward design is difficult",
            "Can be unstable and sensitive",
        ]
        columns = ComparisonColumns("Strengths", strengths, "Limitations", limitations).shift(DOWN * 0.25)
        left_col = columns[0][0]
        right_col = columns[0][1]
        self.play(FadeIn(left_col), run_time=0.9)
        self.wait(14.0)
        self.play(FadeIn(right_col), run_time=0.9)
        self.wait(18.0)

        balance = Text(
            "RL is powerful, but not a universal solution.",
            font_size=TYPOGRAPHY.small_size,
            color=PALETTE.accent,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(balance), run_time=0.6)
        self.wait(14.0)
