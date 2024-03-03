# N-Queens Genetic Algorithm

This project demonstrates the use of a genetic algorithm to solve the N-Queens problem. The N-Queens problem is a classic chess puzzle where N queens must be placed on an N x N chessboard in such a way that no two queens threaten each other.

## Overview

The genetic algorithm involves creating a population of candidate solutions, evaluating their fitness based on the constraints of the N-Queens problem, and iteratively evolving the population towards a solution.

## Files

- **genetic_algorithm.py**: Python script containing the implementation of the genetic algorithm.
- **README.md**: This file, providing an overview of the project.

## Usage

To run the genetic algorithm, modify the parameters in the `main` function of `genetic_algorithm.py` and execute the script.

```python
# Example usage with a population size of 100 and a mutation rate of 0.4
main(population_size=100, mutation_rate=0.4)
