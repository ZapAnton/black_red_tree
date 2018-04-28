import psutil
import random
from timeit import default_timer as timer
from black_red_tree import BlackRedTree


def get_memory_usage():
    return psutil.virtual_memory().active / float(2 ** 20)


if __name__ == '__main__':
    process_start_memory = get_memory_usage()

    tree = BlackRedTree()

    input_size = 5000000

    input_values = [random.randint(-1000, 1000) for _ in range(input_size + 1)]

    random.shuffle(input_values)

    start_memory = get_memory_usage()

    end_memory = start_memory

    start_time = timer()

    for i, value in enumerate(input_values):
        if (i % 10000) == 0:
            memory = get_memory_usage()

            if memory > end_memory:
                end_memory = memory

        tree.insert(value)

    end_time = timer()

    print(
        'Time to insert {} values: {:.5f} seconds'
        .format(input_size, end_time - start_time),

        'Memory used to store {} values: {:.5f} MB'
        .format(input_size, end_memory - start_memory),

        'Total memory usage of a process: {:.5f} MB'
        .format(end_memory - process_start_memory),

        sep='\n'
    )
