import os
import pwd
import sys
from datetime import datetime
import argparse

# Get command line arguments
# Create the parser
parser = argparse.ArgumentParser(description='Find large files in a directory.')

# Add the arguments
parser.add_argument('--path', type=str, default=os.getcwd(), help='The path to search for large files.')
parser.add_argument('--size', type=int, default=10, help='The minimum file size in MB.')

# Parse the arguments
args = parser.parse_args()

path = args.path
size = args.size
large_files = []
file_sizes = []

def get_large_files(search_path) -> None:

    '''
    :param search_path: The path to search for large files
    :return: Nothing
    '''

    for root, dirs, files in os.walk(search_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size > size:
                    file_owner_id = os.stat(file_path).st_uid
                    file_owner = pwd.getpwuid(file_owner_id).pw_name
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    large_file = f'{file_owner}: {file_path}, Size:{file_size:.2f} MB, Created On: {creation_time}'
                    file_sizes.append(file_size)
                    large_files.append(large_file)
            except FileNotFoundError:
                continue


if __name__ == '__main__':
    get_large_files(path)
    print(f"Large files in {path} are:")
    for file in large_files:
        print(file)
    print(f"Total number of files: {len(large_files)}")
    print(f"Total size of files: {sum(file_sizes):.2f} MB")