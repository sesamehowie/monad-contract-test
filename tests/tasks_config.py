from dataclasses import dataclass
from typing import Callable
from .rpsTest import test_rps
from .rouletteTest import test_roulette
from .chestTest import test_chest
from .potTest import test_lottery
from .plinkoTest import test_plinko
from .newRpsTest import test_new_rps
from .newChestTest import test_new_chests
from .chestsV3Test import test_chests_v3
from .predictionTest import test_prediction
from .vaultTest import test_vault
from .pythTest import test_pyth
from .prediction_final import test_prediction_final


@dataclass
class Task:
    id: int
    name: str
    task: Callable


Roulette = Task(1, "Roulette", test_roulette)
ChestsV1 = Task(2, "Chests(V1)", test_chest)
MonRoll = Task(3, "MonRoll", test_lottery)
Plinko = Task(4, "Plinko", test_plinko)
OldRPS = Task(5, "RPS(OLD)", test_rps)
NewRPS = Task(6, "RPS(New)", test_new_rps)
ChestsV2 = Task(7, "Chests(v2)", test_new_chests)
ChestsV3 = Task(8, "Chests(Latest)", test_chests_v3)
Prediction = Task(9, "Prediction(init)", test_prediction)
Vault = Task(10, "Vault", test_vault)
PythOracle = Task(11, "Pyth Oracle", test_pyth)
PredictionFinal = Task(12, "Prediction(Final)", test_prediction_final)

ALL_TASKS = [
    Roulette,
    ChestsV1,
    MonRoll,
    Plinko,
    OldRPS,
    NewRPS,
    ChestsV2,
    ChestsV3,
    Prediction,
    Vault,
    PythOracle,
    PredictionFinal,
]

TASK_IDS = [task.id for task in ALL_TASKS]
