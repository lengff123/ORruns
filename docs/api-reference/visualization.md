# Visualization API Reference

## Plot Functions

### plot_performance

Creates performance plots for experiment metrics.

```python
def plot_performance(
    experiment_name: str,
    metric: str,
    runs: List[str] = None,
    title: str = None,
    ax: plt.Axes = None
) -> plt.Figure:
```

#### Parameters
- `experiment_name`: Name of the experiment
- `metric`: Metric to plot
- `runs`: List of run IDs to include
- `title`: Plot title
- `ax`: Matplotlib axes object

### plot_pareto_front

Visualizes Pareto fronts for multi-objective optimization.

```python
def plot_pareto_front(
    experiment_name: str,
    objectives: List[str],
    run_id: str = None,
    ax: plt.Axes = None
) -> plt.Figure:
```

#### Parameters
- `experiment_name`: Name of the experiment
- `objectives`: List of objective names
- `run_id`: Specific run ID to plot
- `ax`: Matplotlib axes object

## Dashboard Functions

### launch_dashboard

Launches interactive visualization dashboard.

```python
def launch_dashboard(
    experiment_name: str = None,
    port: int = 8050,
    debug: bool = False
) -> None:
```

#### Parameters
- `experiment_name`: Name of the experiment to display
- `port`: Port number for the dashboard
- `debug`: Enable debug mode

## Utility Functions

### create_comparison_plot

Creates comparison plots between multiple experiments.

```python
def create_comparison_plot(
    experiment_names: List[str],
    metric: str,
    plot_type: str = "box"
) -> plt.Figure:
```

#### Parameters
- `experiment_names`: List of experiments to compare
- `metric`: Metric for comparison
- `plot_type`: Type of plot ("box", "violin", etc.)