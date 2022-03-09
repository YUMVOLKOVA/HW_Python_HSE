import math
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import logging
import os


# def init_integrate(f, a, b, *, n_jobs, n_iter):
#     acc = 0
#     step = (b - a) / n_iter
#     for i in range(n_iter):
#         acc += f(a + i * step) * step
#     return acc


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
    output = result_.sum()
    return output


def integrate_process(f, a, b, *, n_jobs, n_iter, logger):
    step = (b - a) / n_iter
    arguments = []
    for i in range(n_iter):
        data = a + i * step
        arguments.append((f, data, step, logger))
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        result_ = list(executor.map(take_step, arguments))
    output = result_.sum()
    return output


dict_with_functions = {'thread': integrate_thread,
                       'process': integrate_process}

params = {'n_jobs': os.cpu_count() * 2,
          'n_iter': 1000,
          'path': 'artifacts/medium',
          'f': math.cos,
          'a': 0,
          'b': math.pi / 2}

if __name__ == "__main__":
    result = {}
    for name, func in dict_with_functions.items():
        logging.basicConfig(filename=os.path.join(params['path'], f'{name}.txt'),
                            level=logging.INFO,
                            format="%(asctime)s ; %(message)s")
        logger = logging.getLogger(os.path.basename(__file__))
        result[str(name)] = []
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
    path_to_save_final = 'artifacts/medium/final.txt'
    file_to_save = open(path_to_save_final, "w")
    file_to_save.write('n_jobs, threading, processing')
    for n, t, p in zip(params['n_jobs'], result['thread'], result['process']):
        file_to_save.write(f'{n}, {t}, {p}')
