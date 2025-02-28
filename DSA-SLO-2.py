# def print_pairs(numbers):
#     for i in numbers:
#         for j in numbers:
#             print(f"{i} * {j} = {i * j}")

# # Test it
# my_list = [1, 2, 3]
# print_pairs(my_list)

def print_pairs_three_times(lst):
    for i in lst:
        for j in lst:
            print(f"{i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} ")
            print(f"{i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} ")
            print(f"{i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} ")
            
print_pairs_three_times([1,1,1,1,1,1,1])



### Problem 1: Constant Time (O(1))
#**Code:**

def get_first(lst):
    return lst[0]
# ```
# - **Your Guess:** O(1) because it has one operation.
# - **Analysis:**
#   - You’re right! Accessing an element by index in a Python list (array) takes constant time, regardless of the list size `n`.
#   - Total steps = 1 (index lookup).
#   - **Time Complexity:** O(1).
# - **Why Correct:** It’s a single, fixed operation—no loops, no scaling with input size.
# - **Covers:** Any problem with a fixed number of operations (e.g., accessing, assigning).

# ---

### Problem 2: Logarithmic Time (O(log n))
#**Code:**
def count_halves(n):
    count = 0
    while n > 1:
        count += 1
        n = n // 2
    return count
# ```
# - **Your Guess:** O(log n) because “loop was running n times but halving the n value so on adding inputs the outputs gradually decrease.”
# - **Analysis:**
#   - Spot-on! The loop runs until `n` becomes 1 or less, halving `n` each time.
#   - Steps: `n → n/2 → n/4 → ... → 1`.
#   - Number of iterations = `floor(log₂(n))` (e.g., `n = 16`: 4 steps—`16 → 8 → 4 → 2 → 1`).
#   - **Time Complexity:** O(log n).
# - **Why Correct:** You nailed the halving pattern—doubling `n` only adds one more step, a logarithmic trait.
# - **Covers:** Algorithms that divide the problem size (e.g., binary search, some tree traversals).

# ---

### Problem 3: Linear Time (O(n))
#**Code:**
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
# ```
# - **Your Guess:** O(n) because “loop was running n times on adding n output grows linearly.”
# - **Analysis:**
#   - Perfect! The `for` loop iterates exactly `n` times (length of `lst`).
#   - Each iteration does a constant-time addition.
#   - Total steps = `n`.
#   - **Time Complexity:** O(n).
# - **Why Correct:** You recognized the single loop and linear growth—doubling `n` doubles the steps.
# - **Covers:** Single-pass algorithms (e.g., linear search, summing, mapping).

# ---

### Problem 4: Linearithmic Time (O(n log n))
#**Code:**
def merge_sort_simulation(lst):
    n = len(lst)
    for i in range(n):           # n times
        temp = n
        while temp > 1:          # log n times
            steps += 1
            temp = temp // 2
    return steps
# ```
# - **Your Guess:** O(n log n) because “for loop runs n time and while loop runs log n times because halving the n value so on adding inputs the outputs gradually decrease.”
# - **Analysis:**
#   - Exactly right! Let’s break it:
#     - Outer `for` loop: Runs `n` times.
#     - Inner `while` loop: For each `i`, `temp` starts at `n` and halves until ≤ 1 (~`log₂(n)` steps).
#     - Total steps = `n * log₂(n)` (e.g., `n = 4`: 4 * 2 = 8 steps).
#   - **Time Complexity:** O(n log n).
# - **Why Correct:** You saw the `n` from the outer loop and `log n` from the halving—multiplying them is O(n log n).
# - **Covers:** Efficient sorting (merge sort, quicksort), divide-and-conquer algorithms.

# ---

### Problem 5: Quadratic Time (O(n²))
#**Code:**
def print_all_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)
# ```
# - **Your Guess:** O(n²) because “nested loop adding n doubles the output.”
# - **Analysis:**
#   - Yep, nailed it!
#     - Outer loop: `n` times.
#     - Inner loop: `n` times per outer iteration.
#     - Total steps = `n * n = n²` (e.g., `n = 3`: 9 prints).
#   - **Time Complexity:** O(n²).
# - **Why Correct:** You caught the nested loops multiplying—doubling `n` quadruples the steps (e.g., `n = 2`: 4; `n = 4`: 16).
# - **Covers:** Brute-force pair-checking (e.g., bubble sort, finding duplicates).

# ---

### Problem 6: Cubic Time (O(n³))
#**Code:**
def triple_loops(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
# ```
# - **Your Guess:** O(n³) because “triple nested loop adding n triples the output.”
# - **Analysis:**
#   - Perfect!
#     - Three nested loops, each running `n` times.
#     - Total steps = `n * n * n = n³` (e.g., `n = 2`: 8 prints).
#   - **Time Complexity:** O(n³).
# - **Why Correct:** You saw three levels of nesting—doubling `n` increases steps by 8 (2³).
# - **Covers:** Multi-dimensional problems (e.g., naive matrix multiplication, triple combinations).

# ---

### Problem 7: Exponential Time (O(2ⁿ))
# **Code:**

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
# ```
# - **Your Guess:** O(2ⁿ) because “recursion calls each function calls next function and next function calls next one so formed an exponential behavior.”
# - **Analysis:**
#   - You’re right on the money!
#     - Each call splits into 2 recursive calls: `f(n-1)` and `f(n-2)`.
#     - Forms a binary tree of calls, depth ~`n`.
#     - Total calls ≈ `2ⁿ` (e.g., `n = 5`: ~20 calls, close to 32).
#     - Exact complexity is O(φⁿ) (where φ ≈ 1.618, the golden ratio), but O(2ⁿ) is a close upper bound and commonly accepted.
#   - **Time Complexity:** O(2ⁿ).
# - **Why Correct:** You spotted the exponential explosion—each level doubles the work.
# - **Covers:** Naive recursive solutions (e.g., subset generation, traveling salesman).

# ---

# ### Your Score: 7/7!
# You got every single one right! Your reasoning is solid:
# - **O(1):** Single operation.
# - **O(log n):** Halving pattern.
# - **O(n):** Single loop, linear growth.
# - **O(n log n):** Loop times halving.
# - **O(n²):** Nested loops.
# - **O(n³):** Triple nesting.
# - **O(2ⁿ):** Recursive doubling.

# ### Why These Cover Everything
# These problems represent the major time complexity classes:
# 1. **O(1):** Base case for operations inside loops.
# 2. **O(log n):** Divide-and-conquer, halving (e.g., binary search).
# 3. **O(n):** Single-pass processing (e.g., linear search).
# 4. **O(n log n):** Optimal sorting/merging (e.g., merge sort).
# 5. **O(n²):** Pairwise operations (e.g., bubble sort).
# 6. **O(n³):** Triple operations (e.g., matrix problems).
# 7. **O(2ⁿ):** Combinatorial explosion (e.g., recursion without memoization).

# Most DSA problems are combinations or variations of these:
# - **Sorting:** O(n log n) or O(n²).
# - **Searching:** O(log n) or O(n).
# - **Graphs:** O(V + E) (linear-ish) to O(V²) or O(2ⁿ).
# - **DP:** Reduces exponential to polynomial (e.g., O(n²)).

# ### What’s Next?
# You’re ready to tackle anything! Want to:
# 1. Mix these (e.g., nested O(n) and O(log n))? 
# 2. Try real DSA problems (e.g., binary search, sorting)?
# 3. Explore space complexity too?
# Pick your poison—I’m here to guide you!