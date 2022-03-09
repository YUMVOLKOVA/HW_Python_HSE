import time
from threading import Thread
from multiprocessing import Process


def fibonacci(n):
    list_with_numbers = [0, 1]
    if n == 1:
        return list_with_numbers[0]
    elif n == 2:
        return list_with_numbers[1]
    else:
        for i in range(1, n):
            list_with_numbers.append(list_with_numbers[i] + list_with_numbers[i - 1])
        return list_with_numbers


def save_results(path, **results):
    print('saving')
    f = open(path, "w")
    for key in results:
        f.write(f'{key}: {results[key]} \n')
    f.close()


params = {'n': 10,
          'n_flows': 10}

if __name__ == '__main__':
    result_dict = {}

    start_1 = time.perf_counter()
    for i in range(params['n_flows']):
        fibonacci(params['n'])
    end_1 = time.perf_counter()
    total_time_1 = end_1 - start_1
    result_dict['Sequential'] = str(total_time_1)
    print(f'done with Sequential, result: {total_time_1}')

    start_2 = time.perf_counter()
    list_threads = [Thread(target=fibonacci, args=(params['n'],)) for i in range(params['n_flows'])]
    for i in list_threads:
        i.start()
    for i in list_threads:
        i.join()
    end_2 = time.perf_counter()
    total_time_2 = end_2 - start_2
    result_dict['Thread'] = str(total_time_2)
    print(f'done with Thread, result: {total_time_2}')

    start_3 = time.perf_counter()
    list_process = [Process(target=fibonacci, args=(params['n'],)) for i in range(params['n_flows'])]
    for i in list_process:
        i.start()
    for i in list_process:
        i.join()
    end_3 = time.perf_counter()
    total_time_3 = end_3 - start_3
    result_dict['Process'] = str(total_time_3)
    print(f'done with Process, result: {total_time_3}')

    path_ = 'artifacts/easy.txt'
    save_results(path_, **result_dict)
