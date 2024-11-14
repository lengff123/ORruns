# Core Concepts

## Experiment Tracking

### What is an Experiment?
In ORruns, an experiment represents a single optimization run or a series of related optimization runs. Each experiment includes:
- Parameters
- Metrics
- Artifacts (data files, figures)
- Metadata

### Experiment Lifecycle
1. **Creation**: Initialize with ExperimentTracker
2. **Configuration**: Set parameters
3. **Execution**: Run optimization
4. **Logging**: Record results
5. **Analysis**: Visualize and compare results

## Key Components

### 1. ExperimentTracker
The central component for managing experiments:
- Handles experiment lifecycle
- Manages data storage
- Provides logging interface

### 2. Decorators
Utility functions that enhance experiment management:
- @repeat_experiment
- @parallel_execution
- @track_time

### 3. Visualization Tools
Built-in visualization capabilities:
- Performance curves
- Parameter distribution
- Comparison plots

### 4. Directory Structure
Standard organization for experiment data:
- artifacts/ - Generated files
- metrics/ - Performance metrics
- params/ - Configuration parameters
- summary.json - Experiment metadata

## Best Practices

1. **Naming Conventions**
- Use descriptive experiment names
- Follow consistent parameter naming

2. **Data Management**
- Log all relevant parameters
- Store intermediate results
- Save visualization artifacts

3. **Reproducibility**
- Set random seeds
- Document dependencies
- Version control experiments