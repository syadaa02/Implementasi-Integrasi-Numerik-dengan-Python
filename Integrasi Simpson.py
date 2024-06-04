import time

def f(x):
    return 4 / (1 + x**2)

def simpson_one_third(a, b, n):
    h = (b - a) / n
    x = a
    integral = f(a) + f(b)

    for i in range(1, n):
        x += h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    return (h / 3) * integral

def calculate_pi_approximation(N):
    start_time = time.time()
    integral_approximation = simpson_one_third(0, 1, N)
    end_time = time.time()
    execution_time = end_time - start_time
    return integral_approximation, execution_time

N_values = [10, 100, 1000, 10000]
pi_reference = 3.14159265358979323846

print("N\t\tApproximation\t\tRMS Error\t\tExecution Time")
print("------------------------------------------------------------")
for N in N_values:
    approximation, execution_time = calculate_pi_approximation(N)
    rms_error = abs(approximation - pi_reference)
    print(f"{N}\t\t{approximation}\t{rms_error}\t{execution_time}")
