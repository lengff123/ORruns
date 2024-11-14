# Parallel Experiments Guide

## Overview

ORruns supports parallel execution of experiments to efficiently handle multiple runs and parameter configurations.

## Basic Parallel Execution

### Using Repeat Experiment Decorator
```python
from orruns.decorators import repeat_experiment

@repeat_experiment(times=5, parallel=True)
def optimization_study(tracker):
    result = your_optimization_algorithm()
    return result
```

### Parameter Sweep
```python
from orruns import ParameterSweep

sweep = ParameterSweep({
    "population_size": [50, 100, 200],
    "mutation_rate": [0.1, 0.2, 0.3]
})

@sweep.run(parallel=True)
def parameter_study(params, tracker):
    result = optimize_with_params(params)
    return result
```

## Advanced Parallel Features

### Custom Process Pool
```python
from orruns import ParallelExecutor

executor = ParallelExecutor(
    max_workers=4,
    timeout=3600,
    backend="multiprocessing"
)

results = executor.map(optimization_function, parameter_sets)
```

### Distributed Execution
```python
from orruns.distributed import DistributedTracker

tracker = DistributedTracker(
    name="distributed_experiment",
    backend="ray"
)

# Execute across multiple machines
tracker.run_distributed(optimization_function, nodes=["node1", "node2"])
```

## Performance Considerations

1. **Resource Management**
   - CPU utilization
   - Memory consumption
   - Disk I/O optimization

2. **Error Handling**
   - Process failure recovery
   - Timeout management
   - Result aggregation

3. **Monitoring**
   - Progress tracking
   - Resource usage
   - Error logging