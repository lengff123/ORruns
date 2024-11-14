# Optimization Examples

## Single-Objective Optimization

### Gradient Descent Example
```python
from orruns import ExperimentTracker
import numpy as np

def optimize_quadratic():
    with ExperimentTracker("gradient_descent") as tracker:
        # Configure optimization
        tracker.log_params({
            "learning_rate": 0.01,
            "max_iterations": 1000,
            "tolerance": 1e-6
        })
        
        # Initial point
        x = np.random.randn(10)
        
        # Optimization loop
        for i in range(1000):
            grad = 2 * x
            x = x - 0.01 * grad
            
            if i % 100 == 0:
                tracker.log_metrics({
                    "iteration": i,
                    "objective": np.sum(x**2)
                })

optimize_quadratic()
```

## Multi-Objective Optimization

### NSGA-II Example
```python
from orruns import ExperimentTracker
from orruns.decorators import repeat_experiment

@repeat_experiment(times=5, parallel=True)
def nsga2_optimization(tracker):
    # Configure NSGA-II
    tracker.log_params({
        "population_size": 100,
        "generations": 50,
        "crossover_rate": 0.9,
        "mutation_rate": 0.1
    })
    
    population = initialize_population()
    for generation in range(50):
        offspring = create_offspring(population)
        population = select_next_generation(population + offspring)
        
        tracker.log_metrics({
            "generation": generation,
            "hypervolume": calculate_hypervolume(population),
            "diversity": calculate_diversity(population)
        })
    
    return population

results = nsga2_optimization()
```

## Parameter Tuning

### Grid Search Example
```python
from orruns import ExperimentTracker
from orruns.decorators import parameter_sweep

param_grid = {
    "population_size": [50, 100, 200],
    "mutation_rate": [0.1, 0.2, 0.3],
    "crossover_rate": [0.8, 0.9]
}

@parameter_sweep(param_grid, parallel=True)
def parameter_study(params, tracker):
    # Run optimization with given parameters
    result = optimize_with_params(params)
    
    tracker.log_metrics({
        "final_hypervolume": result.hypervolume,
        "convergence_time": result.time
    })
    
    return result

results = parameter_study()
```