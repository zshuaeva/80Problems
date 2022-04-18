# Python Practice Problems

---

## Desirable Difficulty

This work is intended to feel like a good mental workout! 🧠

Engage in these practice problems by reading either the pseudocode or
requirements in the python file comments as instructed and writing your own
solution.

Your objective is to pay attention to how challenged you feel and make sure that
it feels "difficult but achievable"

### Translating pseudocode

Pay attention to the pseudocode. You will write this yourself soon. Observe the
logical language and take notes. Write Python code based on the pseudocode and
you will improve your ability to recall and write syntactically correct Python.

### Translating requirements

Create your own pseudocode from the written requirements.

Then, write your own code by translating from your pseudocode.

This is not about getting all the tests to pass.

This is about you engaging in small challenges over and over which improve your
ability to read and understand requirements and generate your own working code.

### Coding interviews

When you engage in whiteboarding interviews, you will use the skills you are
practicing in these exercises. At question 40, you are starting to do challenges
that are similar in difficulty to those in some coding interviews.

1. Improve your ability to write syntactically correct Python
1. Improve your ability to recognize programming logic in written requirements
1. Improve your ability to write pseudocode
1. Improve your ability to self-monitor the difficulty you are experiencing
1. Improve your ability to self-correct your approach depending on the
   difficulty you are experiencing
1. Improve your ability to prioritize skill improvement goals over speed

When you feel challenged, you learn. Embrace the challenge!

> "The only person you need to be better than is the person you were yesterday."

### Unit tests

This collection of practice problems for Python is unit test driven. That's how
you know you're done: when all the tests pass.

Each problem in _problems/_ has a corresponding test in _tests/_ and a
corresponding solution in _solutions/_.

## Getting Started

1. Fork the repository
1. Clone the forked repository
1. Create a branch for your work
1. Setup your environment and dependencies. These instructions are also in
   Learn.
   1. `python -m venv .venv`
   1. Activate your virtual environment
   1. `python -m pip install --upgrade pip`
   1. `pip install -r requirements.txt`
   1. `git checkout -b first-pass`
1. Run `python -m pytest -k "001"` to see the broken test
1. Open _problems/problem_001.py_ to read the specification and fill in the code
1. Run `python -m pytest -k "001"` to see the fixed test
1. Go on to "002" and keep going until you hit "080"

Then, start all over, again!

## Reading and running tests

When you run the test command, you will see test results in your terminal. We wrote code that will import your functions and execute them with some arguments. We then see what your function returned and compare that to what we expected.

### Example test

```python

def test_returns_min_value_if_first_parameter(self):
   value = minimum_value(1, 3)
   self.assertEqual(1, value)

```

When you have tests like this, you can read the test code like you read other code.

Do you see what the code above is doing?

This statement: `self.assertEqual(1, value)` is an assertion which checks if the return value from executing your function was the same as what we expected. If it is not, it will make the test fail!

### Errors

When you get an error, read it carefully. It will often show you the file and line number where the error occurred:

```bash

value1 = 3, value2 = 3

    def minimum_value(value1, value2):
        # if value1 is less than value2
>       if value > value2:
E       NameError: name 'value' is not defined

problems/problem_001.py:10: NameError

```

Did you catch it? `problems/problem_001.py:10: NameError`

You can even go straight to the error by clicking the error in your terminal.

Simply click on the link in your terminal with `Ctrl + click` on Windows or `Cmd + click` on MacOS.
