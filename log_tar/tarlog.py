import os
import tarfile
import argparse
from datetime import datetime

def create_tarball(input_dir, output_dir):
    """
    Creates a tarball of all .log files in the input directory and saves it to the output directory.

    Args:
        input_dir (str): Directory containing .log files.
        output_dir (str): Directory to save the tarball.
    """
    # List all .log files in the input directory
    log_files = [f for f in os.listdir(input_dir) if f.endswith('.log')]

    if not log_files:
        print("No .log files found in the input directory.")
        return

    # Create the tarball filename with a timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    tarball_name = os.path.join(output_dir, f'{timestamp}_logs.tar.gz')

    # Open a tarball file for writing with gzip compression
    with tarfile.open(tarball_name, 'w:gz') as tar:
        for log_file in log_files:
            # Add each log file to the tarball
            file_path = os.path.join(input_dir, log_file)
            tar.add(file_path, arcname=log_file)
            print(f"Added {file_path} to tarball.")

    print(f"Tarball created at {tarball_name}")

def purge_files(input_dir):
    """
    Deletes all .log files in the input directory.

    Args:
        input_dir (str): Directory containing .log files to delete.
    """
    # List all .log files in the input directory
    log_files = [f for f in os.listdir(input_dir) if f.endswith('.log')]

    for log_file in log_files:
        # Delete each log file
        file_path = os.path.join(input_dir, log_file)
        os.remove(file_path)
        print(f"Deleted {file_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Tarball all .log files in a given directory and save them to a given output directory.')
    parser.add_argument('-d', '--directory', required=True, help='Directory of input .log files.')
    parser.add_argument('-o', '--output', help='Directory to save the tarball. If not given, saves to the input directory.')
    parser.add_argument('-p', '--purge', action='store_true', help='Purge original log files after creating the tarball.')

    args = parser.parse_args()

    input_dir = args.directory
    output_dir = args.output if args.output else input_dir

    # Check if input directory exists
    if not os.path.isdir(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return

    # Check if output directory exists, create it if it doesn't
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Create the tarball
    create_tarball(input_dir, output_dir)

    # Purge the original log files if the purge flag is set
    if args.purge:
        purge_files(input_dir)

if __name__ == '__main__':
    main()
