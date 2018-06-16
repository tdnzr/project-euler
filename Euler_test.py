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
    ("Euler008a", 23514624000),
    ("Euler008b", 23514624000),
    ("Euler009a", (200, 375, 425, 31875000)),
    ("Euler009b", (200, 375, 425, 31875000)),
    ("Euler013",  5537376230),
    ("Euler015",  137846528820),
    ("Euler029a", 9183),
    ("Euler029b", 9183),
    ("Euler029c", 9183),
    ("Euler030",  443839),
    ("Euler034", ([145, 40585], 40730)),
    ("Euler053",  4075),
])
def test_eval(problem, answer):
    program = importlib.import_module(problem)
    assert program.run() == answer
