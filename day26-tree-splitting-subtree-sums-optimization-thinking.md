## 📅 Cyber Daily — Day 26  
### Tree Splitting, Subtree Sums & Optimization Thinking

### 🔍 What I Studied
Solved **LeetCode 1339 – Maximum Product of Splitted Binary Tree**, focusing on evaluating all possible split points efficiently using depth-first search (DFS).

Although this is a DSA problem, it reinforces a core security mindset: analyzing impact at every possible boundary.

---

### 🧠 Core Idea
When a binary tree is split by removing one edge:
- One part becomes a subtree
- The other part is the remaining tree

For each possible split:
product = subtree_sum × (total_sum − subtree_sum)


The goal is to maximize the product before applying modulo.

---

### 🛠️ Technique Used
- Two-pass DFS approach:
  1. First DFS to compute the total sum of the tree
  2. Second DFS to compute subtree sums and evaluate the product at every node
- Track the maximum product across all possible splits

**Time Complexity:** O(n)  
**Space Complexity:** O(h) (recursion stack)

---

### 🔐 Security Connection
This problem mirrors real-world security analysis:

- Subtrees ≈ isolated system components  
- Splitting ≈ segmentation or trust boundaries  
- Evaluating all splits ≈ attack surface analysis  

In security, you don’t just protect the whole system — you evaluate the impact of isolating every component.

---

### ⚠️ Important Lessons
- Always maximize values before applying modulo (data integrity matters)
- Recursive traversal is effective for hierarchical systems
- Optimization problems often reduce to evaluating all boundaries safely

---

### ✅ Takeaway
Efficient algorithms and secure systems are built by analyzing every possible break point, not by guessing the best one.

---

### 📌 Status
✔ Cyber Daily streak continued  
✔ Practiced recursive optimization thinking  
✔ Reinforced boundary-based analysis mindset  
