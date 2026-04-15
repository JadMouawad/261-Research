"""Entry point for Person 2 RL scenes (7-12).

Render examples:
    manim -pqh manim_rl_presentation/main.py Scene07QLearningIntuition
    manim -pqh manim_rl_presentation/main.py Scene12ConclusionReferences
"""

from pathlib import Path
import sys

# Robust imports for both:
# 1) `python -m manim manim_rl_presentation/main.py ...`
# 2) direct execution where cwd/path differs.
THIS_DIR = Path(__file__).resolve().parent
PARENT_DIR = THIS_DIR.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

try:
    from manim_rl_presentation.rl_p2.scene07_q_learning_intuition import Scene07QLearningIntuition
    from manim_rl_presentation.rl_p2.scene08_q_update import Scene08QUpdateProcess
    from manim_rl_presentation.rl_p2.scene09_q_to_dqn import Scene09QTableToDQN
    from manim_rl_presentation.rl_p2.scene10_application_warehouse import Scene10WarehouseApplication
    from manim_rl_presentation.rl_p2.scene11_strengths_limitations import Scene11StrengthsLimitations
    from manim_rl_presentation.rl_p2.scene12_conclusion_refs import Scene12ConclusionReferences
except ModuleNotFoundError:
    from rl_p2.scene07_q_learning_intuition import Scene07QLearningIntuition
    from rl_p2.scene08_q_update import Scene08QUpdateProcess
    from rl_p2.scene09_q_to_dqn import Scene09QTableToDQN
    from rl_p2.scene10_application_warehouse import Scene10WarehouseApplication
    from rl_p2.scene11_strengths_limitations import Scene11StrengthsLimitations
    from rl_p2.scene12_conclusion_refs import Scene12ConclusionReferences

__all__ = [
    "Scene07QLearningIntuition",
    "Scene08QUpdateProcess",
    "Scene09QTableToDQN",
    "Scene10WarehouseApplication",
    "Scene11StrengthsLimitations",
    "Scene12ConclusionReferences",
]
