from manim import *


class Segment2WhatIsReinforcementLearning(Scene):
    def construct(self):
        title = Text("What Is Reinforcement Learning?", font_size=54, color=WHITE).to_edge(UP, buff=0.4)

        agent_center = LEFT * 4.2 + DOWN * 0.9
        agent = Dot(point=agent_center, radius=0.15, color=BLUE)

        env_panel = RoundedRectangle(
            width=4.6,
            height=3.1,
            corner_radius=0.22,
            stroke_color=GRAY_B,
            stroke_width=3,
            fill_color=GRAY_E,
            fill_opacity=0.18,
        ).move_to(RIGHT * 2.5 + DOWN * 0.7)

        env_core = Circle(
            radius=0.34,
            stroke_color=BLUE_D,
            stroke_width=2.5,
            fill_color=BLUE_D,
            fill_opacity=0.55,
        ).move_to(env_panel.get_center())

        action_start = agent.get_right() + RIGHT * 0.03
        action_end = env_panel.get_left() + RIGHT * 0.08
        action_path = Line(action_start, action_end)
        action_arrow = Arrow(
            start=action_start,
            end=action_end,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
            color=GRAY_C,
        )

        feedback_start = env_panel.get_left() + LEFT * 0.02 + DOWN * 0.45
        feedback_end = agent.get_right() + UP * 0.35
        feedback_path = ArcBetweenPoints(feedback_start, feedback_end, angle=-0.9)
        feedback_arrow = CurvedArrow(
            start_point=feedback_start,
            end_point=feedback_end,
            angle=-0.9,
            stroke_width=4,
            color=GRAY_C,
        )

        action_path_alt = CubicBezier(
            agent_center + RIGHT * 0.15 + UP * 0.28,
            LEFT * 1.2 + UP * 0.4,
            RIGHT * 1.1 + UP * 0.75,
            env_panel.get_left() + RIGHT * 0.08 + UP * 0.45,
        )

        good_start = agent_center + RIGHT * 0.15 + UP * 0.22
        good_end = env_panel.get_left() + RIGHT * 0.08 + UP * 0.58
        bad_end = env_panel.get_left() + RIGHT * 0.08 + DOWN * 0.72

        good_action_path = CubicBezier(
            good_start,
            LEFT * 1.6 + UP * 0.8,
            RIGHT * 1.1 + UP * 0.95,
            good_end,
        )
        bad_action_path = CubicBezier(
            agent_center + RIGHT * 0.15 + DOWN * 0.15,
            LEFT * 1.6 + DOWN * 1.1,
            RIGHT * 1.0 + DOWN * 1.45,
            bad_end,
        )

        good_arrow = Arrow(
            start=good_start,
            end=good_end,
            buff=0,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.12,
            color=GREEN_D,
        )
        bad_arrow = Arrow(
            start=agent_center + RIGHT * 0.15 + DOWN * 0.15,
            end=bad_end,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
            color=RED_D,
        ).set_opacity(0)

        counter_label = Text("Total Reward:", font_size=30, color=WHITE).to_corner(UR, buff=0.55)
        counter_number = Integer(0, mob_class=Text, font_size=34, color=GREEN_B).next_to(counter_label, RIGHT, buff=0.16)
        reward_counter = VGroup(counter_label, counter_number).set_opacity(0)

        action_signal = Dot(radius=0.07, color=BLUE_B).move_to(action_path.get_start())
        reward_token = Dot(radius=0.09, color=GREEN_B).move_to(feedback_path.point_from_proportion(0))
        penalty_token = Dot(radius=0.09, color=RED_B).move_to(feedback_path.point_from_proportion(0))
        small_token = Dot(radius=0.07, color=GREEN_A).move_to(feedback_path.point_from_proportion(0))
        big_token = Dot(radius=0.12, color=GREEN_C).move_to(feedback_path.point_from_proportion(0))
        green_action_signal = Dot(radius=0.08, color=GREEN_B).move_to(good_action_path.point_from_proportion(0))
        red_action_signal = Dot(radius=0.08, color=RED_B).move_to(bad_action_path.point_from_proportion(0))

        reward_text = Text("+2", font_size=44, color=GREEN_B).move_to(env_panel.get_right() + LEFT * 0.75 + UP * 0.7)
        penalty_text = Text("-1", font_size=44, color=RED_B).move_to(env_panel.get_right() + LEFT * 0.75 + DOWN * 0.7)
        small_reward_text = Text("+1", font_size=34, color=GREEN_A).move_to(env_panel.get_right() + LEFT * 0.8 + UP * 0.45)
        big_reward_text = Text("+3", font_size=52, color=GREEN_C).move_to(env_panel.get_right() + LEFT * 0.72 + UP * 0.82)

        self.play(Write(title), run_time=2.0)

        self.play(FadeIn(agent), FadeIn(env_panel), FadeIn(env_core), run_time=2.0)
        self.play(env_core.animate.scale(1.14), rate_func=there_and_back, run_time=2.0)

        self.play(Create(action_arrow), run_time=1.0)
        self.play(FadeIn(action_signal), MoveAlongPath(action_signal, action_path), run_time=2.0)
        self.play(FadeOut(action_signal), env_core.animate.set_color(TEAL_B).scale(1.08), run_time=0.5)
        self.play(env_core.animate.set_color(BLUE_D).scale(1 / 1.08), run_time=0.5)

        self.play(Create(feedback_arrow), run_time=0.9)
        self.play(FadeIn(reward_text), run_time=0.7)
        self.play(
            FadeIn(reward_token),
            MoveAlongPath(reward_token, feedback_path),
            env_core.animate.set_color(GREEN_B),
            run_time=1.8,
        )
        self.play(FadeOut(reward_text), FadeOut(reward_token), env_core.animate.set_color(BLUE_D), run_time=0.6)

        self.play(FadeIn(penalty_text), env_core.animate.set_color(RED_B), run_time=0.8)
        self.play(FadeIn(penalty_token), MoveAlongPath(penalty_token, feedback_path), run_time=1.8)
        self.play(FadeOut(penalty_text), FadeOut(penalty_token), run_time=0.8)
        self.play(env_core.animate.set_color(BLUE_D), run_time=0.6)

        self.play(agent.animate.shift(UP * 0.28), run_time=0.8)
        self.play(FadeIn(action_signal), MoveAlongPath(action_signal, action_path_alt), run_time=2.0)
        self.play(FadeOut(action_signal), env_core.animate.scale(1.1).set_color(TEAL_B), run_time=0.7)
        self.play(agent.animate.shift(DOWN * 0.28), env_core.animate.scale(1 / 1.1).set_color(BLUE_D), run_time=0.5)

        self.play(FadeIn(small_reward_text), run_time=0.7)
        self.play(
            FadeIn(small_token),
            MoveAlongPath(small_token, feedback_path),
            env_core.animate.set_color(GREEN_A),
            run_time=1.5,
        )
        self.play(FadeOut(small_reward_text), FadeOut(small_token), env_core.animate.set_color(BLUE_D), run_time=0.9)
        self.play(agent.animate.scale(1.06), rate_func=there_and_back, run_time=0.9)

        self.play(FadeIn(big_reward_text), run_time=0.7)
        self.play(
            FadeIn(big_token),
            MoveAlongPath(big_token, feedback_path),
            env_core.animate.set_color(GREEN_B),
            run_time=1.7,
        )
        self.play(FadeOut(big_reward_text), FadeOut(big_token), env_core.animate.set_color(BLUE_D), run_time=0.8)
        self.play(agent.animate.scale(1.12), rate_func=there_and_back, run_time=0.8)

        self.play(FadeIn(reward_counter), run_time=1.0)
        self.play(counter_number.animate.set_value(1), run_time=1.2)
        self.play(counter_number.animate.set_value(4), run_time=1.2)
        self.play(action_arrow.animate.set_stroke(color=GREEN_D, width=5), run_time=0.6)

        self.play(Transform(action_arrow, good_arrow), FadeIn(bad_arrow), run_time=1.5)
        self.play(
            FadeIn(red_action_signal),
            MoveAlongPath(red_action_signal, bad_action_path),
            env_core.animate.set_color(RED_D),
            run_time=1.2,
        )
        self.play(FadeOut(red_action_signal), env_core.animate.set_color(BLUE_D), run_time=0.3)
        self.play(
            FadeIn(green_action_signal),
            MoveAlongPath(green_action_signal, good_action_path),
            env_core.animate.set_color(GREEN_B),
            run_time=1.5,
        )
        self.play(
            MoveAlongPath(green_action_signal, good_action_path),
            counter_number.animate.set_value(5),
            run_time=1.2,
        )
        self.play(FadeOut(green_action_signal), env_core.animate.set_color(BLUE_D), run_time=0.3)

        self.play(bad_arrow.animate.set_stroke(opacity=0.12, width=2), run_time=1.8)
        self.play(FadeIn(red_action_signal), MoveAlongPath(red_action_signal, bad_action_path), run_time=1.1)
        self.play(FadeOut(red_action_signal), run_time=0.4)
        self.play(
            FadeIn(green_action_signal),
            MoveAlongPath(green_action_signal, good_action_path),
            env_core.animate.set_color(GREEN_B),
            run_time=1.3,
        )
        self.play(FadeOut(green_action_signal), env_core.animate.set_color(BLUE_D), run_time=0.4)

        self.play(
            action_arrow.animate.set_stroke(color=GREEN_B, width=6, opacity=1.0),
            feedback_arrow.animate.set_stroke(color=GREEN_B, width=5, opacity=0.9),
            run_time=0.9,
        )
        self.play(
            FadeIn(green_action_signal),
            MoveAlongPath(green_action_signal, good_action_path),
            env_core.animate.set_color(GREEN_B),
            run_time=1.0,
        )
        self.play(
            FadeOut(green_action_signal),
            FadeIn(reward_token),
            MoveAlongPath(reward_token, feedback_path),
            counter_number.animate.set_value(6),
            run_time=1.2,
        )
        self.play(
            FadeOut(reward_token),
            env_core.animate.set_color(BLUE_D),
            agent.animate.shift(UP * 0.05),
            rate_func=there_and_back,
            run_time=0.7,
        )
        self.play(
            env_core.animate.scale(1.05).set_color(GREEN_E),
            agent.animate.scale(1.04),
            rate_func=there_and_back,
            run_time=1.2,
        )
