# Quick Start Guide

This guide will help you get started with ORruns in minutes.

## Basic Usage

### 1. Create Your First Experiment
```python
from orruns import ExperimentTracker

with ExperimentTracker("my_first_experiment") as tracker:
    # Configure experiment parameters
    tracker.log_params({
        "algorithm": "NSGA-II",
        "population_size": 100,
        "generations": 50
    })
    
    # Your optimization code here
    result = run_optimization()
    
    # Log results
    tracker.log_metrics({
        "objective_value": result.best_value,
        "execution_time": result.time
    })
```

### 2. Track Multiple Runs
```python
from orruns.decorators import repeat_experiment

@repeat_experiment(times=5, parallel=True)
def optimization_experiment(tracker):
    # Your optimization code
    return results
```

### 3. Visualize Results
```python
from orruns.visualization import plot_results

# Generate visualization
plot_results("my_first_experiment")
```

## Directory Structure

After running experiments, ORruns creates the following structure:
```
orruns_experiments/
└── my_first_experiment/
    ├── artifacts/
    │   ├── data/
    │   └── figures/
    ├── metrics/
    ├── params/
    └── summary.json
```

## Next Steps

- Explore the [User Guide](../user-guide/experiment-tracking.md) for detailed features
- Check out [Examples](../examples/basic-usage.md) for more use cases
- Learn about [Advanced Features](../user-guide/parallel-experiments.md)