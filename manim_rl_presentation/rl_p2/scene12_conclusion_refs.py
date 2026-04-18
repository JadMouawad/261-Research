"""Scene 12: Conclusion and references."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, LaggedStart, Text, VGroup

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
        self.wait(2.0)

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
        ).scale(0.82)
        refs.next_to(takeaway, UP, buff=0.5)

        self.play(FadeIn(takeaway), run_time=1.0)
        self.wait(14.0)

        recap_title = Text("What to remember", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent, weight="BOLD")
        recap_points = VGroup(
            Text("1. RL learns from rewards over interaction.", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_primary),
            Text("2. Q-learning updates one step at a time.", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_primary),
            Text("3. DQN scales Q-learning with neural networks.", font_size=TYPOGRAPHY.small_size - 2, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        recap = VGroup(recap_title, recap_points).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        recap.next_to(takeaway, UP, buff=0.45).to_edge(LEFT, buff=0.95)
        self.play(LaggedStart(*[FadeIn(m) for m in recap], lag_ratio=0.25), run_time=1.2)
        self.wait(18.0)

        self.play(FadeOut(recap), run_time=0.5)
        self.play(FadeIn(refs), run_time=1.1)
        self.wait(14.0)

        final_line = Text(
            "Key idea: reward feedback shapes better sequential decisions.",
            font_size=TYPOGRAPHY.small_size,
            color=PALETTE.text_muted,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(final_line), run_time=0.6)
        self.wait(11.0)
