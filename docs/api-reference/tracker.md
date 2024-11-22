# ExperimentTracker API Reference

## Overview

`ExperimentTracker` is the core class for managing experiments in ORruns.

```python
from orruns import ExperimentTracker

tracker = ExperimentTracker(
    name="experiment_name",
    base_dir="./orruns_experiments"
)
```

## Core Methods

### Log Parameters

```python
tracker.log_params({
    "solver": "cplex",
    "threads": 4,
    "time_limit": 600
})
```

### Log Metrics

```python
tracker.log_metrics({
    "objective": 123.45,
    "solve_time": 10.5,
    "gap": 0.01
})
```

### Save Artifacts

```python
# Save plots
tracker.log_artifact("convergence.png", plt.gcf())

# Save data files
tracker.log_artifact("solution.csv", df)
```

## Context Manager

```python
with ExperimentTracker("experiment_name") as tracker:
    tracker.log_params({"solver": "gurobi"})
    # Your experiment code
    tracker.log_metrics({"objective": result.value})
```

## Class Methods

### Delete Experiments

```python
# Delete specific experiment
ExperimentTracker.delete_experiment("experiment_name")

# Delete specific run
ExperimentTracker.delete_experiment(
    "experiment_name",
    run_id="run_20240315_123456"
)
```

### Clean Old Experiments

```python
# Delete experiments older than 30 days
ExperimentTracker.delete_all_experiments()
```

## Properties

- `experiment_name`: Name of the experiment
- `run_id`: Unique identifier for current run
- `base_dir`: Base directory for experiment data

## Directory Structure

```
base_dir/
└── experiment_name/
    └── run_id/
        ├── params/
        │   └── params.json
        ├── metrics/
        │   └── metrics.json
        └── artifacts/
            ├── figures/
            └── data/
```

## Best Practices

1. Use descriptive experiment names
2. Log all relevant parameters
3. Save intermediate results
4. Use context manager for automatic cleanup
5. Organize artifacts by type

## Error Handling

Common errors and solutions:

| Error | Solution |
|-------|----------|
| `FileNotFoundError` | Check base directory exists |
| `PermissionError` | Check write permissions |
| `ValueError` | Verify parameter/metric format |