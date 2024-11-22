# Experiment Tracking Guide

## Overview

ORruns provides comprehensive experiment tracking capabilities through the `@experiment_manager` decorator and `ExperimentTracker` class.

## Recommended Approach

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

## Parameter Tracking

### Basic Parameters
```python
@experiment_manager(...)
def experiment(tracker):
    # Simple parameters
    tracker.log_params({
        "solver": "cplex",
        "time_limit": 3600,
        "gap_tolerance": 0.01
    })
```

### Nested Parameters
```python
@experiment_manager(...)
def experiment(tracker):
    # Nested configuration
    tracker.log_params({
        "solver": {
            "name": "cplex",
            "settings": {
                "time_limit": 3600,
                "threads": 4,
                "mip_gap": 0.01
            }
        },
        "problem": {
            "size": 100,
            "constraints": ["capacity", "time_windows"]
        }
    })
```

### Parameter Prefixes
```python
@experiment_manager(...)
def experiment(tracker):
    # Using prefixes for organization
    tracker.log_params({
        "population_size": 100,
        "mutation_rate": 0.1
    }, prefix="genetic")

    tracker.log_params({
        "crossover": "uniform",
        "selection": "tournament"
    }, prefix="genetic.operators")
```

## Metric Tracking

### Basic Metrics
```python
@experiment_manager(...)
def experiment(tracker):
    # Log single metrics
    tracker.log_metrics({
        "objective": 1234.56,
        "solve_time": 120.5,
        "gap": 0.01
    })
```

### Iterative Metrics
```python
@experiment_manager(...)
def experiment(tracker):
    # Track progress with steps
    for iteration in range(100):
        tracker.log_metrics({
            "current_objective": obj_value,
            "improvement": delta
        }, step=iteration)
```

### Nested Metrics
```python
@experiment_manager(...)
def experiment(tracker):
    # Complex metric structure
    tracker.log_metrics({
        "solution": {
            "objective": 1234.56,
            "feasibility": True,
            "constraints": {
                "violations": 0,
                "slack": [0.1, 0.2, 0.3]
            }
        },
        "performance": {
            "solve_time": 120.5,
            "iterations": 50
        }
    })
```

## Artifact Management

### Saving Data Files
```python
@experiment_manager(...)
def experiment(tracker):
    # Save CSV data
    tracker.log_artifact(
        "results.csv",
        pd.DataFrame(results),
        artifact_type="data"
    )

    # Save JSON configuration
    tracker.log_artifact(
        "config.json",
        config_dict,
        artifact_type="data"
    )

    # Save numpy arrays
    tracker.log_artifact(
        "solution.npy",
        solution_array,
        artifact_type="data"
    )
```

### Saving Figures
```python
@experiment_manager(...)
def experiment(tracker):
    # Save matplotlib figure
    plt.figure()
    plt.plot(history)
    tracker.log_artifact(
        "convergence.png",
        plt.gcf(),
        artifact_type="figure"
    )
    plt.close()

    # Save multiple plots
    for i, plot in enumerate(plots):
        tracker.log_artifact(
            f"analysis_{i}.png",
            plot,
            artifact_type="figure"
        )
```

## Result Merging

The `merge_config` parameter controls how results from multiple runs are combined and analyzed.

### Configuration Options

```python
merge_config = {
    # Numerical arrays (e.g., solution vectors)
    "arrays": [
        "solution_vector",
        "population_matrix"
    ],
    
    # Single values (e.g., metrics)
    "scalars": [
        "objective",
        "solve_time",
        "gap"
    ],
    
    # Plots and visualizations
    "images": [
        "convergence.png",
        "solution.png"
    ],
    
    # Statistical analysis
    "distributions": [
        "objectives",
        "gaps"
    ],
    
    # Time series data
    "time_series": [
        "convergence_history",
        "gap_history"
    ],
    
    # Network/graph data
    "graphs": [
        "solution_network"
    ],
    
    # Text content
    "text": [
        "solver_log"
    ],
    
    # Model files
    "models": [
        "trained_model"
    ]
}
```

