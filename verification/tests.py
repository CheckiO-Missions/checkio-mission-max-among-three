"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [1, 2, 3], "answer": 3},
        {"input": [3, 2, 1], "answer": 3},
        {"input": [1, 3, 2], "answer": 3},
        {"input": [0, 0, 0], "answer": 0},
        {"input": [-1, -2, -3], "answer": -1},
        {"input": [5, 5, 4], "answer": 5},
        {"input": [-5, -5, -6], "answer": -5},
        {"input": [10, 9, 10], "answer": 10},
        {"input": [123, 456, 789], "answer": 789},
        {"input": [789, 123, 456], "answer": 789}
    ],
    "Extra": [
        {"input": [10**9, -10**9, 0], "answer": 10**9},
        {"input": [-10**9, -10**9, -10**9], "answer": -10**9}
    ]
}

