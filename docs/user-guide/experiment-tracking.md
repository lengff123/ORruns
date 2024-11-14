# Experiment Tracking Guide

## Overview

ORruns provides comprehensive experiment tracking capabilities to help researchers manage their optimization experiments efficiently.

## Basic Tracking

### Initialize Tracker
```python
from orruns import ExperimentTracker

tracker = ExperimentTracker(
    name="optimization_experiment",
    description="Testing NSGA-II performance",
    tags=["multi-objective", "evolutionary"]
)
```

### Log Parameters
```python
tracker.log_params({
    "algorithm": "NSGA-II",
    "population_size": 100,
    "generations": 500,
    "crossover_rate": 0.9,
    "mutation_rate": 0.1
})
```

### Log Metrics
```python
tracker.log_metrics({
    "hypervolume": 0.856,
    "igd": 0.023,
    "execution_time": 120.5
})
```

### Save Artifacts
```python
# Save data files
tracker.log_artifact("optimization_history.csv", data_frame)

# Save figures
tracker.log_figure("convergence_plot.png", figure)
```

## Advanced Features

### Nested Parameters
```python
tracker.log_params({
    "algorithm": {
        "name": "NSGA-II",
        "operators": {
            "selection": "tournament",
            "crossover": "sbx",
            "mutation": "polynomial"
        }
    }
})
```

### Tracking Multiple Runs
```python
for run in range(5):
    with tracker.start_run(run_id=f"run_{run}"):
        # Your optimization code
        tracker.log_metrics({"run_result": result})
```

### Auto-logging
```python
@tracker.autolog
def optimization_function(params):
    # Function execution will be automatically logged
    return result
```

## Best Practices

1. **Structured Naming**
   - Use consistent experiment names
   - Add meaningful tags
   - Include version information

2. **Comprehensive Logging**
   - Log all relevant parameters
   - Track intermediate results
   - Save visualization artifacts

3. **Resource Management**
   - Use context managers
   - Clean up temporary files
   - Handle large datasets efficiently