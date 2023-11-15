import os

# Define the directory where your text files are located
directory = "./data"

# Define the base name for the output files
output_base = "merged_part_"

# Get a list of text files in the directory
text_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

# Sort the files if necessary
text_files.sort()

# Calculate the number of files to merge into each output file
num_files_per_output = max(1, len(text_files) // 10)

# Initialize counters
file_counter = 0
output_file_number = 1

# Open the first output file
outfile = open(f"{output_base}{output_file_number:02d}.txt", "w")

# Iterate over each file
for filename in text_files:
    # Construct the full file path
    file_path = os.path.join(directory, filename)

    # Open each file in read mode
    with open(file_path, "r") as infile:
        # Read the file's content
        contents = infile.read()

        # Write the file's content to the current output file
        outfile.write(contents)

        # Optionally, write a newline character after each file's content
        outfile.write("\n")

    # Increment the file counter
    file_counter += 1

    # Check if we need to switch to a new output file
    if file_counter >= num_files_per_output and output_file_number < 10:
        # Close the current output file
        outfile.close()

        # Increment the output file number
        output_file_number += 1

        # Reset the file counter
        file_counter = 0

        # Open the next output file
        outfile = open(f"{output_base}{output_file_number:02d}.txt", "w")

# Close the last output file
outfile.close()

print(f"All files have been divided into 10 separate files.")
