# Friend Chain
# You are given a set of friends identified by 1‑based indices.
# There are several unordered pairs of friends and each pair belongs to a particular company identified by an integer.

# For a specific company, consider the graph that contains only the pairs whose company id matches that company.
# The vertices of the graph are the friends that appear in those pairs, edges are the pairs themselves.

# Your task is to determine, across all companies, the size of the largest connected component.
# If more than one component shares that maximum size, you must compute the greatest product of the two friend ids that belong to the same component among those tied components.
# Return that product.
# If a component has fewer than two friends, its product is defined as zero.

# Input
# Two integers N and M – the number of friends and the number of pairs.
# M lines follow, each containing three integers u v c where u and v are friend indices (1‑based) and c is the company id for that pair.
# Output
# A single integer – the maximum product described above.

# Edge Cases
# A company may have no pairs – it contributes no components.
# A component may consist of a single friend – its product is zero.
# Several companies can have components of the same maximum size – you must compare the products across all those components.
# Duplicate edges should be ignored when counting component size.
# Example
# Input
# 5 4
# 1 2 1
# 2 3 1
# 4 5 2
# 1 3 1

# Output
# 6
# Explanation:

# Company 1 forms a component with friends 1, 2, 3. Its size is 3, the largest size among all companies.
# The two highest ids in that component are 3 and 2, their product is 6.
# Company 2 has a component of size 2, but its size is smaller than the maximum, so it is not considered.
# The answer is 6.

from collections import defaultdict, deque
from  typing import Tuple


# n is the number of friends, m is the number of pairs (edges) and edges is the connections between pairs and companies.
def friend_chain_bfs(n: int, m: int, edges: Tuple):

    company_edges = defaultdict(list)
    for u, v, c in edges:
        company_edges[c].append((u, v))

    max_size = 0
    max_product = 0

    # Build a graph and process it for each company
    for _, pairs in company_edges.items():

        # Adjacency list
        graph = defaultdict(set)
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()

        for start_node in graph:
            if start_node not in visited:

                queue = deque([start_node])
                visited.add(start_node)

                comp_size = 0
                max1, max2 = -1, -1 # track top two ids

                while queue:
                    curr = queue.popleft()
                    comp_size += 1

                    # track the top 2 highest ids
                    if curr > max1:
                        max2 = max1
                        max1 = curr
                    elif curr > max2:
                        max2 = curr

                    # Queue up visited neighbours
                    for neighbour in graph[curr]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)

                product = max1 * max2 if comp_size >= 2 else 0

                if comp_size > max_size:
                    max_size = comp_size
                    max_product = product
                elif comp_size == max_size:
                    max_product = max(max_product, product)

    return max_product

