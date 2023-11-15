import ftplib
import xml.etree.ElementTree as ET

# Connect to FTP server
ftp = ftplib.FTP("oda.ft.dk")
ftp.login()  # login as anonymous

# Change to the desired directory
ftp.cwd("ODAXML/Referat/20161")  # Example directory

# List files and download
files = ftp.nlst()
for file in files:
    with open(file, "wb") as local_file:
        ftp.retrbinary("RETR " + file, local_file.write)

# Parse a downloaded XML file
tree = ET.parse("example_file.xml")
root = tree.getroot()

# Extract information from XML (example)
for element in root.findall("yourElement"):
    print(element.text)

# Close FTP connection
ftp.quit()
