""""
    Ones, Threes and Nines (Version #1)
    Given an int, figure out how many ones, threes and nines you could fit into the number.
    You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

    Examples
        n1 = ones_threes_nines(5)
        n1.nines ➞ 0

        n1.ones ➞ 5

        n1.threes ➞ 1
"""

class ones_threes_nines:
    def __init__(self, num) -> None:
        self.num = num

        self.nines = self.num//9
        self.ones = self.num//1
        self.threes = self.num//3


n1 = ones_threes_nines(5)
print(n1.nines)

print(n1.ones)

print(n1.threes)
