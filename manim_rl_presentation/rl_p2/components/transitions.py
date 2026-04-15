"""Small transition helpers to keep scene code readable."""

from manim import AnimationGroup, FadeIn, FadeOut, ReplacementTransform


def crossfade(old_mobject, new_mobject):
    return AnimationGroup(FadeOut(old_mobject), FadeIn(new_mobject), lag_ratio=0.0)


def morph(old_mobject, new_mobject):
    return ReplacementTransform(old_mobject, new_mobject)


def fade_to_black(*mobjects):
    return AnimationGroup(*[FadeOut(m) for m in mobjects], lag_ratio=0.04)

