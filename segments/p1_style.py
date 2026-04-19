from manim import AddTextLetterByLetter, AnimationGroup, Create, DOWN, LEFT, Line, Text, UL, VGroup, WHITE

P1_BACKGROUND = "#0D1117"
P1_TEXT = WHITE
P1_MUTED = "#A8B0BA"
P1_ACCENT = "#E4B15A"


def make_title_block(title: str, title_size: int, subtitle: str) -> VGroup:
    title_text = Text(title, font_size=title_size, color=P1_TEXT).to_corner(UL, buff=0.5)
    underline = Line(title_text.get_left(), title_text.get_right(), stroke_color=P1_TEXT, stroke_width=3).next_to(
        title_text, DOWN, buff=0.08
    )
    subtitle_text = Text(subtitle, font_size=max(22, int(title_size * 0.52)), color=P1_MUTED)
    subtitle_text.next_to(underline, DOWN, buff=0.14).align_to(title_text, LEFT)
    return VGroup(title_text, underline, subtitle_text)


def animate_title_block(scene, title_block: VGroup, run_time: float = 2.0) -> None:
    title_text, underline, subtitle = title_block
    scene.play(
        AnimationGroup(
            AddTextLetterByLetter(title_text),
            Create(underline),
            AddTextLetterByLetter(subtitle),
            lag_ratio=0.12,
        ),
        run_time=run_time,
    )
