import copy
import random

# Hat Object Constructor:

class Hat:

    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        removed = []
        if number >= len(self.contents):
            return self.contents
        while number > 0:
            rball = self.contents.pop(random.randint(0, (len(self.contents)-1)))
            removed.append(rball)
            number -= 1
        return removed

# Probability Calculation Function:  Can be called with the given parameters to
# calculate the probability of drawing the expected set of balls from a given hat
# in N trials.

# Example:
# prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_drawn = hat_copy.draw(num_balls_drawn)

        for color in colors_drawn:
            if color in expected_copy:
                expected_copy[color]-=1

        if(all(x <= 0 for x in expected_copy.values())):
            count += 1

    return count / num_experiments
