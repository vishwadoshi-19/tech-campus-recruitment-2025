import random
import datetime

LOG_LEVELS = ["INFO", "ERROR", "WARN", "DEBUG"]
MESSAGES = [
    "User logged in",
    "Failed to connect to the database",
    "Disk space running low",
    "User logged out",
    "File uploaded successfully",
    "Server restarted",
    "Unauthorized access attempt",
    "Memory usage high",
    "Application crashed unexpectedly",
    "Connection timeout occurred"
]

START_DATE = datetime.date(2023, 1, 1)  # Start of logs
END_DATE = datetime.date(2024, 12, 31)  # End of logs
LOGS_PER_DAY = 100  # Number of logs per day
LOG_FILE = "test_logs.log"


def generate_random_log(date):
    """Generate a random log entry for a given date."""
    time = datetime.timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    timestamp = f"{date} {str(time)}"
    log_level = random.choice(LOG_LEVELS)
    message = random.choice(MESSAGES)
    return f"{timestamp} {log_level} {message}"


def create_log_file():
    """Generate a large log file with evenly distributed logs."""
    with open(LOG_FILE, "w") as f:
        current_date = START_DATE
        while current_date <= END_DATE:
            for _ in range(LOGS_PER_DAY):
                log_entry = generate_random_log(current_date)
                f.write(log_entry + "\n")
            current_date += datetime.timedelta(days=1)
    print(f"Log file '{LOG_FILE}' generated successfully!")


if __name__ == "__main__":
    create_log_file()
