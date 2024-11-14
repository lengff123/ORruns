from orruns import ExperimentConfig, repeat_experiment

# 创建配置文件 config.yaml
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

# 加载配置
config = ExperimentConfig("config.yaml")

# 使用配置运行实验
@repeat_experiment(
    times=config.get("experiment.runs", 1),
    parallel=config.get("experiment.parallel", False)
)
def run_optimization(tracker):
    # 记录实验配置
    tracker.log_params(config.config)
    
    # 获取算法参数
    algo_params = config.get("algorithm.parameters", {})
    max_iter = algo_params.get("max_iterations", 100)
    
    # 实验代码...
    pass