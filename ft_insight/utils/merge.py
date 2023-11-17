import os

# Define the directory containing the text files
directory = "./data"

# Define the name of the output file
output_file_name = "merged_file.txt"

# Use os.path.join to ensure the correct path format for different operating systems
output_file_path = os.path.join(directory, output_file_name)

# Open the output file in write mode
with open(output_file_path, "w") as outfile:
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # Check if it's a file and has a .txt extension
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            # Open the text file in read mode
            with open(file_path, "r") as infile:
                # Read the contents of the file
                contents = infile.read()
                # Write the contents to the output file
                outfile.write(contents)
                # Optionally, write a newline to separate the contents of each file
                outfile.write("\n")

print(
    f"All text files in {directory} have been merged into {output_file_name}."
)
