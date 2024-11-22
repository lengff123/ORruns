from multiprocessing import freeze_support
import numpy as np
from orruns import ExperimentTracker, experiment_manager
import matplotlib.pyplot as plt

class TSPSolver:
    """旅行商问题求解器"""
    def __init__(self, n_cities: int, n_iter: int):
        self.n_cities = n_cities
        self.n_iter = n_iter
        self.cities = np.random.rand(n_cities, 2)  # 随机生成城市坐标
        
    def solve(self, tracker: ExperimentTracker) -> dict:
        """求解TSP"""
        # 初始解
        current_path = np.random.permutation(self.n_cities)
        best_distance = self._calculate_distance(current_path)
        distances = [best_distance]
        
        # 迭代优化
        for i in range(self.n_iter):
            # 2-opt局部搜索
            new_path = self._two_opt(current_path.copy())
            new_distance = self._calculate_distance(new_path)
            
            # 更新最优解
            if new_distance < best_distance:
                current_path = new_path
                best_distance = new_distance
            
            distances.append(float(best_distance))  # 转换为Python float
            
            # 记录每次迭代的指标
            tracker.log_metrics({
                "best_distance": float(best_distance),
                "current_distance": float(new_distance)
            }, step=i)
        
        # 保存收敛曲线
        self._plot_convergence(distances, tracker)
        
        # 保存最优路径图
        self._plot_route(current_path, tracker)
        
        # 保存详细结果数据
        tracker.log_artifact(
            "distances.csv", 
            np.array(distances), 
            "data"
        )
        
        return {
            "distances": distances,
            "best_path": current_path.tolist(),
            "best_distance": float(best_distance)
        }
    
    def _calculate_distance(self, path: np.ndarray) -> float:
        """计算路径总长度"""
        points = self.cities[path]
        return float(np.sum(np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1))))
    
    def _two_opt(self, path: np.ndarray) -> np.ndarray:
        """2-opt局部搜索"""
        i, j = np.random.randint(0, self.n_cities, 2)
        if i > j:
            i, j = j, i
        path[i:j+1] = path[i:j+1][::-1]
        return path
    
    def _plot_convergence(self, distances: list, tracker: ExperimentTracker):
        """绘制收敛曲线"""
        plt.figure(figsize=(10, 6))
        plt.plot(distances)
        plt.xlabel('Iteration')
        plt.ylabel('Distance')
        plt.title('Convergence Curve')
        tracker.log_artifact("convergence.png", plt.gcf(), "figure")
        plt.close()
    
    def _plot_route(self, path: np.ndarray, tracker: ExperimentTracker):
        """绘制路径图"""
        plt.figure(figsize=(8, 8))
        points = self.cities[path]
        plt.plot(points[:, 0], points[:, 1], 'b-')
        plt.plot(points[[0, -1], 0], points[[0, -1], 1], 'b-')
        plt.scatter(self.cities[:, 0], self.cities[:, 1], c='red')
        plt.title('Best Route')
        tracker.log_artifact("route.png", plt.gcf(), "figure")
        plt.close()

@experiment_manager(
    times=5,
    experiment_name="tsp_study",
    parallel=True,
    merge_config={
        "arrays": ["distances"],  # 合并距离数组
        "scalars": ["best_distance"],  # 合并最优距离
        "images": ["convergence.png", "route.png"],  # 保存所有图像
        "distributions": ["distances"]  # 分析距离分布
    },
    system_info_level='basic',
)
def experiment(tracker: ExperimentTracker) -> dict:
    """比较不同城市规模的性能"""
    # 随机选择城市数量
    n_cities = np.random.choice([20, 30, 40])
    
    # 记录参数
    tracker.log_params({
        "n_cities": int(n_cities),
        "n_iterations": 1000
    })
    
    # 求解TSP
    solver = TSPSolver(n_cities, n_iter=10)
    results = solver.solve(tracker)
    
    return results

if __name__ == '__main__':
    freeze_support()
    results = experiment()