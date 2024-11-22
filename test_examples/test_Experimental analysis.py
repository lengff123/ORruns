from orruns.api.experiment import ExperimentAPI

# 创建API实例
api = ExperimentAPI()  # 使用默认数据目录
# 或者指定数据目录
api = ExperimentAPI(data_dir="./optimization_studys")

# 1. 列出最近的实验
recent_experiments = api.list_experiments(last=5)  # 最近5个实验
# 使用模式匹配
optimization_exps = api.list_experiments(pattern="optimization_*")  # 所有以 optimization_ 开头的实验

# 2. 获取特定实验的详细信息
exp_details = api.get_experiment("optimization_study")

# 3. 获取特定运行的详细信息
run_details = api.get_run(
    experiment_name="optimization_study",
    run_id="20240301_123456_7890"
)

# 4. 高级查询
results = api.query_experiments(
    parameter_filters={
        "population_size__gt": 100,  # 种群大小 > 100
        "dimension__eq": 30,         # 维度 = 30
    },
    metric_filters={
        "fitness__lt": 0.5  # 适应度 < 0.5
    }
)

# 5. 获取文件工件
artifacts = api.get_artifacts(
    experiment_name="optimization_study",
    run_id="20240301_123456_7890"
)
# 返回结构如：
{
    "figures": ["convergence.png", "pareto_front.png"],
    "data": ["population.csv", "metrics.json"],
    "others": ["log.txt"]
}

# 6. 加载特定工件
# 加载CSV数据
population_data = api.load_artifact(
    experiment_name="optimization_study",
    run_id="20240301_123456_7890",
    artifact_path="population.csv",
    artifact_type="data"
)

# 加载JSON数据
metrics = api.load_artifact(
    experiment_name="optimization_study",
    run_id="20240301_123456_7890",
    artifact_path="metrics.json",
    artifact_type="data"
)

# 获取图片文件路径
figure_path = api.get_artifact_path(
    experiment_name="optimization_study",
    run_id="20240301_123456_7890",
    artifact_path="convergence.png",
    artifact_type="figure"
)