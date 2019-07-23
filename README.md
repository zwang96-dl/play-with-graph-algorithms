# play-with-graph-algo

Python implementation of imooc course [玩转图论算法](https://coding.imooc.com/class/370.html), will update as the course going.

Check/fork original repo from course instructor [liuyubobobo](https://github.com/liuyubobobo))!

## Notes
### Chapter 2 图的基本表示

1. 顶点Vertex，边Edge

2. 无向图Undirected Graph，有向图Directed Graph

3. 有权图Weighted Graph，无权图Unweighted Graph

4. 自环边，平行边

5. 没有自环边并且没有平行边的图称为简单图

6. 树是一种无环图

7. 无环图不一定一定是树，比如多个联通分量

8. 联通的无环图是树

9. 生成树就是指包括了原来图中的所有的点并且联通的图，该生成树的边数是V - 1，但是V - 1的边组成的新图并不一定是生成树

10. 只有连通图才有（并且一定有）生成树

11. 一个图一定有生成森林，但是并不一定有生成树（由于是否联通的问题）

12. 对于无向图来说，顶点相邻的边数就是degree

13. 邻接矩阵，邻接表来表示图

14. 邻接矩阵空间复杂度O(V^2)，建图O(E)，查看两点是否相邻O(1)，求一个点的相邻节点O(V)（相当于遍历全部节点）

15. 稀疏图（sparse graph）和稠密图（dense graph）-> 完全图（complete graph）

16. 邻接表的空间复杂度O(V + E)，建图O(E*V)，未优化时查看两点是否相邻O(degree(v))，求一个点的相邻节点O(degree(v))；优化后（使用HashSet）建图O(E)，查看两点是否相邻O(1)

### Chapter 3 图的深度优先遍历