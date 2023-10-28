# Gtsp

​	广义旅行商问题（Generalized Traveling Salesman Problem，GTSP）是旅行商问题（Traveling Salesman Problem，TSP）的一个扩展版本。在TSP中，旅行商要找到一条最短路径，经过每个城市一次，并回到起始城市。而在GTSP中，城市被分为不同的集群（clusters），旅行商需要选择每个集群中的一个城市进行访问，并返回起始城市。

​	本仓库实现了两种方法（禁忌搜索、蚁群算法）解决Gtsp问题，并将其性能进行对比。

# 测试方法

1. 测试单个算法

   ```shell
   python tabu_gtsp.py
   ```

   ```shell
   python aco_gtsp.py
   ```

2. 算法对比

   ```shell
   python cmp.py
   ```

   

