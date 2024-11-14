# Visualization Guide

## Overview

ORruns provides powerful visualization tools to help you analyze and present your optimization results effectively.

## Basic Visualizations

### Performance Curves
```python
from orruns.visualization import plot_performance

# Plot convergence curve
plot_performance(
    experiment_name="optimization_experiment",
    metric="hypervolume",
    title="Convergence Analysis"
)
```

### Parameter Distribution
```python
from orruns.visualization import plot_parameter_distribution

# Visualize parameter distributions
plot_parameter_distribution(
    experiment_name="optimization_experiment",
    parameter="mutation_rate"
)
```

### Pareto Front Visualization
```python
from orruns.visualization import plot_pareto_front

# Plot Pareto front
plot_pareto_front(
    experiment_name="optimization_experiment",
    objectives=["cost", "performance"]
)
```

## Advanced Visualization Features

### Custom Plotting
```python
from orruns.visualization import create_custom_plot

def custom_plot_function(data, ax):
    # Your custom plotting logic
    pass

create_custom_plot(
    experiment_name="optimization_experiment",
    plot_function=custom_plot_function
)
```

### Interactive Dashboard
```python
from orruns.visualization import launch_dashboard

# Launch interactive dashboard
launch_dashboard(
    experiment_name="optimization_experiment",
    port=8050
)
```

## Best Practices

1. **Plot Customization**
   - Use consistent color schemes
   - Add proper labels and titles
   - Include error bars when applicable

2. **Performance Optimization**
   - Cache visualization data
   - Use appropriate figure sizes
   - Handle large datasets efficiently

3. **Export Options**
   - Save plots in various formats
   - Generate publication-ready figures
   - Create interactive HTML reports