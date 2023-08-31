"""
  calculator = Calculator()

  calculator.add(10, 5) ➞ 15

  calculator.subtract(10, 5) ➞ 5

  calculator.multiply(10, 5) ➞ 50

  calculator.divide(10, 5) ➞ 2
"""

class Calculator:
  def add(self, first_num, second_num):
      return (first_num + second_num)

  def subtract(self, first_num, second_num):
    return first_num - second_num
  
  def multiply(self, first_num, second_num):
    return first_num * second_num
  
  def divide(self, first_num, second_num):
    return first_num / second_num

calculator = Calculator()

print(calculator.add(10, 5)) 
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))


