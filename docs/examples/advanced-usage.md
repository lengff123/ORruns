# Advanced Usage Examples

## Custom Experiment Management

### Complex Experiment Structure
```python
from orruns import ExperimentTracker
from orruns.decorators import repeat_experiment
import numpy as np
import pandas as pd

class OptimizationExperiment:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.tracker = None
    
    def setup_tracker(self):
        self.tracker = ExperimentTracker(
            name=self.name,
            tags=["advanced", "multi-stage"],
            description="Complex optimization experiment"
        )
        self.tracker.log_params(self.config)
    
    def run(self):
        with self.tracker:
            # Stage 1: Initial Optimization
            stage1_result = self._run_stage1()
            
            # Stage 2: Refinement
            stage2_result = self._run_stage2(stage1_result)
            
            # Stage 3: Final Evaluation
            final_result = self._run_stage3(stage2_result)
            
            return final_result
    
    def _run_stage1(self):
        self.tracker.log_metrics({"stage": 1})
        # Implementation details...
        return initial_solution

    def _run_stage2(self, initial_solution):
        self.tracker.log_metrics({"stage": 2})
        # Implementation details...
        return refined_solution

    def _run_stage3(self, refined_solution):
        self.tracker.log_metrics({"stage": 3})
        # Implementation details...
        return final_result

# Usage
experiment = OptimizationExperiment(
    name="advanced_optimization",
    config={
        "stages": {
            "stage1": {"iterations": 100},
            "stage2": {"refinement_steps": 50},
            "stage3": {"evaluation_samples": 1000}
        }
    }
)
result = experiment.run()
```

## Advanced Parallel Processing

### Custom Parallel Executor
```python
from orruns import ExperimentTracker
from orruns.parallel import ParallelExecutor
import multiprocessing as mp
import numpy as np

class CustomParallelOptimizer:
    def __init__(self, n_workers=None):
        self.n_workers = n_workers or mp.cpu_count()
        self.executor = ParallelExecutor(max_workers=self.n_workers)
    
    def optimize(self, problem_instances):
        with ExperimentTracker("parallel_optimization") as tracker:
            tracker.log_params({
                "n_workers": self.n_workers,
                "n_instances": len(problem_instances)
            })
            
            # Define worker function
            def worker_fn(instance):
                result = solve_instance(instance)
                return {
                    "instance_id": instance.id,
                    "solution": result.solution,
                    "objective": result.objective
                }
            
            # Execute parallel optimization
            results = self.executor.map(worker_fn, problem_instances)
            
            # Aggregate results
            aggregated = self._aggregate_results(results)
            tracker.log_metrics(aggregated)
            
            return results
    
    def _aggregate_results(self, results):
        # Aggregation logic...
        return aggregated_metrics
```

## Advanced Data Management

### Custom Artifact Management
```python
from orruns import ExperimentTracker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class DataManager:
    def __init__(self, experiment_name):
        self.tracker = ExperimentTracker(experiment_name)
        self.data_cache = {}
    
    def save_optimization_history(self, history_data):
        # Convert to DataFrame
        df = pd.DataFrame(history_data)
        
        # Save raw data
        self.tracker.log_artifact(
            "optimization_history.csv",
            df,
            artifact_type="data"
        )
        
        # Create and save visualizations
        self._create_history_plots(df)
        
        # Save summary statistics
        self._save_summary_stats(df)
    
    def _create_history_plots(self, df):
        # Create multiple visualization plots
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Plot 1: Convergence curve
        axes[0,0].plot(df['iteration'], df['objective'])
        axes[0,0].set_title('Convergence Curve')
        
        # Plot 2: Parameter distribution
        axes[0,1].hist(df['parameter_values'])
        axes[0,1].set_title('Parameter Distribution')
        
        # Save plots
        self.tracker.log_artifact(
            "analysis_plots.png",
            fig,
            artifact_type="figure"
        )
        plt.close(fig)
    
    def _save_summary_stats(self, df):
        summary = {
            "statistics": df.describe().to_dict(),
            "correlations": df.corr().to_dict(),
            "final_values": df.iloc[-1].to_dict()
        }
        self.tracker.log_artifact(
            "summary_statistics.json",
            summary,
            artifact_type="json"
        )
```

## Integration with External Tools

### Custom Callback System
```python
from orruns import ExperimentTracker
from typing import Callable, List, Dict
import time

class OptimizationCallback:
    def __init__(self, tracker: ExperimentTracker):
        self.tracker = tracker
        self.start_time = None
    
    def on_optimization_start(self):
        self.start_time = time.time()
        self.tracker.log_metrics({"status": "started"})
    
    def on_iteration_end(self, iteration_data: Dict):
        self.tracker.log_metrics({
            "current_iteration": iteration_data["iteration"],
            "current_objective": iteration_data["objective"],
            "elapsed_time": time.time() - self.start_time
        })
    
    def on_optimization_end(self, final_results: Dict):
        self.tracker.log_metrics({
            "final_objective": final_results["objective"],
            "total_time": time.time() - self.start_time,
            "status": "completed"
        })
        
        # Save final results
        self.tracker.log_artifact(
            "final_results.json",
            final_results,
            artifact_type="json"
        )

# Usage with external optimizer
def run_with_external_optimizer():
    tracker = ExperimentTracker("external_optimization")
    callback = OptimizationCallback(tracker)
    
    # Configure external optimizer
    external_optimizer = ExternalOptimizer(
        callback_fn=callback.on_iteration_end
    )
    
    # Run optimization
    callback.on_optimization_start()
    result = external_optimizer.optimize()
    callback.on_optimization_end(result)
```

## Custom Metrics and Analysis

### Advanced Metrics Tracking
```python
from orruns import ExperimentTracker
import numpy as np
from scipy import stats

class AdvancedMetricsTracker:
    def __init__(self, experiment_name):
        self.tracker = ExperimentTracker(experiment_name)
        self.metrics_history = []
    
    def log_advanced_metrics(self, population, generation):
        metrics = {
            "generation": generation,
            "population_stats": self._calculate_population_stats(population),
            "diversity_metrics": self._calculate_diversity(population),
            "convergence_metrics": self._calculate_convergence(population)
        }
        
        self.metrics_history.append(metrics)
        self.tracker.log_metrics(metrics)
    
    def _calculate_population_stats(self, population):
        return {
            "mean": np.mean(population),
            "std": np.std(population),
            "skewness": stats.skew(population),
            "kurtosis": stats.kurtosis(population)
        }
    
    def _calculate_diversity(self, population):
        return {
            "unique_solutions": len(np.unique(population)),
            "entropy": stats.entropy(np.histogram(population)[0])
        }
    
    def _calculate_convergence(self, population):
        if len(self.metrics_history) > 0:
            prev_pop = self.metrics_history[-1]["population_stats"]["mean"]
            improvement = prev_pop - np.mean(population)
        else:
            improvement = 0
            
        return {
            "improvement": improvement,
            "convergence_rate": improvement if improvement > 0 else 0
        }
```

These advanced examples demonstrate: 
1. Management of complex experimental structures 
2. Custom parallel processing 
3. Advanced data management and visualization 
4. Integration with external tools 
5. Custom metric tracking and analysis Each example includes detailed comments and implementation details, which can be used as a reference for users to implement their own advanced functions.