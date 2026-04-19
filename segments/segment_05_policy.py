from manim import *
from p1_style import P1_BACKGROUND, animate_title_block, make_title_block


class Segment5Policy(Scene):
    def construct(self):
        self.camera.background_color = P1_BACKGROUND
        title_block = make_title_block("Policy", 58, "From many choices to one preferred action")
        title, title_rule, subtitle = title_block

        state_pos = LEFT * 2.8 + DOWN * 0.2
        good_end = RIGHT * 3.0 + UP * 1.1
        alt_end_1 = RIGHT * 3.2 + DOWN * 0.1
        alt_end_2 = RIGHT * 2.9 + DOWN * 1.5
        alt_end_3 = RIGHT * 1.9 + UP * 1.9

        agent = Dot(state_pos, radius=0.15, color=BLUE)
        state_ring = Circle(radius=0.34, stroke_color=BLUE_B, stroke_width=3).move_to(state_pos).set_opacity(0.0)

        start_anchor = state_pos + RIGHT * 0.16

        path_good = ArcBetweenPoints(start_anchor, good_end, angle=-0.16)
        path_alt_1 = ArcBetweenPoints(start_anchor, alt_end_1, angle=-0.02)
        path_alt_2 = ArcBetweenPoints(start_anchor, alt_end_2, angle=0.20)
        path_alt_3 = ArcBetweenPoints(start_anchor, alt_end_3, angle=-0.34)

        return_good_signal = ArcBetweenPoints(good_end, start_anchor, angle=0.35)
        move_good_agent = ArcBetweenPoints(state_pos, good_end, angle=-0.16)
        return_good_agent = ArcBetweenPoints(good_end, state_pos, angle=0.35)

        arrow_good = CurvedArrow(
            start_point=start_anchor,
            end_point=good_end,
            angle=-0.16,
            color=GRAY_B,
            stroke_width=4,
        )
        arrow_alt_1 = CurvedArrow(
            start_point=start_anchor,
            end_point=alt_end_1,
            angle=-0.02,
            color=GRAY_B,
            stroke_width=4,
        )
        arrow_alt_2 = CurvedArrow(
            start_point=start_anchor,
            end_point=alt_end_2,
            angle=0.20,
            color=GRAY_B,
            stroke_width=4,
        )
        arrow_alt_3 = CurvedArrow(
            start_point=start_anchor,
            end_point=alt_end_3,
            angle=-0.34,
            color=GRAY_B,
            stroke_width=4,
        )

        end_good = Dot(good_end, radius=0.08, color=GRAY_C)
        end_alt_1 = Dot(alt_end_1, radius=0.07, color=GRAY_D)
        end_alt_2 = Dot(alt_end_2, radius=0.07, color=GRAY_D)
        end_alt_3 = Dot(alt_end_3, radius=0.07, color=GRAY_D)

        choice_signal = Dot(start_anchor, radius=0.075, color=BLUE_B)
        reward_text = Text("+1", font_size=42, color=GREEN_B).move_to(good_end + RIGHT * 0.55 + UP * 0.15)
        reward_glow = Circle(radius=0.20, stroke_color=GREEN_B, stroke_width=4).move_to(good_end).set_opacity(0.0)

        arrows = VGroup(arrow_good, arrow_alt_1, arrow_alt_2, arrow_alt_3)
        endpoints = VGroup(end_good, end_alt_1, end_alt_2, end_alt_3)

        animate_title_block(self, title_block, run_time=2.0)

        self.play(FadeIn(agent), FadeIn(state_ring), run_time=1.4)
        self.play(FadeIn(arrows), FadeIn(endpoints), run_time=1.8)
        self.play(
            state_ring.animate.set_opacity(0.95).scale(1.08),
            rate_func=there_and_back,
            run_time=0.8,
        )

        self.play(arrow_alt_1.animate.set_stroke(color=BLUE_C, width=5), run_time=0.8)
        self.play(arrow_alt_3.animate.set_stroke(color=BLUE_C, width=5), run_time=0.8)
        self.play(arrow_good.animate.set_stroke(color=BLUE_C, width=5), run_time=0.8)
        self.play(arrow_alt_2.animate.set_stroke(color=BLUE_C, width=5), run_time=0.8)
        self.play(
            arrows.animate.set_stroke(color=GRAY_B, width=4),
            state_ring.animate.set_opacity(0.55),
            run_time=0.8,
        )

        self.play(FadeIn(choice_signal), MoveAlongPath(choice_signal, path_alt_2), run_time=1.0)
        self.play(choice_signal.animate.move_to(start_anchor), run_time=0.2)
        self.play(MoveAlongPath(choice_signal, path_alt_1), run_time=0.9)
        self.play(choice_signal.animate.move_to(start_anchor), run_time=0.2)
        self.play(MoveAlongPath(choice_signal, path_alt_3), run_time=0.9)
        self.play(choice_signal.animate.move_to(start_anchor), run_time=0.2)
        self.play(MoveAlongPath(choice_signal, path_good), run_time=0.6)

        self.play(
            arrow_good.animate.set_stroke(color=TEAL_B, width=5.5, opacity=0.95),
            end_good.animate.set_color(TEAL_B).scale(1.08),
            run_time=1.8,
        )
        self.play(
            MoveAlongPath(choice_signal, return_good_signal),
            state_ring.animate.set_opacity(0.7),
            run_time=0.7,
        )
        self.play(
            MoveAlongPath(choice_signal, path_good),
            ShowPassingFlash(path_good.copy().set_stroke(color=TEAL_B, width=6), time_width=0.35),
            run_time=1.5,
        )

        self.play(
            arrow_alt_1.animate.set_stroke(color=GRAY_D, opacity=0.2, width=2.5),
            arrow_alt_3.animate.set_stroke(color=GRAY_D, opacity=0.18, width=2.2),
            end_alt_1.animate.set_opacity(0.25),
            end_alt_3.animate.set_opacity(0.2),
            run_time=2.0,
        )
        self.play(
            arrow_alt_2.animate.set_stroke(color=RED_D, opacity=0.28, width=2.6),
            end_alt_2.animate.set_opacity(0.3),
            run_time=1.0,
        )
        self.play(
            MoveAlongPath(choice_signal, return_good_signal),
            arrow_alt_2.animate.set_stroke(color=GRAY_D, opacity=0.24, width=2.3),
            run_time=1.0,
        )

        self.play(
            arrow_good.animate.set_stroke(color=GREEN_B, width=7, opacity=1.0),
            end_good.animate.set_color(GREEN_B).scale(1.1),
            run_time=2.0,
        )
        self.play(
            MoveAlongPath(choice_signal, path_good),
            FadeIn(reward_text),
            reward_glow.animate.set_opacity(0.9).scale(1.2),
            run_time=2.0,
        )
        self.play(
            MoveAlongPath(choice_signal, return_good_signal),
            FadeOut(reward_text),
            reward_glow.animate.set_opacity(0.0).scale(1 / 1.2),
            run_time=2.0,
        )
        self.play(
            MoveAlongPath(choice_signal, path_good),
            ShowPassingFlash(path_good.copy().set_stroke(color=GREEN_B, width=7), time_width=0.35),
            run_time=2.0,
        )

        self.play(MoveAlongPath(agent, move_good_agent), run_time=1.6)
        self.play(MoveAlongPath(agent, return_good_agent), run_time=1.4)
        self.play(MoveAlongPath(agent, move_good_agent), run_time=1.6)
        self.play(MoveAlongPath(agent, return_good_agent), run_time=1.4)

        self.play(
            state_ring.animate.set_opacity(0.65),
            arrow_good.animate.set_stroke(color=GREEN_C, width=7.5, opacity=1.0),
            run_time=1.2,
        )
        self.play(
            MoveAlongPath(agent, move_good_agent),
            MoveAlongPath(choice_signal, path_good),
            run_time=2.4,
        )
        self.play(
            MoveAlongPath(agent, return_good_agent),
            MoveAlongPath(choice_signal, return_good_signal),
            run_time=2.4,
        )

        self.play(
            MoveAlongPath(choice_signal, path_good),
            FadeIn(reward_text),
            reward_glow.animate.set_opacity(0.85),
            run_time=1.8,
        )
        self.play(
            MoveAlongPath(choice_signal, return_good_signal),
            FadeOut(reward_text),
            reward_glow.animate.set_opacity(0.0),
            run_time=1.7,
        )
        self.play(
            MoveAlongPath(agent, move_good_agent),
            ShowPassingFlash(path_good.copy().set_stroke(color=GREEN_B, width=7), time_width=0.3),
            run_time=1.5,
        )
        self.play(
            MoveAlongPath(agent, return_good_agent),
            FadeOut(choice_signal),
            state_ring.animate.set_opacity(0.78),
            run_time=1.5,
        )
        self.play(
            FadeOut(
                VGroup(
                    title,
                    title_rule,
                    subtitle,
                    agent,
                    state_ring,
                    arrows,
                    endpoints,
                    choice_signal,
                    reward_text,
                    reward_glow,
                )
            ),
            run_time=1.24,
        )
