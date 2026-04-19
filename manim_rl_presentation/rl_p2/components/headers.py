"""Header/title helpers."""

from manim import AddTextLetterByLetter, Create, DOWN, FadeIn, LEFT, UP, Line, Text, VGroup

from ..constants import PALETTE, TYPOGRAPHY


class SceneHeader(VGroup):
    """Top-of-scene title with an understated separator line."""

    def __init__(self, title: str, subtitle: str | None = None):
        super().__init__()
        self.title_text = Text(title, color=PALETTE.text_primary, font_size=TYPOGRAPHY.title_size, weight="BOLD")
        self.title_text.to_edge(LEFT, buff=0.65).to_edge(UP, buff=0.35)
        # Place separator slightly below glyph descenders so it never strikes through text.
        y = self.title_text.get_bottom()[1] - 0.06
        self.line = Line(
            [self.title_text.get_left()[0], y, 0],
            [self.title_text.get_right()[0], y, 0],
            color=PALETTE.text_muted,
        )
        self.subtitle_text = None
        self.add(self.title_text, self.line)
        if subtitle:
            self.subtitle_text = Text(subtitle, color=PALETTE.text_muted, font_size=TYPOGRAPHY.small_size)
            self.subtitle_text.next_to(self.line, DOWN, aligned_edge=LEFT, buff=0.18)
            self.add(self.subtitle_text)

    def animate_in(self, scene, title_run_time: float = 1.7) -> None:
        """Animate title letters first, then the separator/subtitle."""
        scene.play(AddTextLetterByLetter(self.title_text), run_time=title_run_time)
        scene.play(Create(self.line), run_time=0.35)
        if self.subtitle_text is not None:
            scene.play(FadeIn(self.subtitle_text, shift=DOWN * 0.05), run_time=0.45)
