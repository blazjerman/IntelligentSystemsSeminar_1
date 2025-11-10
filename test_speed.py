from main import *

import time
import matplotlib.pyplot as plt


def test_speed():

    env = mill.env()
    env.reset()
    model = mill.transition_model(env)

    depths = [1, 2, 3, 4, 5, 6, 7]
    times = []

    for d in depths:
        start = time.time()
        minimax(model.clone(), 0, 1, 2, True, float('-inf'), float('inf'), max_depth=d)
        times.append(time.time() - start)

    times_ms = [t * 1000 for t in times]

    plt.plot(depths, times_ms, marker='o')
    plt.xlabel('Search Depth')
    plt.ylabel('Computation Time (ms)')
    plt.title('Minimax Search Time vs Depth')
    plt.grid(True)

    for x, y in zip(depths, times_ms):
        plt.text(x, y, f'{y:.1f} ms', ha='left', va='bottom', fontsize=9)

    plt.show()



if __name__ == "__main__":
    test_speed()


