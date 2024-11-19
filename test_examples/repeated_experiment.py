from multiprocessing import freeze_support
import numpy as np
from orruns.decorators import repeat_experiment
from orruns.tracker import ExperimentTracker
import matplotlib.pyplot as plt
from typing import List, Tuple

class NSGA2Optimizer:
    """简化版的 NSGA2 多目标优化器"""
    def __init__(self, n_var: int, pop_size: int, n_gen: int):
        self.n_var = n_var
        self.pop_size = pop_size
        self.n_gen = n_gen
        
    def zdt1(self, x: np.ndarray) -> Tuple[float, float]:
        """ZDT1 测试函数"""
        f1 = x[0]
        g = 1 + 9 * np.mean(x[1:])
        f2 = g * (1 - np.sqrt(f1/g))
        return f1, f2
        
    def optimize(self, tracker: ExperimentTracker) -> dict:
        """执行优化过程"""
        # 初始化种群
        population = np.random.random((self.pop_size, self.n_var))
        
        # 记录每代的超体积指标
        hypervolumes = []
        
        for gen in range(self.n_gen):
            # 模拟进化过程
            offspring = population + 0.1 * np.random.normal(0, 1, population.shape)
            offspring = np.clip(offspring, 0, 1)
            
            # 计算目标函数值
            pop_objectives = np.array([self.zdt1(x) for x in population])
            off_objectives = np.array([self.zdt1(x) for x in offspring])
            
            # 计算当前代的超体积
            hv = self._calculate_hypervolume(pop_objectives)
            hypervolumes.append(hv)
            
            # 记录每代的指标
            tracker.log_metrics({
                "hypervolume": hv,
                "mean_f1": np.mean(pop_objectives[:, 0]),
                "mean_f2": np.mean(pop_objectives[:, 1])
            }, step=gen)
            
            # 简化的选择过程
            combined = np.vstack((population, offspring))
            combined_obj = np.vstack((pop_objectives, off_objectives))
            
            # 基于非支配排序选择下一代（简化版）
            indices = self._fast_nondominated_sort(combined_obj)[:self.pop_size]
            population = combined[indices]
            
        # 保存最终的帕累托前沿
        final_objectives = np.array([self.zdt1(x) for x in population])
        
        # 绘制帕累托前沿
        plt.figure(figsize=(8, 6))
        plt.scatter(final_objectives[:, 0], final_objectives[:, 1], 
                   c='blue', label='Final Population')
        plt.xlabel('f1')
        plt.ylabel('f2')
        plt.title('Pareto Front')
        plt.legend()
        
        # 保存图像
        tracker.log_artifact("pareto_front.png", plt.gcf())
        plt.close()
        
        return {
            "final_hypervolume": hypervolumes[-1],
            "convergence_rate": (hypervolumes[-1] - hypervolumes[0]) / self.n_gen,
            "pareto_front_size": len(population)
        }
    
    def _calculate_hypervolume(self, objectives: np.ndarray) -> float:
        """计算超体积指标（简化版）"""
        ref_point = np.array([1.1, 1.1])
        sorted_points = objectives[objectives[:, 0].argsort()]
        hv = 0
        for i in range(len(sorted_points)):
            if i == 0:
                height = ref_point[1] - sorted_points[i, 1]
            else:
                height = sorted_points[i-1, 1] - sorted_points[i, 1]
            width = ref_point[0] - sorted_points[i, 0]
            if height > 0:
                hv += height * width
        return hv
    
    def _fast_nondominated_sort(self, objectives: np.ndarray) -> np.ndarray:
        """快速非支配排序（简化版）"""
        n_points = len(objectives)
        domination_count = np.zeros(n_points)
        
        for i in range(n_points):
            for j in range(n_points):
                if i != j:
                    if np.all(objectives[i] <= objectives[j]) and np.any(objectives[i] < objectives[j]):
                        domination_count[j] += 1
        
        return np.argsort(domination_count)

@repeat_experiment(
    times=5,
    experiment_name="optimization_study",
    parallel=True,
    merge_config={
        "arrays": ["population", "objectives"],
        "scalars": ["hypervolume", "runtime"],
        "time_series": ["convergence_history"],
        "distributions": ["fitness_values"],
        "images": ["pareto_front_plot"],
        "text": ["optimization_log"],
    },
    detailed_system_info=True
)
def compare_population_sizes(tracker: ExperimentTracker, dimension: int = 30) -> dict:
    """比较不同种群大小的性能"""
    # 记录实验参数
    pop_size = int(np.random.choice([50, 100, 200]))  # 转换为 Python int
    n_gen = 3
    
    tracker.log_params({
        "dimension": int(dimension),  # 转换为 Python int
        "population_size": pop_size,
        "generations": n_gen
    })
    
    # 创建优化器并执行优化
    optimizer = NSGA2Optimizer(dimension, pop_size, n_gen)
    results = optimizer.optimize(tracker)
    
    # 确保所有返回值都是 Python 原生类型
    results = {
        "population": np.random.random((100, 10)),
        "objectives": np.random.random((100, 2)),
        "hypervolume": 0.75,
        "runtime": 120.5,
        "convergence_history": np.linspace(1.0, 0.1, 100),
        "fitness_values": np.random.normal(0, 1, 1000),
        "pareto_front_plot": plt.figure(),
        "optimization_log": "Optimization completed successfully...",
    }
    return results
if __name__ == '__main__':
    freeze_support()
    
    # 执行重复实验
    results = compare_population_sizes(dimension=30)
  