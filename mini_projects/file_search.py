import os
import time
import json
import threading
import sys
import re
import datetime
import hashlib
import subprocess
import logging

"""
File Search and Reporting Utility:

Develop a script that searches for files matching a given pattern and generates a report.
Employ the sys module to handle command-line arguments for specifying search parameters.
Use the os module to traverse directories and search for files based on patterns.
Utilize the time module to measure the time taken for the search process.
Generate a report in JSON format using the json module, including details such as file paths, sizes, and timestamps.
Implement multithreading with the threading module to speed up the file search process.

Hash Verification: Utilize the hashlib module to compute hash values of the searched files for integrity verification. Compare the 
computed hashes with stored hashes to ensure file integrity.

File Compression: Use the subprocess module to invoke an external compression tool (e.g., tar or zip) to create an archive of the matching files. 
Compress the files into a single archive file while preserving the directory structure.

logging file that contains the hash, date accessed, and the file compression file archive. 

sdfs
shutil

"""
directory = "C:/Users/mycol/WebProjects/Elpis" #includes the output directory
archive_output = 'archive.zip'
log_file = 'file_project.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


result = []

def clear_log_file(log_file_path):
    with open(log_file_path, 'w'):
        pass

def generate_report(file_name, date_created, file_size, file_permission):
    report_data = {
        "file_name": file_name,
        "date_created": date_created,
        "file_size": file_size,
        "file_permission": file_permission
    }

    json_string = json.dumps(report_data, indent=4)
    result.append(json_string)
    logging.info(f"report generated!")


def compute_file_hash(file_path):
    hasher = hashlib.sha256()

    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    
    hash_value = hasher.hexdigest()

    logging.info(f"File has computed: {hash_value}")

    return hash_value

def create_archive(source_dir, output_file):
    try:
        subprocess.run(['zip', '-r', output_file, source_dir])
        print('archive success')
    except subprocess.CalledProcessError as e:
        print(f"output {e}")
        logging.error("subprocess error")
    except FileNotFoundError as ferror:
        print(f"output {source_dir}")
        logging.error("ferror")
    except PermissionError as perror:
        print(f"output {perror}")
    except OSError as oserror:
        print(f"{oserror}")

def del_log(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File is not found")

# ---------------------------------------------------------------------------------------------

print("Enter file regex: ")
input = sys.stdin.readline()

start_time = time.perf_counter()

clear_log_file(log_file)


if len(sys.argv) >= 1:
    search_pattern = input.rstrip()
    list_matches = []
    thread_array = []

    for root, directory, files in os.walk(directory):
        for file_name in files:
            match = re.search(search_pattern, file_name)
            if match:
                list_matches.append(match)
                file_metadata = os.stat(os.path.join(root, file_name))

                thread = threading.Thread(target=generate_report(file_name, datetime.datetime.fromtimestamp(file_metadata.st_ctime).isoformat(), file_metadata.st_size, file_metadata.st_mode))
                hash_thread = threading.Thread(target=compute_file_hash(os.path.join(root, file_name)))
                # archive_thread = threading.Thread(target=create_archive(os.path.join(root, file_name).replace('/', '\\'), archive_output))
                thread.start()
                hash_thread.start()
                # archive_thread.start()

                thread.join()
                hash_thread.join()
                # archive_thread.join()

    for entry in result:
        print(entry)
                
else:
    print('no arguments provided')

end_time = time.perf_counter()

total_time = end_time - start_time
print("Total time spent: ", total_time, "seconds")
print("Operation performed on: ", datetime.datetime.now())