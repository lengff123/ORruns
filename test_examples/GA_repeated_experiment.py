from multiprocessing import freeze_support
import numpy as np
from orruns import ExperimentTracker, experiment_manager
import matplotlib.pyplot as plt

class NSGA2Optimizer:
    """简化版的 NSGA2 多目标优化器"""
    def __init__(self, n_var: int, pop_size: int, n_gen: int):
        self.n_var = n_var
        self.pop_size = pop_size
        self.n_gen = n_gen
        
    def optimize(self, tracker: ExperimentTracker) -> dict:
        """执行优化过程"""
        # 初始化种群
        population = np.random.random((self.pop_size, self.n_var))
        
        # 优化迭代
        for gen in range(self.n_gen):
            # 记录每代的指标
            objectives = self._evaluate(population)
            tracker.log_metrics({
                "mean_f1": float(np.mean(objectives[:, 0])),
                "mean_f2": float(np.mean(objectives[:, 1]))
            }, step=gen)
            
            # 进化
            population = self._evolve(population)
            
        # 保存最终结果图
        self._save_results(population, tracker)
        
        return {
            "final_population_size": len(population),
            "final_objectives": self._evaluate(population).tolist()
        }
    
    def _evaluate(self, population: np.ndarray) -> np.ndarray:
        """计算目标函数值"""
        f1 = population[:, 0]
        g = 1 + 9 * np.mean(population[:, 1:], axis=1)
        f2 = g * (1 - np.sqrt(f1/g))
        return np.column_stack((f1, f2))
    
    def _evolve(self, population: np.ndarray) -> np.ndarray:
        """简化的进化过程"""
        offspring = population + 0.1 * np.random.normal(0, 1, population.shape)
        return np.clip(offspring, 0, 1)
    
    def _save_results(self, population: np.ndarray, tracker: ExperimentTracker):
        """保存结果图"""
        objectives = self._evaluate(population)
        plt.figure(figsize=(8, 6))
        plt.scatter(objectives[:, 0], objectives[:, 1], alpha=0.6)
        plt.xlabel('f1')
        plt.ylabel('f2')
        plt.title('Pareto Front')
        tracker.log_artifact("pareto_front.png", plt.gcf(), "figure")
        plt.close()

@experiment_manager(
    times=3,
    experiment_name="nsga2_test",
    parallel=True
)
def run_optimization(tracker: ExperimentTracker) -> dict:
    """运行优化实验"""
    # 设置参数
    pop_size = np.random.choice([50, 100, 200])
    tracker.log_params({
        "dimension": 30,
        "population_size": int(pop_size),
        "generations": 10
    })
    
    # 运行优化
    optimizer = NSGA2Optimizer(
        n_var=30,
        pop_size=pop_size,
        n_gen=10
    )
    return optimizer.optimize(tracker)

if __name__ == '__main__':
    freeze_support()
    results = run_optimization()