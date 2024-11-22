# Parallel Experiments Guide

## Overview

ORruns supports both parallel and serial execution of experiments through the `@experiment_manager` decorator.

## Basic Usage

### Serial Execution (Default)
```python
from orruns.decorators import experiment_manager

@experiment_manager(
    times=5,  # Run 5 times
    experiment_name="tsp_study"
)
def experiment(tracker):
    result = your_optimization_algorithm()
    return result
```

### Parallel Execution
```python
from orruns.decorators import experiment_manager
from multiprocessing import freeze_support

@experiment_manager(
    times=5,
    experiment_name="tsp_study",
    parallel=True,  # Enable parallel execution
    max_workers=None  # Uses CPU count by default
)
def experiment(tracker):
    result = your_optimization_algorithm()
    return result

if __name__ == '__main__':
    freeze_support()  # Required for Windows
    results = experiment()
```

## Configuration Options

### Process Pool Settings
```python
@experiment_manager(
    times=10,
    parallel=True,
    max_workers=4,  # Limit to 4 processes
    merge_config={...}
)
```

### System Information
```python
@experiment_manager(
    times=5,
    parallel=True,
    system_info_level='basic',  # Options: 'none', 'basic', 'full'
    print_style='auto'  # Options: 'auto', 'rich', 'simple', 'markdown'
)
```

## Result Handling

### Automatic Result Merging
```python
@experiment_manager(
    times=3,
    parallel=True,
    merge_config={
        "scalars": ["objective", "time"],
        "arrays": ["solution_vector"],
        "images": ["convergence.png"],
        "distributions": ["objectives"]
    }
)
def experiment(tracker):
    # Each process returns a result dictionary
    return {
        "objective": final_objective,
        "time": solve_time,
        "solution_vector": solution,
        "objectives": objective_history
    }
```

## Best Practices

1. **Windows Compatibility**
   ```python
   if __name__ == '__main__':
       freeze_support()  # Always include for Windows
       results = experiment()
   ```

2. **Resource Management**
   - Set appropriate `max_workers` based on CPU and memory
   - Consider I/O operations in parallel processes
   - Monitor system resource usage

3. **Error Handling**
   ```python
   @experiment_manager(times=5, parallel=True)
   def experiment(tracker):
       try:
           result = your_algorithm()
           return result
       except Exception as e:
           tracker.log_metrics({"error": str(e)})
           return {"error": str(e)}
   ```

4. **Data Serialization**
   - Return simple data types (numbers, strings, lists)
   - Use numpy arrays for numerical data
   - Avoid returning complex objects

## Directory Structure

```
orruns_experiments/
└── experiment_name/
    ├── run_20240315_123456/    # Process 1
    ├── run_20240315_123457/    # Process 2
    ├── run_20240315_123458/    # Process 3
    └── merged_results/         # Combined results
        └── batch_123456/
            ├── arrays/
            ├── scalars/
            ├── distributions/
            └── time_series/
```

## Limitations

1. **Process Communication**
   - Processes run independently
   - No direct communication between processes
   - Results merged only after completion

2. **Resource Sharing**
   - Each process needs its own memory
   - File access should be coordinated
   - Database connections should be created per process

3. **Windows Specific**
   - Requires `freeze_support()`
   - Uses 'spawn' instead of 'fork'
   - May have slower startup time