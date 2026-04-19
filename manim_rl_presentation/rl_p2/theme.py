"""Theme helper to keep visual language consistent."""

from manim import Rectangle

from .constants import PALETTE


class PresentationTheme:
    """Centralized visual style values used by components and scenes."""

    def __init__(self) -> None:
        self.background_color = PALETTE.background
        self.card_stroke = PALETTE.text_muted
        self.card_fill = "#161B22"
        self.card_fill_opacity = 0.85

    def card(self, width: float, height: float, corner_radius: float = 0.1) -> Rectangle:
        """Reusable card panel."""
        panel = Rectangle(width=width, height=height)
        panel.round_corners(corner_radius)
        panel.set_fill(self.card_fill, opacity=self.card_fill_opacity)
        panel.set_stroke(self.card_stroke, width=1.5)
        return panel

