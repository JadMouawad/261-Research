from manim import *


class Segment4InteractionLoop(Scene):
    def construct(self):
        title = Text("Interaction Loop", font_size=56, color=WHITE).to_edge(UP, buff=0.4)

        loop_path = Ellipse(width=8.0, height=4.8, color=GRAY_C, stroke_width=5).move_to(DOWN * 0.15)
        improved_loop = Ellipse(width=7.2, height=4.3, color=GRAY_C, stroke_width=5).move_to(DOWN * 0.15)
        direct_loop = Ellipse(width=6.5, height=3.8, color=GRAY_C, stroke_width=5).move_to(DOWN * 0.15)

        env_panel = RoundedRectangle(
            width=3.2,
            height=2.4,
            corner_radius=0.2,
            stroke_color=GRAY_B,
            stroke_width=3,
            fill_color=GRAY_E,
            fill_opacity=0.16,
        ).move_to(RIGHT * 3.35 + DOWN * 0.15)

        env_core = Circle(
            radius=0.28,
            stroke_color=BLUE_D,
            stroke_width=2.5,
            fill_color=BLUE_D,
            fill_opacity=0.58,
        ).move_to(env_panel.get_center())

        phase = ValueTracker(0.62)
        state_prop = ValueTracker(0.62)

        agent = Dot(radius=0.14, color=BLUE)
        agent.add_updater(lambda m: m.move_to(loop_path.point_from_proportion(phase.get_value() % 1)))

        state_ring = Circle(radius=0.33, stroke_color=BLUE_B, stroke_width=3).set_opacity(0.0)
        state_ring.add_updater(lambda m: m.move_to(loop_path.point_from_proportion(state_prop.get_value() % 1)))

        action_segment = loop_path.copy()
        action_segment.pointwise_become_partial(loop_path, 0.62, 0.84)

        action_pointer = Arrow(
            start=LEFT * 0.2,
            end=RIGHT * 0.2,
            buff=0,
            color=BLUE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
        ).move_to(loop_path.point_from_proportion(0.62))

        feedback_path = ArcBetweenPoints(
            env_panel.get_left() + LEFT * 0.05 + DOWN * 0.1,
            loop_path.point_from_proportion(0.84) + UP * 0.05,
            angle=-1.05,
        )

        reward_token = Dot(radius=0.09, color=GREEN_B).move_to(feedback_path.get_start())
        reward_text = Text("+1", font_size=42, color=GREEN_B).move_to(env_panel.get_center() + RIGHT * 0.85 + UP * 0.65)

        decision_a = Dot(radius=0.06, color=BLUE_C).set_opacity(0.0)
        decision_b = Dot(radius=0.05, color=BLUE_C).set_opacity(0.0)
        decision_a.add_updater(lambda m: m.move_to(loop_path.point_from_proportion(0.62)))
        decision_b.add_updater(lambda m: m.move_to(loop_path.point_from_proportion(0.70)))

        self.play(Write(title), run_time=1.1)
        self.play(Create(loop_path), run_time=0.9)
        self.play(FadeIn(env_panel), FadeIn(env_core), FadeIn(agent), run_time=0.7)

        self.play(FadeIn(state_ring), run_time=1.1)
        self.play(
            state_ring.animate.set_opacity(0.98).set_stroke(color=BLUE_B, width=4).scale(1.08),
            agent.animate.scale(1.06),
            rate_func=there_and_back,
            run_time=1.5,
        )
        self.play(state_ring.animate.set_opacity(0.5), run_time=1.1)

        self.play(FadeIn(action_pointer), run_time=0.5)
        self.play(
            MoveAlongPath(action_pointer, action_segment),
            phase.animate.set_value(0.84),
            loop_path.animate.set_stroke(color=BLUE_B, width=6),
            ShowPassingFlash(action_segment.copy().set_stroke(color=BLUE_C, width=7), time_width=0.35),
            run_time=2.3,
        )
        self.play(
            FadeOut(action_pointer),
            loop_path.animate.set_stroke(color=GRAY_C, width=5),
            run_time=0.9,
        )

        self.play(FadeIn(reward_text), env_core.animate.set_color(GREEN_B), run_time=0.9)
        self.play(
            FadeIn(reward_token),
            MoveAlongPath(reward_token, feedback_path),
            ShowPassingFlash(feedback_path.copy().set_stroke(color=GREEN_B, width=6), time_width=0.4),
            run_time=1.8,
        )
        self.play(
            FadeOut(reward_token),
            FadeOut(reward_text),
            env_core.animate.set_color(BLUE_D),
            run_time=1.2,
        )

        self.play(
            phase.animate.set_value(1.15),
            loop_path.animate.set_stroke(color=TEAL_B, width=5.5),
            run_time=2.6,
        )
        self.play(
            state_prop.animate.set_value(1.15),
            state_ring.animate.set_opacity(0.92).set_stroke(color=TEAL_B, width=4).scale(1.05),
            rate_func=there_and_back,
            run_time=1.4,
        )

        self.play(
            phase.animate.set_value(1.62),
            loop_path.animate.set_stroke(color=BLUE_C, width=6),
            run_time=3.0,
        )
        self.play(loop_path.animate.set_stroke(color=GRAY_C, width=5), run_time=1.0)

        self.play(phase.animate.set_value(2.30), run_time=2.4)
        self.play(
            FadeIn(reward_text),
            env_core.animate.set_color(GREEN_B).scale(1.08),
            rate_func=there_and_back,
            run_time=1.2,
        )
        self.play(
            FadeOut(reward_text),
            phase.animate.set_value(2.62),
            env_core.animate.set_color(BLUE_D),
            run_time=1.4,
        )

        self.play(Transform(loop_path, improved_loop), run_time=1.6)
        self.play(
            phase.animate.set_value(3.62),
            loop_path.animate.set_stroke(color=GREEN_D, width=5.5, opacity=0.92),
            run_time=3.4,
        )

        self.play(Transform(loop_path, direct_loop), run_time=1.5)
        self.play(
            phase.animate.set_value(4.62),
            state_ring.animate.set_opacity(0.35),
            run_time=3.5,
        )

        self.play(phase.animate.set_value(5.82), run_time=2.2)
        self.play(phase.animate.set_value(7.02), run_time=2.0)
        self.play(env_core.animate.set_color(GREEN_E).scale(1.08), rate_func=there_and_back, run_time=0.8)

        self.play(
            loop_path.animate.set_stroke(color=GREEN_B, width=6, opacity=0.95),
            env_core.animate.set_color(BLUE_D),
            run_time=1.0,
        )
        self.play(phase.animate.set_value(8.02), env_core.animate.set_color(GREEN_B), run_time=2.2)
        self.play(
            phase.animate.set_value(8.92),
            FadeIn(reward_token),
            MoveAlongPath(reward_token, feedback_path),
            run_time=2.0,
        )
        self.play(
            phase.animate.set_value(9.62),
            FadeOut(reward_token),
            env_core.animate.set_color(BLUE_D),
            run_time=1.8,
        )
        self.play(state_ring.animate.set_opacity(0.4), run_time=1.0)

        self.play(FadeIn(decision_a), FadeIn(decision_b), run_time=1.0)
        self.play(
            phase.animate.set_value(10.42),
            loop_path.animate.set_stroke(color=GREEN_B, width=6.2, opacity=0.96),
            run_time=2.5,
        )
        self.play(
            phase.animate.set_value(11.12),
            env_core.animate.set_color(BLUE_D),
            run_time=2.3,
        )
        self.play(
            phase.animate.set_value(11.82),
            env_core.animate.set_color(GREEN_B),
            run_time=2.1,
        )
        self.play(
            phase.animate.set_value(12.30),
            ShowPassingFlash(action_segment.copy().set_stroke(color=BLUE_C, width=7), time_width=0.35),
            env_core.animate.set_color(BLUE_D),
            run_time=1.3,
        )
        self.play(
            decision_a.animate.set_opacity(0.95),
            decision_b.animate.set_opacity(0.75),
            state_ring.animate.set_opacity(0.45),
            run_time=0.8,
        )
