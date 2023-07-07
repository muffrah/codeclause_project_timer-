import time

def timer(seconds):
    print(f"Timer started for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up!")

def stopwatch():
    print("Stopwatch started. Press enter to stop.")
    input("Press enter to start...")
    start_time = time.time()
    input("Press enter to stop...")
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Example usage
timer(10)  # Start a timer for 10 seconds
print()
stopwatch()  # Start a stopwatch
