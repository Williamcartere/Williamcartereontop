import random
import time
from datetime import datetime

def generate_log_entry():
    return f"[AUTO LOG] {datetime.now().isoformat()} {random.randint(10000, 99999)}"

def main():
    print("Running commit activity generator...")
    for i in range(10):
        log_entry = generate_log_entry()
        with open("log.txt", "a") as log_file:
            log_file.write(log_entry + "\n")
        print(f"Log {i+1}: {log_entry}")
        time.sleep(1)

if __name__ == "__main__":
    main()
