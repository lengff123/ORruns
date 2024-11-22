# Quick Start Guide

## Installation

```bash
pip install orruns
```

## Basic Usage (Not Recommended)

You can directly use `ExperimentTracker`, but this is not the recommended approach:

```python
import numpy as np
from orruns import ExperimentTracker
from docplex.mp.model import Model  # Using CPLEX solver

# 1. Create experiment tracker
tracker = ExperimentTracker("tsp_example")

# 2. Prepare data
n = 10  # Number of cities
np.random.seed(42)
distances = np.random.rand(n, n)  # Random distance matrix

# 3. Log parameters
tracker.log_params({
    "solver": "cplex",
    "n_cities": n,
    "time_limit": 600
})

# 4. Solve TSP
model = Model("tsp")
# ... model building code ...
solution = model.solve()

# 5. Save results
tracker.log_metrics({
    "objective": solution.get_objective_value(),
    "solve_time": solution.solve_time,
    "gap": solution.gap
})
```

## Recommended Approach

We strongly recommend using the `@experiment_manager` decorator for better experiment management:

```python
from orruns.decorators import experiment_manager
from multiprocessing import freeze_support

@experiment_manager(
    times=5,  # Run 5 times
    experiment_name="tsp_study",
    parallel=True,  # Enable parallel execution
    merge_config={
        "arrays": ["distances"],  # Merge distance arrays
        "scalars": ["best_distance"],  # Merge optimal distances
        "images": ["convergence.png", "route.png"],  # Save all plots
        "distributions": ["distances"]  # Analyze distance distributions
    },
    system_info_level='basic',  # Log basic system info
)
def experiment(tracker: ExperimentTracker) -> dict:
    """Compare performance across different city scales"""
    # Your experiment code here
    n_cities = np.random.choice([20, 30, 40])
    
    tracker.log_params({
        "n_cities": int(n_cities),
        "n_iterations": 1000
    })
    
    solver = TSPSolver(n_cities, n_iter=10)
    results = solver.solve(tracker)
    
    return results

if __name__ == '__main__':
    freeze_support()  # Required for Windows
    results = experiment()
```

## Common Use Cases

### 1. Comparing Different Solvers

```python
@experiment_manager(
    times=3,
    parallel=True,
    merge_config={
        "scalars": ["objective", "time", "gap"],
        "distributions": ["nodes"]
    }
)
def compare_solvers(tracker):
    solver_name = np.random.choice(["cplex", "gurobi", "cbc"])
    tracker.log_params({
        "solver": solver_name,
        "problem_size": n,
        "time_limit": 600
    })
    
    solver_func = solvers[solver_name]
    solution = solver_func(distances)
    
    return {
        "objective": solution.objective,
        "time": solution.time,
        "gap": solution.gap,
        "nodes": solution.nodes
    }
```

### 2. Parameter Tuning Experiments

```python
@experiment_manager(
    times=5,
    parallel=True,
    merge_config={
        "scalars": ["objective", "time"],
        "distributions": ["gap"]
    }
)
def tune_cplex_params(tracker):
    # Configure parameters
    params = {
        "method": np.random.choice(["barrier", "dual"]),
        "threads": np.random.choice([1, 2, 4, 8]),
        "mip_cuts": np.random.choice(["auto", "aggressive"])
    }
    tracker.log_params(params)
    
    # Solve
    solution = solve_tsp_with_params(params)
    
    return {
        "objective": solution.objective,
        "time": solution.time,
        "gap": solution.gap,
        "nodes": solution.nodes
    }
```

### 3. Analyzing Results

```python
from orruns.api import ExperimentAPI

api = ExperimentAPI()

# Export experiment data
df = api.export_to_dataframe(
    "solver_comparison",
    metrics=["objective", "time", "gap"]
)

# Statistical analysis
stats = df.groupby("solver").agg({
    "objective": ["mean", "std", "min", "max"],
    "time": ["mean", "std"],
    "gap": ["mean", "max"]
}).round(4)

print(stats)
```

## Directory Structure

Experiment data is saved in the `orruns_experiments` directory:
```
orruns_experiments/
└── solver_comparison/           # Experiment name
    ├── run_20240315_123456/    # Run ID
    │   ├── params/             # Parameters
    │   │   └── params.json
    │   ├── metrics/            # Results
    │   │   └── metrics.json
    │   └── artifacts/          # Generated files
    │       ├── figures/        # Plots
    │       └── data/          # Data files
    └── merged_results/         # Merged results
        ├── batch_123456/       # Batch results
        └── plots/              # Batch plots
```

## FAQ

**Q: How to save and visualize convergence history?**
```python
@experiment_manager(
    times=3,
    merge_config={
        "images": ["convergence.png"],
        "distributions": ["objectives"]
    }
)
def convergence_experiment(tracker):
    # Record convergence history
    history = {"iterations": [], "objectives": []}
    for i in range(max_iter):
        # ... optimization iteration ...
        history["iterations"].append(i)
        history["objectives"].append(obj)

    # Plot convergence
    plt.figure(figsize=(10, 6))
    plt.plot(history["iterations"], history["objectives"])
    plt.title("Convergence History")
    plt.xlabel("Iteration")
    plt.ylabel("Objective Value")
    tracker.log_artifact("convergence.png", plt.gcf())
    
    return {
        "objectives": history["objectives"],
        "final_obj": history["objectives"][-1]
    }
```

**Q: How to visualize multiple runs?**
```python
from orruns.visualization import ExperimentDashboard

# Launch dashboard
dashboard = ExperimentDashboard()
dashboard.run(port=8050)  # Visit http://localhost:8050
```

## Why Use @experiment_manager?

1. **Automatic Parallel Execution**
   - Run multiple experiments in parallel
   - Efficient resource utilization
   - Built-in result merging

2. **Better Result Management**
   - Automatic result collection
   - Statistical analysis
   - Distribution analysis
   - Plot management

3. **System Information Logging**
   - Hardware details
   - Software versions
   - Runtime environment

4. **Reproducibility**
   - Consistent experiment setup
   - Parameter tracking
   - Environment recording

## Next Steps

1. Check out the [Examples](../examples/index.md) for more use cases
2. Read [Core Concepts](concepts.md) to understand the design
3. See [API Reference](../api-reference/decorators.md) for detailed documentation