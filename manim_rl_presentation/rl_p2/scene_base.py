"""Base scene with shared helpers for Person 2 scenes."""

from manim import FadeOut, Scene, VGroup

from .theme import PresentationTheme
from .timings import TIMINGS


class P2BaseScene(Scene):
    """Common utilities for styling, pacing, and transitions."""

    def setup(self) -> None:
        self.theme = PresentationTheme()
        self.camera.background_color = self.theme.background_color

    def pause_for(self, beat: str = "normal") -> None:
        """Small, named pauses aligned to narration beats."""
        self.wait(TIMINGS.get(beat, 0.8))

    def fade_out_group(self, *mobjects) -> None:
        """Fade out multiple objects with a single call."""
        group = VGroup(*mobjects)
        self.play(FadeOut(group))

