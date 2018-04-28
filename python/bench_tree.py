import psutil
import random
from timeit import default_timer as timer
from black_red_tree import BlackRedTree


def get_memory_usage():
    return psutil.virtual_memory().active / float(2 ** 20)


if __name__ == '__main__':
    process_start_memory = get_memory_usage()

    tree = BlackRedTree()

    input_size = 2000000

    input_values = random.sample(range(-10000000, 10000000), input_size)

    random.shuffle(input_values)

    start_memory = get_memory_usage()

    end_memory = start_memory

    start_time_insert = timer()

    for i, value in enumerate(input_values):
        if (i % 10000) == 0:
            memory = get_memory_usage()

            if memory > end_memory:
                end_memory = memory

        tree.insert(value)

    end_time_insert = timer()

    start_time_min = timer()

    tree.min()

    end_time_min = timer()

    start_time_max = timer()

    tree.max()

    end_time_max = timer()

    start_time_find = timer()

    tree.find(random.randint(-1000, 1000))

    end_time_find = timer()

    print(
        'Time to insert {} values: {:.5f} seconds'
        .format(input_size, end_time_insert - start_time_insert),

        'Time to find min value in a tree: {:.8f} seconds'
        .format(end_time_min - start_time_min),

        'Time to find max value in a tree: {:.8f} seconds'
        .format(end_time_max - start_time_max),

        'Time to find random value in a tree: {:.8f} seconds'
        .format(end_time_find - start_time_find),

        'Memory used to store {} values: {:.5f} MB'
        .format(input_size, end_memory - start_memory),

        'Total memory usage of a process: {:.5f} MB'
        .format(end_memory - process_start_memory),

        sep='\n'
    )
