from orruns.tracker import ExperimentTracker
from orruns.visualization import ExperimentDashboard
import numpy as np
from pathlib import Path
import shutil
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set backend to Agg to avoid Tkinter issues
import matplotlib.pyplot as plt

def run_optimization_demo():
    # Clean and create experiment directory
    base_dir = Path("./demo_experiments")
    if base_dir.exists():
        shutil.rmtree(base_dir)
    #base_dir.mkdir()

    # Simulate experiments with different learning rates
    learning_rates = [0.001, 0.01, 0.1]
    
    for lr in learning_rates:
        # Create experiment tracker
        tracker = ExperimentTracker("optimization_demo", base_dir=str(base_dir))
        
        # Record hyperparameters
        tracker.log_params({
            "learning_rate": lr,
            "batch_size": 32,
            "optimizer": "Adam"
        })
        
        # Lists for collecting training data
        epochs = []
        losses = []
        accuracies = []
        
        # Simulate training process
        np.random.seed(42)
        for epoch in range(50):
            # Simulate loss decrease
            base_loss = 1.0 * np.exp(-lr * epoch)
            noise = np.random.normal(0, 0.1)
            loss = base_loss + noise
            
            # Simulate accuracy increase
            accuracy = 1.0 - base_loss + np.random.normal(0, 0.05)
            accuracy = min(max(accuracy, 0), 1)  # Constrain to [0,1] range
            
            # Collect data
            epochs.append(epoch)
            losses.append(float(loss))
            accuracies.append(float(accuracy))
            
            # Record metrics
            tracker.log_metrics({
                "loss": float(loss),
                "accuracy": float(accuracy)
            }, step=epoch)

        # Create and save training history CSV
        history_df = pd.DataFrame({
            'epoch': epochs,
            'loss': losses,
            'accuracy': accuracies
        })
        tracker.log_artifact('training_history.csv', history_df)

        # Create and save training curves
        fig = plt.figure(figsize=(10, 5))
        
        # Loss curve
        plt.subplot(1, 2, 1)
        plt.plot(epochs, losses, 'b-', label='Loss')
        plt.title(f'Training Loss (lr={lr})')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.legend()
        
        # Accuracy curve
        plt.subplot(1, 2, 2)
        plt.plot(epochs, accuracies, 'r-', label='Accuracy')
        plt.title(f'Training Accuracy (lr={lr})')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        tracker.log_artifact(f'training_curves_lr_{lr}.png', fig)
        plt.close(fig)  # Explicitly close figure
        plt.close('all')  # Ensure all figures are closed

    # Create and launch dashboard
    dashboard = ExperimentDashboard(base_dir=str(base_dir))
    dashboard.run(port=8050)

if __name__ == "__main__":
    print("\n=== ORruns Dashboard ===")
    print("Starting dashboard...")
    print("\nVisit http://localhost:8050 to view experiment results")
    print("\nFeatures:")
    print("- Experiment overview and statistics")
    print("- Interactive charts")
    print("- Parameter comparison")
    print("- File management")
    print("\nPress Ctrl+C to stop the server\n")
    run_optimization_demo()