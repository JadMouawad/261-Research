"""Scene 12: Whole-presentation conclusion and references."""

from pathlib import Path
import sys

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, LaggedStart, RoundedRectangle, Text, VGroup

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
    """Final close for the whole project, then references."""

    def construct(self):
        header = SceneHeader("Conclusion and References")
        header.animate_in(self)
        self.wait(1.2)

        # Whole-talk recap strip (segments 1-12 condensed into six milestones).
        milestones = [
            "Trial and error",
            "Agent-environment loop",
            "Core RL components",
            "Explore vs exploit",
            "Q-learning updates",
            "DQN + applications",
        ]
        cards = VGroup()
        for text in milestones:
            panel = RoundedRectangle(width=3.8, height=0.72, corner_radius=0.08)
            panel.set_fill("#161B22", opacity=0.9).set_stroke(PALETTE.text_muted, width=1.0)
            label = Text(text, font_size=TYPOGRAPHY.small_size - 4, color=PALETTE.text_primary)
            label.move_to(panel.get_center())
            cards.add(VGroup(panel, label))
        cards.arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(LEFT, buff=0.7).shift(DOWN * 0.05)

        recap_title = Text("Full presentation recap", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent, weight="BOLD")
        recap_title.next_to(cards, UP, aligned_edge=LEFT, buff=0.2)

        self.play(FadeIn(recap_title), run_time=0.5)
        for card in cards:
            self.play(FadeIn(card), run_time=0.45)
            self.wait(0.35)
        self.wait(1.8)
        self.wait(6.5)

        takeaway_lines = VGroup(
            Text("Final takeaway", font_size=TYPOGRAPHY.small_size, color=PALETTE.accent, weight="BOLD"),
            Text(
                "Reinforcement Learning improves decisions\nfrom feedback over time.",
                font_size=TYPOGRAPHY.small_size - 4,
                color=PALETTE.text_primary,
            ),
            Text("Q-learning is the core idea; DQN makes it scale.", font_size=TYPOGRAPHY.small_size - 4, color=PALETTE.text_primary),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        takeaway_panel = RoundedRectangle(width=7.5, height=2.2, corner_radius=0.12)
        takeaway_panel.set_fill("#161B22", opacity=0.92).set_stroke(PALETTE.text_muted, width=1.1)
        takeaway_lines.move_to(takeaway_panel.get_center()).align_to(takeaway_panel, LEFT).shift(RIGHT * 0.25)
        takeaway = VGroup(takeaway_panel, takeaway_lines)
        takeaway.next_to(cards, RIGHT, buff=0.7, aligned_edge=UP).shift(DOWN * 0.12)

        self.play(FadeIn(takeaway_panel), run_time=0.55)
        self.play(LaggedStart(*[FadeIn(line) for line in takeaway_lines], lag_ratio=0.2), run_time=1.2)
        self.wait(7.0)

        refs = ReferenceList(
            [
                "Sutton & Barto (2018), Reinforcement Learning: An Introduction",
                "Mnih et al. (2015), Nature: Human-level control through deep RL",
                "OpenAI Spinning Up: RL Intro",
                "David Silver RL Course (UCL)",
                "Lilian Weng: RL Overview",
                "Berkeley CS285 lecture notes",
            ]
        ).scale(0.74)
        refs.to_edge(RIGHT, buff=0.62).shift(DOWN * 1.55)

        self.play(FadeIn(refs[0]), run_time=0.8)
        self.play(FadeIn(refs[1][0]), run_time=0.45)
        ref_rows = refs[1][1]
        for row in ref_rows:
            self.play(FadeIn(row), run_time=0.32)
        self.wait(1.2)
        self.wait(9.0)

        closing = Text("Thank you.", font_size=TYPOGRAPHY.subtitle_size, color=PALETTE.accent, weight="BOLD").to_edge(DOWN, buff=0.25)
        self.play(FadeOut(refs), FadeOut(takeaway), FadeOut(cards), FadeOut(recap_title), run_time=0.5)
        self.play(FadeIn(closing), run_time=0.5)
        self.wait(2.5)
        self.play(FadeOut(closing), run_time=0.4)
