from solutions.SUM.sum_solution import SumSolution
from solutions.HLO.hello_solution import HelloSolution
from solutions.FIZ.fizz_buzz_solution import FizzBuzzSolution
from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.DMO.demo_round1_solution import DemoRound1Solution
from solutions.DMO.demo_round2_solution import DemoRound2Solution
from solutions.DMO.demo_round3_solution import DemoRound3Solution
from solutions.DMO.inventory_item import InventoryItem
from solutions.DMO.demo_round4n5_solution import DemoRound4n5Solution

from dataclasses import is_dataclass, asdict

class EntryPointMapping:
    def __init__(self):
        self.sum_solution = SumSolution()
        self.hello_solution = HelloSolution()
        self.fizz_buzz_solution = FizzBuzzSolution()
        self.checkout_solution = CheckoutSolution()
        self.demo_round1_solution = DemoRound1Solution()
        self.demo_round2_solution = DemoRound2Solution()
        self.demo_round3_solution = DemoRound3Solution()
        self.demo_round4n5_solution = DemoRound4n5Solution()

    # Round 0
    def sum(self, *args):
        return self.sum_solution.compute(*args)

    def hello(self, *args):
        return self.hello_solution.hello(*args)

    def fizz_buzz(self, *args):
        return self.fizz_buzz_solution.fizz_buzz(*args)

    def checkout(self, *args):
        return self.checkout_solution.checkout(*args)

    # Round 1
    def increment(self, *args):
        return self.demo_round1_solution.increment(*args)

    def to_uppercase(self, *args):
        return self.demo_round1_solution.to_uppercase(*args)

    def letter_to_santa(self):
        return self.demo_round1_solution.letter_to_santa()

    def count_lines(self, *args):
        return self.demo_round1_solution.count_lines(*args)

    # Round 2
    def array_sum(self, *args):
        return self.demo_round2_solution.array_sum(*args)

    def int_range(self, *args):
        return self.demo_round2_solution.int_range(*args)

    def filter_pass(self, *args):
        return self.demo_round2_solution.filter_pass(*args)

    # Round 3
    def inventory_add(self, inventory_item, number):
        item = InventoryItem(**inventory_item)
        return self.demo_round3_solution.inventory_add(item, number)

    def inventory_size(self):
        return self.demo_round3_solution.inventory_size()

    def inventory_get(self, *args):
        response = self.demo_round3_solution.inventory_get(*args)
        if is_dataclass(response):
            # noinspection PyDataclass
            return asdict(response)
        return response

    # Round 4 & 5
    def waves(self, *args):
        return self.demo_round4n5_solution.waves(*args)
