import datetime

# Path to the log file containing keystrokes with timestamps
log_file = "keystroke_log.txt"


def read_keystroke_data(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def analyze_keystrokes():
    keystroke_data = read_keystroke_data(log_file)

    # Initialize variables for analysis
    total_keystrokes = len(keystroke_data)
    start_time = None
    end_time = None
    key_combinations = {}

    # Iterate over each keystroke
    for keystroke in keystroke_data:
        # Update start and end time
        timestamp_str, keystroke_str = keystroke.split(": ")
        timestamp = datetime.datetime.strptime(
            timestamp_str, "%Y-%m-%d %H:%M:%S")
        if start_time is None or timestamp < start_time:
            start_time = timestamp
        if end_time is None or timestamp > end_time:
            end_time = timestamp

        # Count key combinations
        if keystroke_str in key_combinations:
            key_combinations[keystroke_str] += 1
        else:
            key_combinations[keystroke_str] = 1

    # Calculate total time elapsed
    time_elapsed = (end_time - start_time).total_seconds() / 60  # Convert to minutes

    # Calculate average typing speed
    average_typing_speed = total_keystrokes / time_elapsed

    # Analyze keystroke patterns
    analyze_keystroke_patterns(keystroke_data)  # Remove the 'time_elapsed' argument

    return {
        "total_keystrokes": total_keystrokes,
        "time_elapsed": time_elapsed,
        "average_typing_speed": average_typing_speed,
        "key_combinations": key_combinations
    }


def analyze_keystroke_patterns(keystroke_data):
    # Calculate typing speed
    
    keystroke_str = ' '.join([keystroke.split(": ")[1] for keystroke in keystroke_data])
    # Check for the sequence "Alt+Tab Ctrl+A Ctrl+C Alt+Tab Ctrl+V"
    sequence = "alt tab ctrl a ctrl c alt tab ctrl v"
    if sequence in keystroke_str:
        print("Sequence 'Alt+Tab Ctrl+A Ctrl+C Alt+Tab Ctrl+V' detected! Potential cheating behavior.")

    # Add more analysis logic as needed


# Analyze keystrokes and print the results
analysis_results = analyze_keystrokes()
print("Total Keystrokes:", analysis_results["total_keystrokes"])
print("Time Elapsed (minutes):", analysis_results["time_elapsed"])
print("Average Typing Speed (keystrokes per minute):", analysis_results["average_typing_speed"])


