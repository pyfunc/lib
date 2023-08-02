import os
import hashlib
import sys

sys.path.append('../')

from pyfunc.file.move_file import move_file



# Python script to move duplicated files based on content:

def get_file_hash(file_path):
    # Read the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file content in chunks for memory optimization
        chunk_size = 4096
        file_hash = hashlib.sha256()
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            file_hash.update(chunk)
    return file_hash.hexdigest()

def move_duplicate_files(directory, duplicated):
    # Dictionary to store file hashes and paths
    file_hashes = {}
    # Traverse the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash in file_hashes and file_path != file_hashes[file_hash]:
                duplic = file_hashes[file_hash]
                print(f"move_duplicate_files duplicated: {file_path} => {duplic}")
                # Uncomment the below line to remove duplicate files
                # os.remove(file_path)
                move_file(file_path, '', duplicated)
            else:
                file_hashes[file_hash] = file_path