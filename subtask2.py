def process_sequence():
    # Initialization
    n = 0
    s = 0
    m = None  # Using None initially to identify the first number
 
    print("Enter a sequence of natural numbers (end with -1):")
 
    while True:
        # read x command
        try:
            x = int(input())
        except ValueError:
            print("Please enter a valid natural number.")
            continue
 
        # Main Loop Condition: check for terminator -1
        if x == -1:
            break
 
        # Update count and sum
        n += 1
        s += x
 
        # Handling Minimum (m) logic from flowchart
        if n == 1:
            m = x  # First valid number is the initial minimum
        else:
            if x < m:
                m = x
 
    # Post-Loop Logic
    if n == 0:
        m = -1
        a = -1
    else:
        # Basic arithmetic: mean a = s/n
        a = s / n
 
    # Final Output
    print(f"\nResults:")
    print(f"Count (n): {n}")
    print(f"Sum (s): {s}")
    print(f"Minimum (m): {m}")
    print(f"Mean (a): {a}")
 
# Run the algorithm
if __name__ == "__main__":
    process_sequence()
