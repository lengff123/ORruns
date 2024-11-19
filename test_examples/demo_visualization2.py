from orruns.tracker import ExperimentTracker
from orruns.visualization import ExperimentDashboard
import numpy as np
from pathlib import Path
import shutil


def run_specific_experiments():
    # Clean and create experiment directory
    base_dir = Path("./demo_experiments")
    if base_dir.exists():
        shutil.rmtree(base_dir)
    base_dir.mkdir()

    # 1. aim experiment (single run, no parameters)
    tracker = ExperimentTracker("aim", base_dir=str(base_dir))
    # Record metrics
    for epoch in range(50):
        loss = 1.0 * np.exp(-0.1 * epoch) + np.random.normal(0, 0.1)
        acc = 1.0 - loss + np.random.normal(0, 0.05)
        tracker.log_metrics({
            "loss": float(loss),
            "accuracy": float(acc)
        }, step=epoch)

    # 2. sam experiment (s=3, 5 repetitions)
    for run in range(5):
        tracker = ExperimentTracker("sam", base_dir=str(base_dir))
        # Record parameters
        tracker.log_params({
            "s": 3
        })
        # Record metrics
        for epoch in range(50):
            loss = 1.0 * np.exp(-0.1 * epoch) + np.random.normal(0, 0.1)
            acc = 1.0 - loss + np.random.normal(0, 0.05)
            tracker.log_metrics({
                "loss": float(loss),
                "accuracy": float(acc)
            }, step=epoch)

    # 3. sam experiment (s=5, 5 repetitions)
    for run in range(5):
        tracker = ExperimentTracker("sam", base_dir=str(base_dir))
        # Record parameters
        tracker.log_params({
            "s": 5
        })
        # Record metrics
        for epoch in range(50):
            loss = 1.0 * np.exp(-0.1 * epoch) + np.random.normal(0, 0.1)
            acc = 1.0 - loss + np.random.normal(0, 0.05)
            tracker.log_metrics({
                "loss": float(loss),
                "accuracy": float(acc)
            }, step=epoch)

    # Create and launch dashboard
    dashboard = ExperimentDashboard(base_dir=str(base_dir))
    print("\n=== ORruns Dashboard ===")
    print("Starting dashboard...")
    print("\nVisit http://localhost:8050 to view experiment results")
    print("\nExperiment Overview:")
    print("- aim: single run, no parameters")
    print("- sam (s=3): 5 repetitions")
    print("- sam (s=5): 5 repetitions")
    print("\nPress Ctrl+C to stop the server\n")
    dashboard.run(port=8050)

if __name__ == "__main__":
    run_specific_experiments()