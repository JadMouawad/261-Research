"""Header/title helpers."""

from manim import DOWN, LEFT, UP, Line, Text, VGroup

from ..constants import PALETTE, TYPOGRAPHY


class SceneHeader(VGroup):
    """Top-of-scene title with an understated separator line."""

    def __init__(self, title: str, subtitle: str | None = None):
        super().__init__()
        title_text = Text(title, color=PALETTE.text_primary, font_size=TYPOGRAPHY.title_size, weight="BOLD")
        title_text.to_edge(LEFT, buff=0.65).to_edge(UP, buff=0.35)
        line = Line(title_text.get_left() + DOWN * 0.22, title_text.get_right() + DOWN * 0.22, color=PALETTE.text_muted)
        self.add(title_text, line)
        if subtitle:
            subtitle_text = Text(subtitle, color=PALETTE.text_muted, font_size=TYPOGRAPHY.small_size)
            subtitle_text.next_to(line, DOWN, aligned_edge=LEFT, buff=0.18)
            self.add(subtitle_text)
