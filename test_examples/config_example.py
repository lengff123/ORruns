from orruns import ExperimentConfig, experiment_manager

# Create configuration file config.yaml
"""
algorithm:
  name: "VNS"
  parameters:
    max_iterations: 1000
    neighborhood_types: ["swap", "insert", "reverse"]
    
problem:
  type: "TSP"
  size: 100
  
experiment:
  runs: 5
  parallel: true
  seed: 42
"""

# Load configuration
config = ExperimentConfig("config.yaml")

# Run experiment with configuration
@experiment_manager(
    times=config.get("experiment.runs", 1),
    parallel=config.get("experiment.parallel", False)
)
def run_optimization(tracker):
    # Record experiment configuration
    tracker.log_params(config.config)
    
    # Get algorithm parameters
    algo_params = config.get("algorithm.parameters", {})
    max_iter = algo_params.get("max_iterations", 100)
    
    # Experiment code...
    pass