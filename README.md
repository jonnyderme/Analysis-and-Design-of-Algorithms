# 📘 Analysis and Design οf Algorithms – Optional Assignment (2024)

Optional coursework for the **Analysis and Design οf Algorithms** course  
Faculty of Engineering, AUTh  
School of Electrical and Computer Engineering  
Electronics and Computers Department

📚 *Course:*  Analysis and Design οf Algorithms   
🏛️ *Faculty:* AUTh - School of Electrical and Computer Engineering  
📅 *Semester:* 6th Semester, 2023–2024

---

## 🧭 Table of Contents

- [📌 Problem 1: Fuel-Constrained Shortest Path](#-problem-1-fuel-constrained-shortest-path)
- [📌 Problem 2: Optimal Service Queue](#-problem-2-optimal-service-queue)
- [📌 Problem 3: Optimal String Splitting (DP)](#-problem-3-optimal-string-splitting-dp)
- [🧠 Theoretical Tools & Techniques](#-theoretical-tools--techniques)
- [📁 Repository Structure](#-repository-structure)

---

# 📌 Problem 1: Fuel-Constrained Shortest Path

Given an undirected graph G = (V, E) representing cities and roads with edge weights (distances), determine whether there exists a **feasible route** from city `s` to city `t` given a fuel limit `L`:

### ✅ Subtasks:
1. Design an algorithm that checks if a feasible path exists with current tank capacity `L`.
2. Find the **minimum fuel capacity L\*** such that a path exists between `s` and `t`.

### 💡 Insights:
- A BFS/DFS variation can be used with an edge filter (`le ≤ L`).
- Binary search over L combined with Dijkstra’s or DFS ensures optimal `L*`.
- Time complexity can be optimized to **O((|V| + |E|)·log|V|)** using Dijkstra with binary search.

---

# 📌 Problem 2: Optimal Service Queue

You're given the individual service times of `n` citizens arriving in a queue. Rearranging them **minimizes total waiting time**.

### ✅ Solution:
- **Sort citizens by service time in ascending order** (Shortest Job First – SJF).
- This greedy strategy ensures minimal accumulated delays.

### 🕒 Time Complexity: O(n log n)  
### 📏 Justification: Proven using an exchange argument and greedy choice property.

---

# 📌 Problem 3: Optimal String Splitting (DP)

Given a string of length `n` and a list of `m` split points, each **split costs O(k)** where `k` is the substring length. Compute the **minimum total cost** of splitting the string.

### ✅ Approach:
- Apply **dynamic programming** similar to matrix chain multiplication.
- Use a DP table `dp[i][j]` representing the minimum cost of splitting from split point `i` to `j`.

### ⏱️ Time Complexity: O(m²)

---

## 🧠 Theoretical Tools & Techniques

- Graph Algorithms: BFS, DFS, Dijkstra, Binary Search on answer
- Greedy Algorithms: Optimal ordering for scheduling problems
- Dynamic Programming: Cost minimization with subproblem reuse
- Time Complexity Analysis and Proofs of Correctness

---

## 📁 Repository Structure
