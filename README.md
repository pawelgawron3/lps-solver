# 🔤 Longest Prefix-Suffix Solver

This repository contains two alternative (Python & Go) implementations designed to solve the **Longest Prefix-Suffix (LPS)** problem. The project explores both the highly efficient, linear-time Knuth-Morris-Pratt (KMP) prefix function and an advanced Suffix Array structure to find the longest proper prefix of a string that is also its suffix.

---

## 🚀 Features

- **Dual Approach:** Solve the exact same problem using two completely different algorithmic methodologies.
- **Stream-Ready:** Input handling is fully compatible with standard input (`stdin`) redirection, making it perfect for automated grading platforms.
- **Data Generator:** A helper script to easily generate large-scale test cases (for example ~500k characters) to benchmark both implementations.
- **Clean Code:** Clean, modular Python & Go implementations with error handling for empty inputs.

---

## 🛠️ Tech Stack

- Python - used for the KMP core algorithm and the test data generator.
- Go (Golang) - used for the Suffix Array solver to achieve native, low-level execution speed.
- `index/suffixarray` - Go's highly optimized built-in library utilizing the **SA-IS** algorithm for linear-time suffix array construction.

---

## 📊 Algorithm Complexity

Both approaches have $O(n)$ Time Complexity and $O(n)$ Space Complexity.

| File                       | Language | Algorithm             | Time Complexity | Space Complexity |
| :------------------------- | :------- | :-------------------- | :-------------- | :--------------- |
| `solution_kmp.py`          | Python   | KMP (Prefix Function) | $O(n)$          | $O(n)$           |
| `solution_suffix_array.go` | Go       | Suffix Array (SA-IS)  | $O(n)$          | $O(n)$           |

> 💡 **Architectural Note:** A Suffix Array is structurally isomorphic to a Suffix Tree. I chose Go's Suffix Array implementation to avoid the extreme memory pointer overhead and garbage collection pressure that standard object-oriented Suffix Trees (like Python's suffix-trees external library) introduce when handling 500k+ character strings.

---

## 💻 How to Run

### 🔧 Prerequisites

No external libraries or third-party packages are required. Both Python and Go standard libraries have everything built-in.

---

### 🧪 Generating Test Data

Before benchmarking, you can generate a heavy (almost 500k characters) test file (`input.txt`) with a specific pattern using the Python helper script:

```bash
python generate_data.py
```

---

### 🏃 Running the Solvers

Both programs accept data via standard input (stdin). Use your terminal of choice to inject the input.txt file into the scripts:

- On Linux / macOS / Windows CMD:

```bash
# Run KMP version (Python)
python solution_kmp.py < input.txt

# Run Suffix Array version (Go)
go run solution_suffix_array.go < input.txt
```

- On Windows PowerShell:

```bash
# Run KMP version (Python)
cat input.txt | python solution_kmp.py

# Run Suffix Array version (Go)
cat input.txt | go run solution_suffix_array.go
```

---

## 📋 Problem Description

Below is the original task statement provided in Polish language during the uni assignment:

![Task description](assets/task.png)
