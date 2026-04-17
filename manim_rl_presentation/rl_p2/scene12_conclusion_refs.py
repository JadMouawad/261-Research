"""Scene 12: Conclusion and references."""

from pathlib import Path
import sys

from manim import DOWN, UP, FadeIn, Text, VGroup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from .components.headers import SceneHeader
    from .components.references import ReferenceList
    from .constants import PALETTE, TYPOGRAPHY
    from .scene_base import P2BaseScene
except ImportError:
    from manim_rl_presentation.rl_p2.components.headers import SceneHeader
    from manim_rl_presentation.rl_p2.components.references import ReferenceList
    from manim_rl_presentation.rl_p2.constants import PALETTE, TYPOGRAPHY
    from manim_rl_presentation.rl_p2.scene_base import P2BaseScene


class Scene12ConclusionReferences(P2BaseScene):
    """Professional close: concise takeaway + readable references."""

    def construct(self):
        header = SceneHeader("12. Conclusion + References")
        self.play(FadeIn(header))

        takeaway = VGroup(
            Text(
                "RL learns better decisions over time from reward feedback.",
                font_size=TYPOGRAPHY.subtitle_size,
                color=PALETTE.accent,
                weight="BOLD",
            ),
            Text(
                "Q-learning -> DQN keeps the same core idea, but scales to larger problems.",
                font_size=TYPOGRAPHY.small_size,
                color=PALETTE.text_primary,
            ),
        ).arrange(DOWN, buff=0.18)
        takeaway.shift(DOWN * 1.5)

        refs = ReferenceList(
            [
                "Sutton & Barto (2018), Reinforcement Learning: An Introduction",
                "Mnih et al. (2015), Nature: Human-level control through deep RL",
                "OpenAI Spinning Up: RL Intro",
                "David Silver RL Course (UCL)",
                "Lilian Weng: RL Overview",
            ]
        ).scale(0.88)
        refs.next_to(takeaway, UP, buff=0.5)

        self.play(FadeIn(takeaway), run_time=1.0)
        self.play(FadeIn(refs), run_time=1.1)
        self.pause_for("long")
