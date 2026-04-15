"""Scene 11: Strengths and limitations."""

from pathlib import Path
import sys

from manim import DOWN, FadeIn, LaggedStart

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from .components.comparison_layouts import ComparisonColumns
    from .components.headers import SceneHeader
    from .scene_base import P2BaseScene
except ImportError:
    from manim_rl_presentation.rl_p2.components.comparison_layouts import ComparisonColumns
    from manim_rl_presentation.rl_p2.components.headers import SceneHeader
    from manim_rl_presentation.rl_p2.scene_base import P2BaseScene


class Scene11StrengthsLimitations(P2BaseScene):
    """Balanced comparison to avoid over-selling RL."""

    def construct(self):
        header = SceneHeader("11. Strengths and Limitations of RL")
        self.play(FadeIn(header))

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
        self.play(LaggedStart(FadeIn(left_col), FadeIn(right_col), lag_ratio=0.25), run_time=1.3)
        self.pause_for("long")
