import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def obj_func(x):
    return x[0]**2 + x[1]**2

def black_hole_algorithm(obj_func, lb, ub, dimension, iteration, population):
    # 初始化种群
    positions = []
    for i in range(population):
        pos = [random.uniform(lb, ub) for j in range(dimension)]
        positions.append(pos)

    # 开始迭代
    for i in range(iteration):
        # 计算每个个体的适应度值
        fitness = [obj_func(pos) for pos in positions]
        # 找到最优个体的位置和适应度值
        best_fitness_idx = fitness.index(max(fitness))
        best_fitness = fitness[best_fitness_idx]
        best_position = positions[best_fitness_idx]
        # 计算每个个体的引力值和距离
        gravity = [0 for j in range(population)]
        distance = [0 for j in range(population)]
        for j in range(population):
            for k in range(dimension):
                gravity[j] += (positions[j][k] - best_position[k])**2
            gravity[j] = gravity[j]**0.5
            distance[j] = 1 / (1 + gravity[j])
        # 更新每个个体的位置
        for j in range(population):
            for k in range(dimension):
                r1 = random.random()
                r2 = random.random()
                attract = r1 * gravity[j] * (best_position[k] - positions[j][k])
                repulse = r2 * distance[j] * (best_position[k] - positions[j][k])
                positions[j][k] += attract - repulse
                if positions[j][k] < lb:
                    positions[j][k] = lb
                elif positions[j][k] > ub:
                    positions[j][k] = ub

    # 找到最优个体的位置和适应度值
    fitness = [obj_func(pos) for pos in positions]
    best_fitness_idx = fitness.index(max(fitness))
    best_position = positions[best_fitness_idx]
    best_fitness = fitness[best_fitness_idx]

    return (best_position, best_fitness)

# 设置搜索空间的下限和上限
lb = -100
ub = 100
# 运行黑洞算法，寻找目标函数的最优解
best_position, best_fitness = black_hole_algorithm(obj_func, lb, ub, dimension=2, iteration=100, population=30)
print(f"Best position: {best_position}")
print(f"Best fitness: {best_fitness}")

# 可视化目标函数的图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.linspace(lb, ub, 100)
X, Y = np.meshgrid(x, y)
Z = obj_func([X, Y])
ax.plot_surface(X, Y, Z, cmap="coolwarm", alpha=0.8)
# 将最优解标出
ax.scatter(best_position[0], best_position[1], best_fitness, c="r", marker="*", s=100)
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
