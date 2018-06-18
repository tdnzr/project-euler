# This file contains the pytests for my Project Euler solutions.

# Tests can be started by running "pytest" in the terminal.
# One can also run "pytest --durations=0" instead to see execution times for all tests.

import pytest
import importlib


# Rather than copy & paste the same test a gazillion times, I wanted to reuse the same test with different parameters.
# In pytest, this is apparently called "parametrizing fixtures" and works as follows:
@pytest.mark.parametrize("problem, answer", [
    ("Euler001a", 233168),
    ("Euler001b", 233168),
    ("Euler001c", 233168),
    ("Euler002a", 4613732),
    ("Euler002b", 4613732),
    ("Euler003",  6857),
    ("Euler004",  906609),
    ("Euler005a", 232792560),
    #("Euler005b", 232792560), # Slow - takes >2 min.
    ("Euler005c", 232792560),
    ("Euler006",  25164150),
    ("Euler007",  104743),
    ("Euler008a", 23514624000),
    ("Euler008b", 23514624000),
    ("Euler009a", (200, 375, 425, 31875000)),
    ("Euler009b", (200, 375, 425, 31875000)),
    ("Euler010",  142913828922),
    ("Euler011",  70600674),
    ("Euler012",  (12375, 76576500, 576)),
    ("Euler013",  5537376230),
    ("Euler015",  137846528820),
    ("Euler016",  1366),
    ("Euler017",  21124),
    ("Euler020",  648),
    ("Euler021",  31626),
    ("Euler022",  871198282),
    ("Euler023",  4179871),
    ("Euler024",  2783915460),
    ("Euler025",  4782),
    ("Euler029a", 9183),
    ("Euler029b", 9183),
    ("Euler029c", 9183),
    ("Euler030",  443839),
    ("Euler031",  73682),
    ("Euler034",  ([145, 40585], 40730)),
    ("Euler036",  872187),
    ("Euler038",  932718654),
    ("Euler039",  840),
    ("Euler042",  162),
    ("Euler043",  16695334890),
    ("Euler044",  5482660),
    ("Euler045",  1533776805),
    ("Euler048",  9110846700),
    ("Euler053",  4075),
    ("Euler056",  972),
    ("Euler057",  153),
    ("Euler062",  127035954683),
    ("Euler063",  49),
    ("Euler074",  402),
    ("Euler091",  14234),
    ("Euler093",  "1258"),
    ("Euler095a", 14316),
    ("Euler095b", 14316),
    ("Euler099",  709),
    ("Euler112", 1587100),
    ("Euler206a", 1389019170),
    ("Euler206b", 1389019170),
])
def test_eval(problem, answer):
    program = importlib.import_module(problem)
    assert program.run() == answer
