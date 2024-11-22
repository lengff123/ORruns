# Visualization API Reference

## Dashboard

The `ExperimentDashboard` provides an interactive web interface for experiment analysis.

### Basic Usage

```python
from orruns.visualization import ExperimentDashboard

# Launch dashboard
dashboard = ExperimentDashboard()
dashboard.run(port=8050)  # Visit http://localhost:8050
```

### Features

1. **Experiment Overview**
   - Total runs
   - Best performance
   - Latest run status

2. **Interactive Plots**
   - Metric distributions
   - Convergence curves
   - Parameter relationships

3. **Data Analysis**
   - Statistical summaries
   - Parameter comparisons
   - Artifact visualization

## Plot Types

### Box Plots

```python
from orruns.visualization import PlotManager

plot_manager = PlotManager()

# Basic box plot
fig = plot_manager.create_box_plot(
    data=df,
    metric="objective",
    title="Objective Value Distribution"
)

# Grouped box plot
fig = plot_manager.create_grouped_box_plot(
    data=df,
    value_col="objective",
    group_col="solver",
    metric="objective",
    title="Objective by Solver"
)
```

### Line Plots

```python
# Single line plot
fig = plot_manager.create_line_plot(
    data=convergence_data,
    metric="gap",
    title="Convergence History"
)

# Grouped line plot with confidence intervals
fig = plot_manager.create_grouped_line_plot(
    data=convergence_data,
    metric="gap",
    title="Convergence by Method"
)
```

### Advanced Visualizations

```python
# Parameter relationships
fig = plot_manager.create_parallel_coordinates(
    data=df,
    params=["threads", "method", "cuts"],
    metric="objective"
)

# Correlation matrix
fig = plot_manager.create_scatter_matrix(
    data=df,
    params=["threads", "method", "cuts"],
    metric="objective"
)
```

## Customization

### Plot Theme

```python
plot_manager = PlotManager()
plot_manager.theme = 'plotly_white'  # Change theme
plot_manager.colors = ['#1f77b4', '#ff7f0e']  # Custom colors
```

### Layout Options

```python
plot_manager.default_layout.update({
    'paper_bgcolor': 'white',
    'plot_bgcolor': '#f8f9fa',
    'font': {'family': 'Arial'}
})
```

## Dashboard Configuration

### Custom Base Directory

```python
dashboard = ExperimentDashboard(
    base_dir="/path/to/experiments"
)
```

### Server Options

```python
dashboard.run(
    port=8080,
    debug=True,
    host='0.0.0.0'  # Allow external access
)
```

## Best Practices

1. **Performance**
   - Filter large datasets before plotting
   - Use appropriate plot types for data size

2. **Readability**
   - Add clear titles and labels
   - Use consistent color schemes
   - Include units in axis labels

3. **Interactivity**
   - Enable zooming for dense plots
   - Add hover information
   - Include download options

## Common Issues

| Issue | Solution |
|-------|----------|
| Slow loading | Reduce data points or use sampling |
| Missing plots | Check data format and availability |
| Port conflict | Change dashboard port number |