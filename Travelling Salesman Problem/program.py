import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")
vertices = 15
x = np.random.randint(low=0, high=100, size=vertices)
y = np.random.randint(low=0, high=100, size=vertices)
print("x =", x)
print("y =", y)

xs = []
ys = []
edge_cost = []
for i in range(vertices):
    for j in range(vertices):
        xs.append(x[i])
        ys.append(y[i])
        xs.append(x[j])
        ys.append(y[j])
        calculate_cost = np.sqrt(np.square(abs(x[i] - x[j])) + np.square(abs(y[i] - y[j])))
        edge_cost.append(calculate_cost)
edge_cost = np.reshape(edge_cost, (vertices, vertices))
print(edge_cost)

def draw_MST(result):
    result_x = []
    result_y = []
    for i in range(len(result)-1):
        result_x.append(x[result[i]])
        result_y.append(y[result[i]]) 
        result_x.append(x[result[i+1]])
        result_y.append(y[result[i+1]]) 
        plt.plot(result_x,result_y,color="blue",zorder=1)

def primMST():
    reached = []
    unreached = []
    unreached = [v for v in range(vertices)]
    reached.append(unreached[0])
    unreached.pop(0) # removes element at the specified index
    while len(unreached) > 0:
        record = 10000
        uIndex = 0
        cost = 0
        for i in range(len(reached)):
            for j in range(len(unreached)):
                v1 = reached[i]
                v2 = unreached[j]
                d = edge_cost[v1][v2]
                if d < record:
                    record = d
                    uIndex = j
                    cost = cost + record
        reached.append(unreached[uIndex])
        unreached.pop(uIndex)
    reached.append(0)
    print("Path :", reached)
    print("Cost :", cost)
    return reached

def draw_graph():
    result = primMST()
    plt.scatter(x,y,color="red",zorder=2)
    plt.plot(xs,ys,color="gray",zorder=0)
    for i in range(vertices):
        plt.text(x[i], y[i], i, color="black", fontsize=17, zorder=3)
    draw_MST(result)
    plt.axis([-10, 110, -10 , 110])
    plt.show()

if __name__ == "__main__":
    draw_graph()