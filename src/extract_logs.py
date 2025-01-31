import sys
import os

def extract_logs(log_file, date):
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    try:
        with open(log_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith(date):
                    outfile.write(line)
        print(f"Logs for {date} saved to {output_file}")
    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date = sys.argv[1]
    log_file = "test_logs.log"  # Update with actual path
    extract_logs(log_file, date)
