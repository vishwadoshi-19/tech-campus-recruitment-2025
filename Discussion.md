# Discussion.md

## Solutions Considered

1. **Reading the Entire File into Memory:**

   - This approach would load the entire 1TB log file into memory and filter the lines containing the required date.
   - **Issue:** Not feasible due to high memory consumption and slow processing speed.

2. **Streaming the File Line-by-Line:**

   - Reads the log file line by line and checks if the line starts with the specified date.
   - Writes matching lines to an output file.
   - **Chosen Approach:** Efficient in terms of memory and processing speed since it avoids loading the entire file into memory.

3. **Indexing and Binary Search:**

   - Creating an index of timestamps and using binary search to quickly locate logs for a given date.
   - **Issue:** While highly efficient for repeated queries, the index creation would take significant time and storage.

## Final Solution Summary

The chosen solution reads the log file line-by-line, checks if the line starts with the specified date, and writes matching lines to an output file. This ensures minimal memory usage and efficient processing.

## Steps to Run

1. **Generate a Sample Log File:**

   - Since the provided log file was not downloadable, a script `generate_random_log_file.py` was created to generate a sample log file named `test_logs.log`.
   - Run the script to generate the log file:

     ```sh
     python generate_random_log_file.py
     ```

2. **If the download works , simply download the test_logs.log file from there:**
   To download the log file, run the following command in your terminal:

   - Run the script to generate the log file:
     `curl -L -o test_logs.log "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3#X1xnzrH5s4H_DKEkT_dfBuUT1mFKZuj4cFWNoMJGX98"`

3. **Run the Log Extraction Script:**
   ```sh
   python extract_logs.py YYYY-MM-DD
   ```
   Replace `YYYY-MM-DD` with the desired date.

## Edge Cases Considered

- Non-existent log file (handled with error messages)
- Dates with no log entries (creates an empty output file)
- Large file handling without excessive memory usage
