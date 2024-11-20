import re
import tkinter as tk
import os

def export_to_html():
    html_content = ""
    html_content += "<h1>Log File Analyzer Results</h1>"
    html_content += "<p>Average times (in minutes):</p>"
    html_content += "<ul>"
    for operation, avg_time in average_times.items():
        html_content += f"<li>{operation.capitalize()}: {avg_time:.2f} minutes</li>"
    html_content += "</ul>"
    html_content += f"<p>Total duration of all test executions: {total_hours:.2f} hours</p>"
    
    script_dir = os.path.dirname(__file__)
    output_file = os.path.join(script_dir, "results.html")
    
    with open(output_file, "w") as file:
        file.write(html_content)

# Define the log file path
log_file_path = 'C:/Users/lovim/Documents/Calculator/PerfTest.2024-03-11.log'

# Define regex patterns to match the relevant log lines
patterns = {
    'getting': re.compile(r'Getting 1000 cardholders took (\d+) seconds in average.'),
    'updating': re.compile(r'Updating 1000 cardholders took (\d+) seconds in average.'),
    'creating': re.compile(r'Creating 1000 cardholders took (\d+) seconds in average.'),
    'deleting': re.compile(r'Deleting 1000 cardholders took (\d+) seconds in average.')
}

# Initialize lists to store the extracted times
times = {
    'getting': [],
    'updating': [],
    'creating': [],
    'deleting': []
}

# Open and read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        for operation, pattern in patterns.items():
            match = pattern.search(line)
            if match:
                times[operation].append(int(match.group(1)))

# Convert times from seconds to minutes and calculate averages
average_times = {operation: sum(times[operation]) / len(times[operation]) / 60 for operation in times}

# Create the main window
root = tk.Tk()
root.title("Log File Analyzer")

# Create a label to display the results
label = tk.Label(root, text="Average times (in minutes):")
label.pack()

# Create a text box to display the results
text_box = tk.Text(root, height=10, width=40)
text_box.pack()

# Insert the results into the text box
for operation, avg_time in average_times.items():
    text_box.insert(tk.END, f"{operation.capitalize()}: {avg_time:.2f} minutes\n")

# Calculate the total duration of all test executions in hours
total_seconds = sum(sum(times[operation]) for operation in times)
total_hours = total_seconds / 3600

# Create a label to display the total duration
total_duration_label = tk.Label(root, text=f"Total duration of all test executions: {total_hours:.2f} hours")
total_duration_label.pack()

# Create a button to close the window
button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

# Start the main loop
root.mainloop()

# Define the log file path
log_file_path = 'C:/Users/lovim/Documents/Calculator/PerfTest.2024-03-11.log'

# Define regex patterns to match the relevant log lines
patterns = {
    'getting': re.compile(r'Getting 1000 cardholders took (\d+) seconds in average.'),
    'updating': re.compile(r'Updating 1000 cardholders took (\d+) seconds in average.'),
    'creating': re.compile(r'Creating 1000 cardholders took (\d+) seconds in average.'),
    'deleting': re.compile(r'Deleting 1000 cardholders took (\d+) seconds in average.')
}

# Initialize lists to store the extracted times
times = {
    'getting': [],
    'updating': [],
    'creating': [],
    'deleting': []
}

# Open and read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        for operation, pattern in patterns.items():
            match = pattern.search(line)
            if match:
                times[operation].append(int(match.group(1)))

# Convert times from seconds to minutes and calculate averages
average_times = {operation: sum(times[operation]) / len(times[operation]) / 60 for operation in times}

# Calculate the total duration of all test executions in hours
total_seconds = sum(sum(times[operation]) for operation in times)
total_hours = total_seconds / 3600

# Print the results
print("Average times (in minutes):")
for operation, avg_time in average_times.items():
    print(f"{operation.capitalize()}: {avg_time:.2f} minutes")

print(f"\nTotal duration of all test executions: {total_hours:.2f} hours")


export_to_html()



