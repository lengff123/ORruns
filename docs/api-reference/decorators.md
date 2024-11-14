# Decorators API Reference

## Overview

ORruns provides several decorators to enhance experiment management and execution.

## @repeat_experiment

Repeats an experiment multiple times with different random seeds.

### Syntax
```python
@repeat_experiment(
    times: int = 1,
    parallel: bool = False,
    max_workers: int = None
)
```

### Parameters
- `times`: Number of repetitions
- `parallel`: Whether to run in parallel
- `max_workers`: Maximum number of parallel workers

### Example
```python
from orruns.decorators import repeat_experiment

@repeat_experiment(times=5, parallel=True)
def optimization_study(tracker):
    result = your_optimization_algorithm()
    return result
```

## @track_time

Tracks execution time of functions.

### Syntax
```python
@track_time(prefix: str = None)
```

### Parameters
- `prefix`: Prefix for the time metric name

### Example
```python
from orruns.decorators import track_time

@track_time(prefix="algorithm")
def optimize(params):
    # Your optimization code
    return result
```

## @parameter_sweep

Performs parameter sweep experiments.

### Syntax
```python
@parameter_sweep(
    parameter_grid: Dict,
    parallel: bool = False
)
```

### Parameters
- `parameter_grid`: Dictionary of parameters to sweep
- `parallel`: Whether to run in parallel

### Example
```python
from orruns.decorators import parameter_sweep

param_grid = {
    "population_size": [50, 100, 200],
    "mutation_rate": [0.1, 0.2, 0.3]
}

@parameter_sweep(param_grid, parallel=True)
def sweep_study(params, tracker):
    result = optimize_with_params(params)
    return result
```