# Probability Calculator

A Python program that estimates the probability of drawing a specific combination of colored balls from a hat, using a Monte Carlo simulation.

## How It Works

- **`Hat`**: a class that holds balls of different colors and supports random draws without replacement.
- **`experiment()`**: repeats a draw many times and returns the fraction of experiments that included the expected balls.

## Usage

```python
import prob_calculator

hat = prob_calculator.Hat(blue=4, red=2, green=6)

probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "green": 1},
    num_balls_drawn=4,
    num_experiments=1000,
)

print(probability)
```

This estimates the chance of drawing at least 2 blue balls and 1 green ball when drawing 4 balls from the hat. The result is a number between 0 and 1, and it gets more accurate as `num_experiments` increases.

## Parameters

| Parameter | Description |
| --- | --- |
| `hat` | A `Hat` object containing the balls |
| `expected_balls` | Dictionary of colors and the minimum count of each to draw |
| `num_balls_drawn` | Number of balls drawn in each experiment |
| `num_experiments` | Number of times to repeat the experiment |

