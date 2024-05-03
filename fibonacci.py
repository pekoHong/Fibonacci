import time
import matplotlib.pyplot as plt

# Top-down (recursive) method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Bottom-up (dynamic programming) method
def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Measure execution times for F(1) to F(100) using both methods
n_values = list(range(1, 101))
times_recursive = []
times_dynamic = []
max_n = 0

for n in n_values:
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    elapsed_time_recursive = end_time - start_time
    times_recursive.append(elapsed_time_recursive)

    start_time = time.time()
    fibonacci_dynamic(n)
    end_time = time.time()
    elapsed_time_dynamic = end_time - start_time
    times_dynamic.append(elapsed_time_dynamic)

    if elapsed_time_recursive > 5*60*60:  # If it takes more than 12 hours, stop and record max_n
        max_n = n - 1
        break

# Plotting execution times
plt.figure(figsize=(10, 6))
plt.plot(n_values[:max_n], times_recursive[:max_n], label='Recursive')
plt.plot(n_values[:max_n], times_dynamic[:max_n], label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Fibonacci Calculation')
plt.legend()
plt.grid(True)
plt.savefig('fibonacci_execution_time.png')
plt.show()

# Calculate the degree of overlapping subproblems for F(4) when computing F(5) to F(50)
overlapping_degree = []
for n in range(5, 51):
    start_time = time.time()
    fibonacci_recursive(4)
    end_time = time.time()
    overlapping_degree.append(end_time - start_time)

# Plotting overlapping degree
plt.figure(figsize=(10, 6))
plt.plot(range(5, 51), overlapping_degree)
plt.xlabel('n')
plt.ylabel('Execution Time of F(4) (seconds)')
plt.title('Overlapping Subproblem Degree')
plt.grid(True)
plt.savefig('overlapping_subproblems.png')
plt.show()