### Example Usage

```python
@experiment_manager(
    times=10,
    merge_config={
        "scalars": ["objective", "time"],
        "distributions": ["gaps"],
        "time_series": ["convergence"],
        "images": ["convergence.png"]
    }
)
def experiment(tracker):
    # ... experiment code ...
    return {
        "objective": final_objective,
        "time": solve_time,
        "gaps": gap_history,
        "convergence": convergence_history
    }
```

## System Information

Control the level of system information logging:

```python
@experiment_manager(
    # Basic hardware/software info (default)
    system_info_level='basic',
    
    # Detailed system information
    system_info_level='full',
    
    # No system information
    system_info_level='none'
)
```


## Common Patterns

### 1. Optimization Experiments
```python
@experiment_manager(
    times=5,
    merge_config={
        "scalars": ["objective", "time", "gap"],
        "time_series": ["convergence"],
        "images": ["convergence.png"]
    }
)
def optimization_experiment(tracker):
    # Log solver configuration
    tracker.log_params(solver_config)
    
    # Run optimization
    for iteration in range(max_iter):
        result = solver.step()
        tracker.log_metrics({
            "current_objective": result.objective,
            "gap": result.gap
        }, step=iteration)
    
    return {
        "objective": result.objective,
        "time": result.time,
        "gap": result.gap,
        "convergence": result.history
    }
```

### 2. Parameter Studies
```python
@experiment_manager(
    times=10,
    merge_config={
        "distributions": ["results"],
        "images": ["comparison.png"]
    }
)
def parameter_study(tracker):
    # Random parameter selection
    params = {
        "population_size": np.random.choice([50, 100, 200]),
        "mutation_rate": np.random.uniform(0.1, 0.3)
    }
    
    tracker.log_params(params)
    results = run_algorithm(params)
    
    return {
        "results": results,
        "best_solution": results.best
    }
```

### 3. Comparative Analysis
```python
@experiment_manager(
    times=3,
    merge_config={
        "scalars": ["time", "quality"],
        "images": ["comparison.png"]
    }
)
def compare_methods(tracker):
    methods = ["method1", "method2", "method3"]
    results = {}
    
    for method in methods:
        tracker.log_params({"current_method": method})
        result = run_method(method)
        results[method] = result
        
        tracker.log_metrics({
            f"{method}_time": result.time,
            f"{method}_quality": result.quality
        })
    
    return results
```



## Directory Structure

```
orruns_experiments/
└── experiment_name/
    ├── run_20240315_123456/    # Individual run
    │   ├── params/             # Parameters
    │   │   └── params.json
    │   ├── metrics/            # Results
    │   │   └── metrics.json
    │   └── artifacts/          # Generated files
    │       ├── figures/
    │       │   ├── convergence.png
    │       │   └── analysis.png
    │       └── data/
    │           ├── results.csv
    │           └── solution.json
    └── merged_results/         # Combined analysis
        └── batch_123456/       # Batch results
            ├── arrays/
            ├── scalars/
            ├── distributions/
            └── time_series/
```

## Best Practices

1. **Experiment Organization**
   - Use meaningful experiment names
   - Group related parameters with prefixes
   - Maintain consistent metric names

2. **Parameter Management**
   - Log all relevant parameters
   - Use nested structures for complex configs
   - Include version information

3. **Metric Tracking**
   - Log metrics at appropriate steps
   - Use consistent units
   - Include intermediate results

4. **Artifact Handling**
   - Save important visualizations
   - Use appropriate file formats
   - Clean up temporary files

5. **Result Analysis**
   - Configure appropriate merge_config
   - Save raw data for later analysis
   - Document statistical methods

6. **Error Handling**
   - Wrap core logic in try-except
   - Log errors as metrics
   - Save partial results