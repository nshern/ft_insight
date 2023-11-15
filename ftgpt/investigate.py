# import ftplib

# # Connect to FTP server
# ftp = ftplib.FTP("oda.ft.dk")
# ftp.login()  # login as anonymous

# # List the contents of the current directory (root directory)
# # ftp.retrlines("LIST")

# # Now, based on the output, you can navigate to the correct directory
# # For example, if 'ODAXML' is a directory in the root, you would do:
# # ftp.cwd("ODAXML")


# # If you need to go deeper, you can chain the cwd commands like this:
# ftp.cwd("ODAXML/Referat/samling/20231")
# ftp.retrlines("LIST")
# # When you find the correct directory, you can list its contents too
# # ftp.retrlines('LIST')

# # Close FTP connection
# ftp.quit()

import ftplib
import os

# Connect to FTP server
ftp = ftplib.FTP("oda.ft.dk")
ftp.login()  # login as anonymous

# Navigate to the correct directory
ftp.cwd("ODAXML/Referat/samling/20231")

# Create a directory to store the downloaded files
local_directory = "downloaded_xmls"
os.makedirs(local_directory, exist_ok=True)

# List the files in the directory
files = ftp.nlst()

# Loop through the files and download each one
for file in files:
    # Define local file path
    local_file_path = os.path.join(local_directory, file)

    # Open a local file for writing
    with open(local_file_path, "wb") as local_file:
        # Use FTP RETR command to download the file
        ftp.retrbinary("RETR " + file, local_file.write)
        print(f"Downloaded {file}")

# Close FTP connection
ftp.quit()

print("All files downloaded.")
