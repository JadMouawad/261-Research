from manim import *


class Segment3CoreComponents(Scene):
    def construct(self):
        title = Text("Core Components", font_size=56, color=WHITE).to_edge(UP, buff=0.4)

        state_1 = LEFT * 4.1 + DOWN * 0.8
        state_2 = LEFT * 3.3 + UP * 0.2

        env_panel = RoundedRectangle(
            width=4.7,
            height=3.2,
            corner_radius=0.22,
            stroke_color=GRAY_B,
            stroke_width=3,
            fill_color=GRAY_E,
            fill_opacity=0.18,
        ).move_to(RIGHT * 2.6 + DOWN * 0.4)

        env_core = Circle(
            radius=0.34,
            stroke_color=BLUE_D,
            stroke_width=2.5,
            fill_color=BLUE_D,
            fill_opacity=0.55,
        ).move_to(env_panel.get_center())

        env_top = env_panel.get_left() + RIGHT * 0.06 + UP * 0.55
        env_bottom = env_panel.get_left() + RIGHT * 0.06 + DOWN * 0.62
        env_feedback = env_panel.get_left() + LEFT * 0.02 + DOWN * 0.35

        agent = Dot(state_1, radius=0.15, color=BLUE)
        state_ring = Circle(radius=0.34, stroke_color=BLUE_B, stroke_width=3).move_to(state_1).set_opacity(0)

        tag = Text("State", font_size=30, color=GRAY_A).to_edge(DOWN, buff=0.55)

        good_action_path_1 = ArcBetweenPoints(state_1 + RIGHT * 0.16, env_top, angle=-0.25)
        bad_action_path_1 = ArcBetweenPoints(state_1 + RIGHT * 0.16, env_bottom, angle=0.18)

        good_action = CurvedArrow(
            start_point=state_1 + RIGHT * 0.16,
            end_point=env_top,
            angle=-0.25,
            stroke_width=4,
            color=GRAY_C,
        ).set_opacity(0)
        bad_action = CurvedArrow(
            start_point=state_1 + RIGHT * 0.16,
            end_point=env_bottom,
            angle=0.18,
            stroke_width=4,
            color=GRAY_C,
        ).set_opacity(0)

        feedback_path_1 = ArcBetweenPoints(env_feedback, state_1 + RIGHT * 0.15 + UP * 0.2, angle=-0.95)
        feedback_arrow = CurvedArrow(
            start_point=env_feedback,
            end_point=state_1 + RIGHT * 0.15 + UP * 0.2,
            angle=-0.95,
            stroke_width=4,
            color=GRAY_C,
        ).set_opacity(0)

        transition_path = ArcBetweenPoints(state_1, state_2, angle=0.55)

        good_action_path_2 = ArcBetweenPoints(state_2 + RIGHT * 0.16, env_top, angle=-0.18)
        bad_action_path_2 = ArcBetweenPoints(state_2 + RIGHT * 0.16, env_bottom, angle=0.12)
        good_action_new = CurvedArrow(
            start_point=state_2 + RIGHT * 0.16,
            end_point=env_top,
            angle=-0.18,
            stroke_width=4,
            color=GRAY_C,
        )
        bad_action_new = CurvedArrow(
            start_point=state_2 + RIGHT * 0.16,
            end_point=env_bottom,
            angle=0.12,
            stroke_width=4,
            color=GRAY_C,
        )

        feedback_path_2 = ArcBetweenPoints(env_feedback, state_2 + RIGHT * 0.15 + DOWN * 0.05, angle=-1.0)
        feedback_arrow_new = CurvedArrow(
            start_point=env_feedback,
            end_point=state_2 + RIGHT * 0.15 + DOWN * 0.05,
            angle=-1.0,
            stroke_width=4,
            color=GRAY_C,
        )

        self_loop = CurvedArrow(
            start_point=state_2 + DOWN * 0.3,
            end_point=state_2 + UP * 0.3,
            angle=-3.9,
            stroke_width=4,
            color=GRAY_C,
        ).set_opacity(0)

        action_signal = Dot(radius=0.075, color=BLUE_B).move_to(good_action_path_1.get_start())
        feedback_signal = Dot(radius=0.085, color=GREEN_B).move_to(feedback_path_1.get_start())
        red_signal = Dot(radius=0.085, color=RED_B).move_to(bad_action_path_2.get_start())
        loop_signal = Dot(radius=0.07, color=BLUE_C).move_to(self_loop.get_start())

        reward_text = Text("+1", font_size=42, color=GREEN_B).move_to(env_panel.get_center() + UP * 0.85 + RIGHT * 0.95)
        penalty_text = Text("-1", font_size=42, color=RED_B).move_to(env_panel.get_center() + DOWN * 0.85 + RIGHT * 0.95)

        self.play(Write(title), run_time=2.0)

        self.play(FadeIn(agent), FadeIn(env_panel), FadeIn(env_core), run_time=2.0)
        self.play(env_core.animate.scale(1.13), rate_func=there_and_back, run_time=2.0)

        self.play(FadeIn(state_ring), FadeIn(tag), run_time=1.4)
        self.play(
            state_ring.animate.set_opacity(0.95).scale(1.08),
            agent.animate.scale(1.06),
            rate_func=there_and_back,
            run_time=1.6,
        )
        self.play(state_ring.animate.set_stroke(opacity=0.45), run_time=1.0)

        action_tag = Text("Action", font_size=30, color=GRAY_A).move_to(tag)
        self.play(
            FadeIn(good_action),
            FadeIn(bad_action),
            ReplacementTransform(tag, action_tag),
            run_time=1.5,
        )
        tag = action_tag
        self.play(FadeIn(action_signal), MoveAlongPath(action_signal, bad_action_path_1), run_time=1.2)
        self.play(
            FadeOut(action_signal),
            good_action.animate.set_stroke(color=BLUE_B, width=5, opacity=1.0),
            bad_action.animate.set_stroke(opacity=0.55),
            run_time=1.3,
        )

        reward_tag = Text("Reward", font_size=30, color=GRAY_A).move_to(tag)
        self.play(ReplacementTransform(tag, reward_tag), run_time=0.8)
        tag = reward_tag
        self.play(FadeIn(feedback_arrow), run_time=0.8)
        self.play(
            FadeIn(reward_text),
            FadeIn(feedback_signal),
            MoveAlongPath(feedback_signal, feedback_path_1),
            env_core.animate.set_color(GREEN_B),
            run_time=1.8,
        )
        self.play(
            FadeOut(reward_text),
            FadeOut(feedback_signal),
            env_core.animate.set_color(BLUE_D),
            run_time=0.6,
        )

        new_state_tag = Text("New State", font_size=30, color=GRAY_A).move_to(tag)
        self.play(ReplacementTransform(tag, new_state_tag), run_time=0.8)
        tag = new_state_tag
        self.play(
            MoveAlongPath(agent, transition_path),
            state_ring.animate.move_to(state_2),
            run_time=2.6,
        )
        self.play(env_core.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)

        loop_tag = Text("Loop", font_size=30, color=GRAY_A).move_to(tag)
        self.play(ReplacementTransform(tag, loop_tag), run_time=0.8)
        tag = loop_tag
        self.play(FadeIn(self_loop), run_time=0.8)
        self.play(
            Transform(good_action, good_action_new),
            Transform(bad_action, bad_action_new),
            Transform(feedback_arrow, feedback_arrow_new),
            run_time=1.2,
        )
        self.play(
            FadeIn(loop_signal),
            MoveAlongPath(loop_signal, self_loop),
            run_time=1.2,
        )

        self.play(
            FadeOut(loop_signal),
            FadeIn(action_signal),
            MoveAlongPath(action_signal, good_action_path_2),
            env_core.animate.set_color(BLUE_E),
            run_time=1.8,
        )
        self.play(
            FadeOut(action_signal),
            FadeIn(feedback_signal),
            MoveAlongPath(feedback_signal, feedback_path_2),
            FadeIn(loop_signal),
            run_time=2.0,
        )
        self.play(
            FadeOut(feedback_signal),
            MoveAlongPath(loop_signal, self_loop),
            env_core.animate.set_color(BLUE_D),
            run_time=2.2,
        )

        self.play(
            bad_action.animate.set_stroke(color=RED_D, width=5, opacity=0.9),
            FadeIn(penalty_text),
            run_time=1.2,
        )
        self.play(
            FadeIn(red_signal),
            MoveAlongPath(red_signal, bad_action_path_2),
            env_core.animate.set_color(RED_D),
            run_time=2.0,
        )
        self.play(
            FadeOut(red_signal),
            FadeOut(penalty_text),
            FadeIn(action_signal),
            MoveAlongPath(action_signal, good_action_path_2),
            FadeIn(feedback_signal),
            MoveAlongPath(feedback_signal, feedback_path_2),
            env_core.animate.set_color(GREEN_B),
            run_time=2.0,
        )
        self.play(
            FadeOut(action_signal),
            FadeOut(feedback_signal),
            env_core.animate.set_color(BLUE_D),
            run_time=0.8,
        )

        self.play(
            good_action.animate.set_stroke(color=GREEN_B, width=6, opacity=1.0),
            feedback_arrow.animate.set_stroke(color=GREEN_B, width=5, opacity=0.95),
            run_time=1.5,
        )
        self.play(
            FadeIn(action_signal),
            MoveAlongPath(action_signal, good_action_path_2),
            FadeIn(reward_text),
            env_core.animate.set_color(GREEN_B),
            run_time=2.2,
        )
        self.play(
            FadeOut(action_signal),
            FadeIn(feedback_signal),
            MoveAlongPath(feedback_signal, feedback_path_2),
            FadeOut(reward_text),
            MoveAlongPath(loop_signal, self_loop),
            run_time=2.3,
        )

        self.play(
            bad_action.animate.set_stroke(opacity=0.15, width=2),
            run_time=2.0,
        )
        self.play(
            FadeOut(feedback_signal),
            FadeIn(action_signal),
            MoveAlongPath(action_signal, good_action_path_2),
            FadeIn(feedback_signal),
            MoveAlongPath(feedback_signal, feedback_path_2),
            run_time=2.0,
        )
        self.play(
            FadeOut(action_signal),
            MoveAlongPath(loop_signal, self_loop),
            tag.animate.set_opacity(0.0),
            env_core.animate.set_color(BLUE_D),
            run_time=2.0,
        )

        self.play(
            FadeIn(action_signal),
            MoveAlongPath(action_signal, good_action_path_2),
            FadeOut(feedback_signal),
            env_core.animate.set_color(GREEN_B),
            run_time=2.8,
        )
        self.play(
            FadeOut(action_signal),
            FadeIn(feedback_signal),
            MoveAlongPath(feedback_signal, feedback_path_2),
            MoveAlongPath(loop_signal, self_loop),
            run_time=2.8,
        )
        self.play(
            FadeOut(feedback_signal),
            FadeIn(action_signal),
            MoveAlongPath(action_signal, good_action_path_2),
            env_core.animate.set_color(BLUE_D),
            run_time=2.8,
        )
        self.play(
            FadeOut(action_signal),
            env_core.animate.scale(1.05),
            state_ring.animate.set_opacity(0.55),
            rate_func=there_and_back,
            run_time=0.8,
        )
        self.wait(0.8)
