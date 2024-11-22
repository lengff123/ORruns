# Experiment Management Guide

## Overview

ORruns provides a high-level API for managing your experiments after they've been run. You can list, query, analyze, and export your experimental results.

## Basic Usage

### Initialize API
```python
from orruns.api import ExperimentAPI

api = ExperimentAPI()  # Uses default data directory
```

## Viewing Experiments

### List Recent Experiments
```python
# List last 10 experiments
experiments = api.list_experiments()

# List experiments matching pattern
tsp_experiments = api.list_experiments(pattern="tsp_*")
```

### Get Experiment Details
```python
# Get specific experiment
experiment = api.get_experiment("tsp_study")

# Get specific run
run = api.get_experiment("tsp_study", run_id="20240315_123456")
```

## Querying Results

### Basic Queries
```python
# Find experiments with specific parameters
results = api.query_experiments(
    parameter_filters={
        "n_cities__gt": 50,
        "solver__eq": "cplex"
    }
)
```

### Analyzing Results
```python
# Compare multiple experiments
comparison = api.compare_experiments(
    experiment_names=["exp1", "exp2"],
    metrics=["objective", "time"]
)

# Get experiment history
history = api.get_experiment_history("tsp_study")
```

## Managing Artifacts

### List Available Artifacts
```python
artifacts = api.list_artifacts(
    experiment_name="tsp_study",
    run_id="20240315_123456"
)
```

### Access Artifacts
```python
# Get convergence plot
plot = api.get_artifact(
    experiment_name="tsp_study",
    run_id="20240315_123456",
    artifact_path="convergence.png",
    load_content=True
)

# Get results data
results = api.get_artifact(
    experiment_name="tsp_study",
    run_id="20240315_123456",
    artifact_path="results.csv",
    load_content=True
)
```

## Exporting Results

### Export to DataFrame
```python
# Export all metrics
df = api.export_to_dataframe("tsp_study")

# Export specific metrics
df = api.export_to_dataframe(
    "tsp_study",
    metrics=["objective", "time"]
)
```

### Export Artifacts
```python
# Export figures and data
exported = api.export_artifacts(
    experiment_name="tsp_study",
    run_id="20240315_123456",
    output_dir="./exports",
    artifact_types=["figures", "data"]
)
```

## Maintenance

### Cleaning Up
```python
# Delete specific experiment
api.delete_experiment("old_experiment")

# Delete specific run
api.delete_experiment(
    "experiment_name",
    run_id="20240315_123456"
)

# Clean old experiments
deleted = api.clean_old_experiments(days=30)
```

## Query Operators

When querying experiments, you can use these operators:

| Operator | Meaning | Example |
|----------|---------|---------|
| `__eq` | Equal to | `"solver__eq": "cplex"` |
| `__gt` | Greater than | `"n_cities__gt": 50` |
| `__lt` | Less than | `"time__lt": 3600` |
| `__gte` | Greater than or equal | `"gap__gte": 0.01` |
| `__lte` | Less than or equal | `"memory__lte": 1024` |

## Best Practices

1. **Regular Maintenance**
   - Clean up old experiments periodically
   - Export important results before deletion
   - Keep meaningful experiment names

2. **Result Organization**
   - Use consistent metric names
   - Group related experiments
   - Document experiment parameters

3. **Data Export**
   - Export to DataFrame for analysis
   - Save important artifacts
   - Use version control for exports

4. **Query Efficiency**
   - Use specific filters
   - Limit result sets
   - Sort results appropriately