from orruns.tracker import ExperimentTracker
from orruns.visualization import ExperimentDashboard
import numpy as np
from pathlib import Path
import shutil


def run_specific_experiments():
    # 清理并创建实验目录
    base_dir = Path("./demo_experiments")
    if base_dir.exists():
        shutil.rmtree(base_dir)
    base_dir.mkdir()

    # 1. aim 实验 (单次运行，无参数)
    tracker = ExperimentTracker("aim", base_dir=str(base_dir))
    # 记录指标
    for epoch in range(50):
        loss = 1.0 * np.exp(-0.1 * epoch) + np.random.normal(0, 0.1)
        acc = 1.0 - loss + np.random.normal(0, 0.05)
        tracker.log_metrics({
            "loss": float(loss),
            "accuracy": float(acc)
        }, step=epoch)

    # 2. sam 实验 (s=3, 重复5次)
    for run in range(5):
        tracker = ExperimentTracker("sam", base_dir=str(base_dir))
        # 记录参数
        tracker.log_params({
            "s": 3
        })
        # 记录指标
        for epoch in range(50):
            loss = 1.0 * np.exp(-0.1 * epoch) + np.random.normal(0, 0.1)
            acc = 1.0 - loss + np.random.normal(0, 0.05)
            tracker.log_metrics({
                "loss": float(loss),
                "accuracy": float(acc)
            }, step=epoch)

    # 3. sam 实验 (s=5, 重复5次)
    for run in range(5):
        tracker = ExperimentTracker("sam", base_dir=str(base_dir))
        # 记录参数
        tracker.log_params({
            "s": 5
        })
        # 记录指标
        for epoch in range(50):
            loss = 1.0 * np.exp(-0.1 * epoch) + np.random.normal(0, 0.1)
            acc = 1.0 - loss + np.random.normal(0, 0.05)
            tracker.log_metrics({
                "loss": float(loss),
                "accuracy": float(acc)
            }, step=epoch)

    # 创建并启动仪表板
    dashboard = ExperimentDashboard(base_dir=str(base_dir))
    print("\n=== ORruns Dashboard ===")
    print("正在启动仪表板...")
    print("\n访问 http://localhost:8050 查看实验结果")
    print("\n实验概览:")
    print("- aim: 单次运行，无参数")
    print("- sam (s=3): 5次重复运行")
    print("- sam (s=5): 5次重复运行")
    print("\n按 Ctrl+C 停止服务器\n")
    dashboard.run(port=8050)

if __name__ == "__main__":
    run_specific_experiments()