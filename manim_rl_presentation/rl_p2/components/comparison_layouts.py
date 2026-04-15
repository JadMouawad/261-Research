"""Symmetric comparison layouts."""

from manim import DOWN, LEFT, RIGHT, RoundedRectangle, Text, VGroup

from ..constants import PALETTE, TYPOGRAPHY


class ComparisonColumns(VGroup):
    """Reusable two-column card layout for strengths vs limitations."""

    def __init__(self, left_title: str, left_items: list[str], right_title: str, right_items: list[str]):
        super().__init__()
        left = self._build_column(left_title, left_items, "#132A1B")
        right = self._build_column(right_title, right_items, "#2A1515")
        cols = VGroup(left, right).arrange(RIGHT, buff=0.6)
        self.add(cols)

    @staticmethod
    def _build_column(title: str, items: list[str], fill_color: str) -> VGroup:
        title_txt = Text(title, font_size=TYPOGRAPHY.subtitle_size, color=PALETTE.text_primary, weight="BOLD")
        bullets = VGroup(*[Text(f"- {item}", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary) for item in items])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.17)
        body = VGroup(title_txt, bullets).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        panel = RoundedRectangle(width=max(5.6, body.width + 0.6), height=max(3.2, body.height + 0.5), corner_radius=0.12)
        panel.set_fill(fill_color, opacity=0.75).set_stroke(PALETTE.text_muted, width=1.2)
        body.move_to(panel.get_center())
        return VGroup(panel, body)
