# ExperimentTracker API Reference

## Class: ExperimentTracker

Main class for tracking experiments in ORruns.

### Constructor

```python
ExperimentTracker(
    name: str,
    description: str = None,
    tags: List[str] = None,
    base_dir: str = None
) -> ExperimentTracker
```

#### Parameters:
- `name` (str): Unique name for the experiment
- `description` (str, optional): Detailed description
- `tags` (List[str], optional): Tags for categorizing experiments
- `base_dir` (str, optional): Base directory for storing experiment data

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

#### log_artifact
```python
def log_artifact(
    self,
    name: str,
    artifact: Union[str, bytes, pd.DataFrame],
    artifact_type: str = None
) -> None
```
Save experiment artifacts.

#### start_run
```python
def start_run(self, run_id: str = None) -> ContextManager
```
Start a new experiment run.

#### end_run
```python
def end_run(self) -> None
```
End current experiment run.

### Properties

#### experiment_dir
```python
@property
def experiment_dir(self) -> str
```
Get experiment directory path.

#### current_run_id
```python
@property
def current_run_id(self) -> str
```
Get current run identifier.

### Context Manager Support

The ExperimentTracker can be used as a context manager:
```python
with ExperimentTracker("experiment_name") as tracker:
    # Your experiment code
```