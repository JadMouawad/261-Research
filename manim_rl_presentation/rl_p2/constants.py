"""Project-wide constants for Person 2 scenes."""

from dataclasses import dataclass

from manim import BLUE_D, GOLD_D, GREEN_D, GREY_B, RED_D, WHITE


@dataclass(frozen=True)
class Palette:
    background: str = "#0D1117"
    text_primary: str = WHITE
    text_muted: str = GREY_B
    agent: str = BLUE_D
    goal: str = GREEN_D
    bad: str = RED_D
    accent: str = GOLD_D


@dataclass(frozen=True)
class Typography:
    title_size: int = 44
    subtitle_size: int = 28
    body_size: int = 26
    small_size: int = 22


@dataclass(frozen=True)
class Layout:
    edge_margin: float = 0.5
    card_buff: float = 0.2
    grid_cell_size: float = 0.9
    standard_gap: float = 0.35


PALETTE = Palette()
TYPOGRAPHY = Typography()
LAYOUT = Layout()

