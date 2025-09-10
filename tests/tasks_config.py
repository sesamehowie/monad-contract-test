from dataclasses import dataclass
from typing import Callable
from .rouletteTest import test_roulette
from .potTest import test_lottery
from .plinkoTest import test_plinko
from .newRpsTest import test_new_rps
from .chestsV3Test import test_chests_v3
from .prediction_classic_test import test_prediction_classic


@dataclass
class Task:
    id: int
    name: str
    task: Callable


Roulette = Task(1, "Roulette", test_roulette)
MonRoll = Task(2, "MonRoll", test_lottery)
Plinko = Task(3, "Plinko", test_plinko)
NewRPS = Task(4, "RPS(New)", test_new_rps)
ChestsV3 = Task(5, "Chests(Latest)", test_chests_v3)
PredictionClassic = Task(6, "Prediction Game (Classic)", test_prediction_classic)

ALL_TASKS = [Roulette, MonRoll, Plinko, NewRPS, ChestsV3, PredictionClassic]

TASK_IDS = [task.id for task in ALL_TASKS]
