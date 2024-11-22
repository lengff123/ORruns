from multiprocessing import freeze_support
from optimization import optimize_function

if __name__ == '__main__':
    freeze_support()
    results = optimize_function(dimension=5)
    print(f"Experiment results: {results}")