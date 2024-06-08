import os
import string
import random
import argparse

# List of common file extensions for the random option
COMMON_EXTENSIONS = ['log', 'txt', 'jpg', 'png', 'pdf', 'docx', 'xlsx', 'pptx', 'csv', 'json', 'xml']
MAXIMUM_NUMBER = 10000

def generate_random_filename(length=8):
    """Generate a random filename of a given length using lowercase alphabet."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_files(directory, extension, number, rand):
    """Generate files with specified parameters."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(number):
        filename = generate_random_filename()
        if rand:
            ext = random.choice(COMMON_EXTENSIONS)
        else:
            ext = extension
        filepath = os.path.join(directory, f"{filename}.{ext}")
        open(filepath, 'w').close()

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Create multiple files with specified extensions.")
    parser.add_argument('-d', '--directory', type=str, required=True, help="Directory to place the files")
    parser.add_argument('-e', '--extension', type=str, default='log', help="Type of file to create (default: .log)")
    parser.add_argument('-n', '--number', type=int, default=10, help="Number of files to create (default: 10)")
    parser.add_argument('-r', '--rand', action='store_true', help="Produce files with randomized extensions, overrides -e")

    args = parser.parse_args()

    # Override number if it exceeds the maximum allowed
    if args.number > MAXIMUM_NUMBER:
        print(f"-n has been overridden. Creating {MAXIMUM_NUMBER} files instead of {args.number}.")
        args.number = MAXIMUM_NUMBER

    # Generate files based on the parsed arguments
    generate_files(args.directory, args.extension, args.number, args.rand)

if __name__ == "__main__":
    main()
