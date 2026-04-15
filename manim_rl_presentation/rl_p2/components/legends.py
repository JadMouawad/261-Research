"""Legend and chip helpers."""

from manim import DOWN, LEFT, RIGHT, RoundedRectangle, Text, VGroup

from ..constants import LAYOUT, PALETTE, TYPOGRAPHY


def make_legend(items: list[tuple[str, str]]) -> VGroup:
    """Create a small floating legend with color chips and labels."""
    rows = VGroup()
    for color, label in items:
        chip = RoundedRectangle(width=0.28, height=0.28, corner_radius=0.06)
        chip.set_fill(color, opacity=1).set_stroke(color, width=0)
        txt = Text(label, font_size=TYPOGRAPHY.small_size, color=PALETTE.text_primary)
        row = VGroup(chip, txt).arrange(RIGHT, buff=0.12)
        rows.add(row)
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.08)

    panel = RoundedRectangle(width=rows.width + 0.36, height=rows.height + 0.3, corner_radius=0.12)
    panel.set_fill("#161B22", opacity=0.9).set_stroke(PALETTE.text_muted, width=1.2)
    panel.move_to(rows)
    group = VGroup(panel, rows)
    group.to_corner(LEFT + DOWN, buff=LAYOUT.edge_margin)
    return group

