import math
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import logging
import os
import pandas as pd
import numpy as np


def take_step(arg):
    f, data, step, _ = arg
    logger.info(f'Current argument: \n x: {str(round(data, 5))} \n')
    acc = f(data) * step
    return acc


def integrate_thread(f, a, b, *, n_jobs, n_iter, logger):
    step = (b - a) / n_iter
    arguments = []
    for i in range(n_iter):
        data = a + i * step
        arguments.append((f, data, step, logger))
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        result_ = list(executor.map(take_step, arguments))
    output = sum(result_)
    return output


def integrate_process(f, a, b, *, n_jobs, n_iter, logger):
    step = (b - a) / n_iter
    arguments = []
    for i in range(n_iter):
        data = a + i * step
        arguments.append((f, data, step, logger))
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        result_ = list(executor.map(take_step, arguments))
    output = sum(result_)
    return output


dict_with_functions = {'thread': integrate_thread,
                       'process': integrate_process}

params = {'n_jobs': range(1, os.cpu_count() * 2 + 1),
          'n_iter': 1000,
          'path_log': 'artifacts/medium_logging.txt',
          'path_final': 'artifacts/medium_final.csv',
          'f': math.cos,
          'a': 0,
          'b': math.pi / 2}

if __name__ == "__main__":
    result = {}
    for name, func in dict_with_functions.items():
        print(f'starting name: {name}')
        logging.basicConfig(filename=params['path_log'],
                            level=logging.INFO,
                            format="%(asctime)s -> %(levelname)s  -> %(message)s")
        logger = logging.getLogger(os.path.basename(__file__))
        result[str(name)] = []
        print(params['n_jobs'])
        for job in params['n_jobs']:
            start = time.perf_counter()
            func(f=params['f'],
                 a=params['a'],
                 b=params['b'],
                 n_jobs=job,
                 n_iter=params['n_iter'],
                 logger=logger)
            end = time.perf_counter()
            result[str(name)].append(str(end - start))
        print(f'finished with {name}')
    print(f'result["thread"]: {result["thread"]}')
    print(f'result["process"]: {result["process"]}')

    df = pd.DataFrame({'n_jobs': params['n_jobs'],
                       'thread': result['thread'],
                       'process': result['process']})
    df.to_csv(params['path_final'], index=False)
