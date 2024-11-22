# Core Concepts

## Overview

ORruns is an experiment tracking framework designed for optimization and operations research. It provides:

[previous content remains the same...]

## Advanced Concepts

### 1. Experiment Manager Decorator

The `@experiment_manager` decorator is the recommended way to manage experiments:

```python
@experiment_manager(
    times=5,  # Number of repetitions
    experiment_name="tsp_study",
    parallel=True,  # Enable parallel execution
    merge_config={  # Result merging configuration
        "arrays": ["distances"],
        "scalars": ["best_distance"],
        "images": ["convergence.png", "route.png"],
        "distributions": ["distances"]
    },
    system_info_level='basic'  # System information detail level
)
def experiment(tracker: ExperimentTracker) -> dict:
    # Experiment code
    pass
```

Key features:
- **Automatic Repetition**: Run experiments multiple times
- **Parallel Execution**: Utilize multiple CPU cores
- **Result Merging**: Combine results from multiple runs
- **System Monitoring**: Track hardware and software environment

### 2. Result Merging System

The result merger supports various data types:

```python
merge_config = {
    "arrays": ["solution_vectors"],     # Numerical arrays
    "scalars": ["objective", "time"],   # Single values
    "images": ["convergence.png"],      # Plots and figures
    "distributions": ["gaps"],          # Statistical distributions
    "time_series": ["iterations"],      # Time-based data
    "graphs": ["network"],              # Network structures
    "text": ["logs"],                   # Text content
    "models": ["trained_model"]         # Saved models
}
```

Merging capabilities:
- Statistical aggregation
- Distribution analysis
- Time series alignment
- Visual comparison
- Model ensemble

### 3. System Information Management

Three levels of system information:

1. **Basic Level**:
```python
system_info = {
    "hardware": {
        "cpu_count": 8,
        "memory_gb": 16
    },
    "software": {
        "python_version": "3.8.10",
        "key_packages": ["numpy", "pandas"]
    }
}
```

2. **Full Level**:
```python
system_info = {
    "hardware": {
        "cpu_model": "Intel(R) Core(TM) i7-9750H",
        "cpu_count": 8,
        "memory_gb": 16,
        "gpu_info": "NVIDIA GeForce RTX 2060"
    },
    "software": {
        "os": "Ubuntu 20.04",
        "python_version": "3.8.10",
        "installed_packages": {...},
        "environment_variables": {...}
    },
    "runtime": {
        "start_time": "2024-03-15 10:30:00",
        "pid": 12345,
        "working_directory": "/path/to/project"
    }
}
```

### 4. Directory Structure Details

Extended directory organization:

```
experiment_name/
├── run_[timestamp]/
│   ├── params/
│   │   ├── params.json           # Run parameters
│   │   └── system_info.json      # System information
│   ├── metrics/
│   │   ├── metrics.json          # Performance metrics
│   │   └── time_series/          # Time-based metrics
│   ├── artifacts/
│   │   ├── figures/              # Plots and visualizations
│   │   │   ├── convergence.png
│   │   │   └── solution.png
│   │   └── data/                 # Generated data
│   │       ├── solutions.csv
│   │       └── statistics.json
│   └── metadata.json             # Run information
├── merged_results/               # Combined analysis
│   ├── batch_[timestamp]/        # Batch results
│   │   ├── arrays/              # Merged arrays
│   │   ├── scalars/             # Merged metrics
│   │   ├── distributions/        # Statistical analysis
│   │   └── batch_metadata.json   # Batch information
│   └── plots/                    # Batch visualizations
└── summary.json                  # Experiment overview
```

### 5. Error Handling and Recovery

The framework provides robust error handling:

- **Parameter Validation**:
  - Type checking
  - Range validation
  - Dependency verification

- **Runtime Protection**:
  - Process isolation
  - Resource monitoring
  - Timeout management

- **Data Integrity**:
  - Atomic writes
  - Backup management
  - Corruption detection

### 6. Integration Patterns

Common integration scenarios:

1. **Solver Integration**:
```python
@experiment_manager(...)
def optimize(tracker):
    # Configure solver
    solver = OptimizationSolver()
    
    # Track solver progress
    for iteration in solver.solve():
        tracker.log_metrics({
            "objective": iteration.objective,
            "gap": iteration.gap
        })
    
    return solver.get_solution()
```

2. **Custom Metrics**:
```python
@experiment_manager(...)
def custom_tracking(tracker):
    # Define custom metric
    def calculate_metric(solution):
        return custom_analysis(solution)
    
    # Track custom metrics
    tracker.log_metrics({
        "standard": standard_metric(),
        "custom": calculate_metric(solution)
    })
```

## Best Practices

[previous content about best practices remains the same...]