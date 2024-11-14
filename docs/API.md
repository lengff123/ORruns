# ExperimentTracker API Reference

## Class: ExperimentTracker

The main class for tracking experiments in ORruns.

### Constructor

```python
ExperimentTracker(
    experiment_name: str,
    base_dir: Optional[str] = None,
    metadata: Optional[Dict] = None
)
```

#### Parameters
- `experiment_name`: Name of the experiment
- `base_dir`: Base directory for storing experiment data
- `metadata`: Additional metadata for the experiment

### Methods

#### log_params
```python
def log_params(self, params: Dict[str, Any]) -> None
```
Log experiment parameters.

#### log_metrics
```python
def log_metrics(self, metrics: Dict[str, Union[float, int]]) -> None
```
Log experiment metrics.

#### save_artifact
```python
def save_artifact(
    self,
    filename: str,
    artifact: Union[pd.DataFrame, np.ndarray, Any],
    artifact_type: str = "data"
) -> str
```
Save experiment artifacts (data, figures, etc.).

[Continue with other methods...]