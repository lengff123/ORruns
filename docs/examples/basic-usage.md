# Basic Usage Examples

## Simple Optimization Experiment

```python
from orruns import ExperimentTracker
import numpy as np

def objective_function(x):
    return np.sum(x**2)

# Initialize tracker
with ExperimentTracker("simple_optimization") as tracker:
    # Set parameters
    tracker.log_params({
        "dimensions": 10,
        "iterations": 1000,
        "algorithm": "gradient_descent"
    })
    
    # Run optimization
    x = np.random.randn(10)
    for i in range(1000):
        grad = 2 * x
        x = x - 0.01 * grad
        
        if i % 100 == 0:
            tracker.log_metrics({
                "iteration": i,
                "objective_value": objective_function(x)
            })
    
    # Log final results
    tracker.log_metrics({
        "final_value": objective_function(x),
        "solution_norm": np.linalg.norm(x)
    })
```

## Multi-Objective Optimization

```python
from orruns import ExperimentTracker
from orruns.decorators import experiment_manager

@experiment_manager(times=5)
def nsga2_experiment(tracker):
    # Initialize NSGA-II
    problem = MultiObjectiveProblem()
    algorithm = NSGA2(
        pop_size=100,
        n_generations=50
    )
    
    # Run optimization
    population = algorithm.run(problem)
    
    # Log results
    tracker.log_metrics({
        "hypervolume": calculate_hypervolume(population),
        "pareto_front_size": len(population.fronts[0])
    })
    
    # Save Pareto front
    tracker.log_artifact(
        "pareto_front.csv",
        population.fronts[0]
    )
    
    return population

# Run experiments
results = nsga2_experiment()
```

## Parameter Study

```python
from orruns import ExperimentTracker
from orruns.utils import parameter_sweep

# Define parameter grid
param_grid = {
    "population_size": [50, 100, 200],
    "mutation_rate": [0.1, 0.2, 0.3],
    "crossover_rate": [0.8, 0.9]
}

# Run parameter sweep
@parameter_sweep(param_grid, parallel=True)
def optimization_study(params, tracker):
    # Initialize algorithm with params
    algorithm = GeneticAlgorithm(**params)
    
    # Run optimization
    result = algorithm.optimize()
    
    # Log results
    tracker.log_metrics({
        "best_fitness": result.best_fitness,
        "convergence_time": result.time
    })
    
    return result

# Execute study
results = optimization_study()
```