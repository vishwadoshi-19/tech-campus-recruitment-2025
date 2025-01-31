const fs = require("fs");
const path = require("path");
const readline = require("readline");

// Function to extract logs
async function extractLogs(logFile, date) {
  const outputDir = "../output";
  const outputFile = path.join(outputDir, `output_${date}.txt`);

  // Create the output directory if it doesn't exist
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  try {
    const fileStream = fs.createReadStream(logFile); // Create a readable stream
    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity, // Recognize all instances of CR LF as a single line break
    });

    const outputStream = fs.createWriteStream(outputFile, { flags: "w" });

    // Read and filter lines
    let foundLogs = false;
    for await (const line of rl) {
      if (line.startsWith(date)) {
        outputStream.write(line + "\n");
        foundLogs = true;
      }
    }

    outputStream.end();

    if (foundLogs) {
      console.log(`Logs for ${date} saved to ${outputFile}`);
    } else {
      console.log(`No logs found for ${date}.`);
    }
  } catch (error) {
    if (error.code === "ENOENT") {
      console.error("Error: Log file not found.");
    } else {
      console.error(`Error: ${error.message}`);
    }
  }
}

// Main script execution
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length !== 1) {
    console.error("Usage: node extractLogs.js YYYY-MM-DD");
    process.exit(1);
  }

  const date = args[0];
  const logFile = "logs_2024.log"; // Update with actual path
  extractLogs(logFile, date);
}
