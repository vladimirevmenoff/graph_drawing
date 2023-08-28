# graph_drawing

## About

This project is my implementation of Kamada-Kawai graph drawing algorithm

## Theory

Let's say we have a distance $d_{u, v}$ between 2 vertices $u$ and $v$.
The intuition behind this implementation is that probably the distances between verticies in the visualization must somehow correspond to the ones in the graph itself.

How are we going to achevie that? Well, first of all, let's create $l_{i,j} = L \cdot d_{i, j}$, 
We choose L in such a way, that those $l_{i,j}$ will be lenghts, that we want to achive in the visualization. A good way of choosing $L = n / D$ where $D$ is a graph diametr and $n$ is the number of verticies.

Also, let's introduce $k_{i, j} = K / d_{i, j} ^ {2}$ - the spring tensions from the Hook's law. $K = 10$ is belived to be good.

So, what we want to do now is to punish the system for it's edges being not the right lenght, exactly, if we have determened positions $p_{i}, p_{j}$ then their toll/energy will be 
$$k_{i, j} \cdot (||p_{i} - p_{j}|| - l_{i,j}) ^ {2}$$

Let's sum this energy for all unordere pairs of vericies, and get the total energy of the system. Now we just need to minimize the total energy. Some say, Newton-Raphson method is applicable here. But i find it better to use gradient desend method. 

![image](https://github.com/vladimirevmenoff/graph_drawing/assets/58567711/3571a9a4-f285-4852-a0be-508e8de98455)

## Programming

This project is implemented in modular programming style. It has a module generate_graph, that generates a graph in $O(n^2)$ time complexity. And a module springs that find's an optimal layout. And a governence module main, that combines it all together.

## Installing

Well, this repository works out of the box for different platforms(Yes i am a genius). So no need for containerezation. 
Just do

```bash
git clone https://github.com/vladimirevmenoff/graph_drawing
```
