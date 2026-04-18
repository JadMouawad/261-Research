"""References block used in the final scene."""

from manim import DOWN, LEFT, RoundedRectangle, Text, VGroup

from ..constants import PALETTE, TYPOGRAPHY


class ReferenceList(VGroup):
    """Compact, readable reference list for educational slides."""

    def __init__(self, references: list[str], title: str = "References"):
        super().__init__()
        heading = Text(title, font_size=TYPOGRAPHY.subtitle_size, color=PALETTE.text_primary, weight="BOLD")
        rows = VGroup(*[Text(f"• {ref}", font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary) for ref in references])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        content = VGroup(heading, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        panel = RoundedRectangle(width=max(10.8, content.width + 0.6), height=max(3.5, content.height + 0.5), corner_radius=0.12)
        panel.set_fill("#161B22", opacity=0.92).set_stroke(PALETTE.text_muted, width=1.2)
        content.move_to(panel.get_center())
        self.add(panel, content)

