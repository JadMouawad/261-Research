from manim import *


class Segment1TrialAndError(Scene):
    def construct(self):
        title = Text("Trial and Error", font_size=60, color=WHITE).to_edge(UP, buff=0.45)

        start = LEFT * 1.4 + DOWN * 2.0
        bad_end = RIGHT * 3.7 + DOWN * 1.6
        good_end = LEFT * 4.6 + DOWN * 1.2

        platform = Line(LEFT * 6.2 + DOWN * 2.35, RIGHT * 6.2 + DOWN * 2.35).set_stroke(
            color=GRAY_B, width=2, opacity=0.45
        )

        agent = Dot(start, radius=0.14, color=BLUE)

        bad_path = CubicBezier(
            start,
            start + RIGHT * 1.6 + UP * 0.7,
            bad_end + LEFT * 1.1 + UP * 0.4,
            bad_end,
        ).set_stroke(color=GRAY_C, width=5, opacity=0.75)

        good_path = CubicBezier(
            start,
            start + LEFT * 1.2 + UP * 1.0,
            good_end + RIGHT * 1.1 + UP * 0.3,
            good_end,
        ).set_stroke(color=GRAY_C, width=5, opacity=0.75)

        bad_return = ArcBetweenPoints(bad_end, start, angle=PI / 5)
        good_return = ArcBetweenPoints(good_end, start, angle=-PI / 6)

        red_x = Text("X", font_size=60, color=RED).move_to(bad_end + UP * 0.65)
        plus_one = Text("+1", font_size=52, color=GREEN).move_to(good_end + UP * 0.65)

        reward_value = ValueTracker(0)
        reward_label = Text("Rewards:", font_size=34, color=WHITE).to_corner(UR, buff=0.6)
        reward_num = Text("0", font_size=38, color=GREEN).next_to(reward_label, RIGHT, buff=0.16)
        reward_num.add_updater(
            lambda m: m.become(
                Text(str(int(reward_value.get_value())), font_size=38, color=GREEN).move_to(m.get_center())
            )
        )
        reward_counter = VGroup(reward_label, reward_num)
        reward_counter.set_opacity(0)

        path_group = VGroup(bad_path, good_path)

        self.add(platform)

        self.play(Write(title), run_time=2.0)

        self.play(title.animate.scale(1.04), run_time=1.5)
        self.play(title.animate.scale(1 / 1.04), run_time=1.5)

        self.play(FadeIn(agent, scale=0.85), run_time=1.2)
        self.play(agent.animate.shift(UP * 0.10), rate_func=there_and_back, run_time=1.8)

        self.play(MoveAlongPath(agent, bad_path), run_time=2.2, rate_func=smooth)
        self.play(FadeIn(red_x), run_time=0.8)

        self.play(FadeOut(red_x), run_time=0.5)
        self.play(MoveAlongPath(agent, bad_return), run_time=2.5, rate_func=smooth)

        self.play(MoveAlongPath(agent, good_path), run_time=3.0, rate_func=smooth)
        self.play(FadeIn(plus_one), run_time=0.7)
        self.wait(0.3)

        self.play(FadeOut(plus_one), run_time=0.4)
        self.play(MoveAlongPath(agent, good_return), run_time=0.8, rate_func=smooth)
        self.play(MoveAlongPath(agent, good_path), run_time=1.8, rate_func=smooth)

        reward_value.set_value(1)
        self.play(FadeIn(reward_counter), FadeIn(plus_one), run_time=0.8)
        self.play(reward_value.animate.set_value(2), plus_one.animate.scale(1.18), run_time=1.0)
        self.play(plus_one.animate.scale(1 / 1.18), run_time=0.2)
        self.play(FadeOut(plus_one), run_time=0.6)
        self.play(MoveAlongPath(agent, good_return), run_time=1.2, rate_func=smooth)
        self.wait(0.2)

        self.play(Create(path_group), run_time=1.0)
        self.play(MoveAlongPath(agent, bad_path), run_time=1.2, rate_func=smooth)
        self.play(FadeIn(red_x), run_time=0.5)
        self.play(FadeOut(red_x), MoveAlongPath(agent, bad_return), run_time=0.8, rate_func=smooth)
        self.play(MoveAlongPath(agent, good_path), run_time=1.2, rate_func=smooth)
        self.play(FadeIn(plus_one), run_time=0.3)

        self.play(FadeOut(plus_one), run_time=0.5)
        self.play(MoveAlongPath(agent, good_return), run_time=1.0, rate_func=smooth)
        self.play(bad_path.animate.set_stroke(color=GRAY_D, width=3, opacity=0.25), run_time=1.5)
        bad_partial = bad_path.copy()
        bad_partial.pointwise_become_partial(bad_path, 0, 0.45)
        self.play(MoveAlongPath(agent, bad_partial), run_time=1.0, rate_func=smooth)
        self.play(agent.animate.move_to(start), run_time=1.0)

        self.play(good_path.animate.set_stroke(color=GREEN_B, width=8, opacity=1.0), run_time=1.5)
        self.play(MoveAlongPath(agent, good_path), run_time=2.0, rate_func=smooth)
        self.play(FadeIn(plus_one), run_time=0.5)
        self.play(reward_value.animate.set_value(3), run_time=0.8)
        self.play(FadeOut(plus_one), run_time=0.2)

        smooth_good_path = CubicBezier(
            start,
            start + LEFT * 1.6 + UP * 1.15,
            good_end + RIGHT * 1.4 + UP * 0.6,
            good_end,
        ).set_stroke(color=GREEN_C, width=9, opacity=1.0)
        self.play(MoveAlongPath(agent, good_return), run_time=1.0, rate_func=smooth)
        self.play(Transform(good_path, smooth_good_path), run_time=1.2)
        self.play(MoveAlongPath(agent, good_path), run_time=2.3, rate_func=smooth)
        self.play(reward_value.animate.set_value(4), run_time=0.5)

        self.play(
            FadeOut(
                VGroup(
                    title,
                    platform,
                    path_group,
                    agent,
                    red_x,
                    plus_one,
                    reward_counter,
                )
            ),
            run_time=3.5,
        )
        self.wait(1.5)
