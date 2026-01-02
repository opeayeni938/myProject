def largest_square(n):
    # Initialization
    i = 0
    q = 0
    
    # Loop condition: Check if the next integer squared is still within n
    while (i + 1) * (i + 1) <= n:
        # Increment i and update the square value
        i = i + 1
        q = i * i
        
    return q

# Main execution
n_value = 31
result = largest_square(n_value)
print(f"For n = {n_value}, the largest square q is {result}")

# Testing additional cases
print(f"For n = 8, q = {largest_square(8)}")
print(f"For n = 0, q = {largest_square(0)}")
