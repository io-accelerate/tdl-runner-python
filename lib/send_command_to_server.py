import sys
from tdl.queue.queue_based_implementation_runner import QueueBasedImplementationRunnerBuilder
from tdl.runner.challenge_session import ChallengeSession

from solutions.SUM import sum_solution
from solutions.HLO import hello_solution
from solutions.FIZ import fizz_buzz_solution
from solutions.CHK import checkout_solution
from solutions.DMO import demo_round1_solution
from solutions.DMO import demo_round2_solution
from solutions.DMO.demo_round3_solution import DemoRound3Solution
from solutions.DMO import demo_round4n5_solution
from runner.utils import Utils
from runner.user_input_action import get_user_input


"""
  ~~~~~~~~~~ Running the system: ~~~~~~~~~~~~~
 
    From IDE:
       Run this file from the IDE.
 
    From command line:
       PYTHONPATH=lib python lib/send_command_to_server.py
 
    To run your unit tests locally:
       PYTHONPATH=lib python -m pytest -q test/solution_tests/
 
  ~~~~~~~~~~ The workflow ~~~~~~~~~~~~~
 
    By running this file you interact with a challenge server.
    The interaction follows a request-response pattern:
         * You are presented with your current progress and a list of actions.
         * You trigger one of the actions by typing it on the console.
         * After the action feedback is presented, the execution will stop.
 
    +------+-----------------------------------------------------------------------+
    | Step | The usual workflow                                                    |
    +------+-----------------------------------------------------------------------+
    |  1.  | Run this file.                                                        |
    |  2.  | Start a challenge by typing "start".                                  |
    |  3.  | Read the description from the "challenges" folder.                    |
    |  4.  | Locate the file corresponding to your current challenge in:           |
    |      |   ./lib/solutions                                                     |
    |  5.  | Replace the following placeholder exception with your solution:       |
    |      |   raise NotImplementedError()                                         |
    |  6.  | Deploy to production by typing "deploy".                              |
    |  7.  | Observe the output, check for failed requests.                        |
    |  8.  | If passed, go to step 1.                                              |
    +------+-----------------------------------------------------------------------+
 
    You are encouraged to change this project as you please:
         * You can use your preferred libraries.
         * You can use your own test framework.
         * You can change the file structure.
         * Anything really, provided that this file stays runnable.
 
"""

demo_round3_solution = DemoRound3Solution()

runner = QueueBasedImplementationRunnerBuilder()\
    .set_config(Utils.get_runner_config())\
    .with_solution_for('sum', sum_solution.compute)\
    .with_solution_for('hello', hello_solution.hello)\
    .with_solution_for('fizz_buzz', fizz_buzz_solution.fizz_buzz)\
    .with_solution_for('checkout', checkout_solution.checkout)\
    .with_solution_for('increment', demo_round1_solution.increment)\
    .with_solution_for('to_uppercase', demo_round1_solution.to_uppercase)\
    .with_solution_for('letter_to_santa', demo_round1_solution.letter_to_santa)\
    .with_solution_for('count_lines', demo_round1_solution.count_lines)\
    .with_solution_for('array_sum', demo_round2_solution.array_sum)\
    .with_solution_for('int_range', demo_round2_solution.int_range)\
    .with_solution_for('filter_pass', demo_round2_solution.filter_pass)\
    .with_solution_for('inventory_add', demo_round3_solution.inventory_add)\
    .with_solution_for('inventory_size', demo_round3_solution.inventory_size)\
    .with_solution_for('inventory_get', demo_round3_solution.inventory_get)\
    .with_solution_for('waves', demo_round4n5_solution.waves)\
    .create()

ChallengeSession\
    .for_runner(runner)\
    .with_config(Utils.get_config())\
    .with_action_provider(lambda: get_user_input(sys.argv[1:]))\
    .start()
