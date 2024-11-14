from orruns.tracker import ExperimentTracker
from orruns.visualization import ExperimentDashboard
import numpy as np
from pathlib import Path
import shutil
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # 设置后端为 Agg，避免 Tkinter 相关问题
import matplotlib.pyplot as plt

def run_optimization_demo():
    # 清理并创建实验目录
    base_dir = Path("./demo_experiments")
    if base_dir.exists():
        shutil.rmtree(base_dir)
    #base_dir.mkdir()

    # 模拟多个不同学习率的实验
    learning_rates = [0.001, 0.01, 0.1]
    
    for lr in learning_rates:
        # 创建实验追踪器
        tracker = ExperimentTracker("optimization_demo", base_dir=str(base_dir))
        
        # 记录超参数
        tracker.log_params({
            "learning_rate": lr,
            "batch_size": 32,
            "optimizer": "Adam"
        })
        
        # 用于收集训练数据的列表
        epochs = []
        losses = []
        accuracies = []
        
        # 模拟训练过程
        np.random.seed(42)
        for epoch in range(50):
            # 模拟损失下降
            base_loss = 1.0 * np.exp(-lr * epoch)
            noise = np.random.normal(0, 0.1)
            loss = base_loss + noise
            
            # 模拟准确率上升
            accuracy = 1.0 - base_loss + np.random.normal(0, 0.05)
            accuracy = min(max(accuracy, 0), 1)  # 限制在 [0,1] 范围内
            
            # 收集数据
            epochs.append(epoch)
            losses.append(float(loss))
            accuracies.append(float(accuracy))
            
            # 记录指标
            tracker.log_metrics({
                "loss": float(loss),
                "accuracy": float(accuracy)
            }, step=epoch)

        # 创建并保存训练历史CSV
        history_df = pd.DataFrame({
            'epoch': epochs,
            'loss': losses,
            'accuracy': accuracies
        })
        tracker.log_artifact('training_history.csv', history_df)

        # 创建并保存训练曲线图
        fig = plt.figure(figsize=(10, 5))
        
        # 损失曲线
        plt.subplot(1, 2, 1)
        plt.plot(epochs, losses, 'b-', label='Loss')
        plt.title(f'Training Loss (lr={lr})')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.legend()
        
        # 准确率曲线
        plt.subplot(1, 2, 2)
        plt.plot(epochs, accuracies, 'r-', label='Accuracy')
        plt.title(f'Training Accuracy (lr={lr})')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        tracker.log_artifact(f'training_curves_lr_{lr}.png', fig)
        plt.close(fig)  # 明确关闭图形
        plt.close('all')  # 确保所有图形都被关闭

    # 创建并启动仪表板
    dashboard = ExperimentDashboard(base_dir=str(base_dir))
    dashboard.run(port=8050)

if __name__ == "__main__":
    print("\n=== ORruns Dashboard ===")
    print("正在启动仪表板...")
    print("\n访问 http://localhost:8050 查看实验结果")
    print("\n特性:")
    print("- 实验概览和统计")
    print("- 交互式图表")
    print("- 参数对比")
    print("- 文件管理")
    print("\n按 Ctrl+C 停止服务器\n")
    run_optimization_demo()