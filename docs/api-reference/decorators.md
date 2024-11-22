# Decorators API Reference

## @experiment_manager

The main decorator for managing experiment execution.

### Syntax
```python
@experiment_manager(
    times: int = 1,
    parallel: bool = False,
    merge_config: Optional[Dict] = None,
    experiment_name: Optional[str] = None
)
```

### Parameters
- `times`: Number of experiment runs
- `parallel`: Enable parallel execution
- `merge_config`: Configuration for merging results
- `experiment_name`: Optional custom experiment name

### Example
```python
from orruns.decorators import experiment_manager

@experiment_manager(
    times=5,
    parallel=True,
    merge_config={
        "scalars": ["objective", "time"],
        "distributions": ["gap"]
    }
)
def optimization_experiment(tracker):
    # Your experiment code
    params = {
        "method": "barrier",
        "threads": 4
    }
    tracker.log_params(params)
    
    result = solve_problem(params)
    return {
        "objective": result.objective,
        "time": result.time,
        "gap": result.gap
    }
```

### Result Merging

The `merge_config` parameter supports:
- `scalars`: Metrics to aggregate (mean, std, min, max)
- `distributions`: Metrics to analyze as distributions
- `artifacts`: Artifact handling configuration

## Common Use Cases

### 1. Simple Repetition
```python
@experiment_manager(times=3)
def basic_experiment(tracker):
    # Run 3 times sequentially
    pass
```

### 2. Parallel Execution
```python
@experiment_manager(
    times=10,
    parallel=True
)
def parallel_experiment(tracker):
    # Run 10 times in parallel
    pass
```

### 3. Result Analysis
```python
@experiment_manager(
    times=5,
    merge_config={
        "scalars": ["objective"],
        "distributions": ["iterations"]
    }
)
def analysis_experiment(tracker):
    # Results will be automatically analyzed
    pass
```