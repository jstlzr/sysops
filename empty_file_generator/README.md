# nfile.py

## Summary

`nfile.py` is a Python script that creates multiple __empty files__ in a given directory. It allows users to customize the file extension, number of files, and directory. Additionally, it can create files with randomized extensions from a list of common file types.

## Features

- **Directory Specification**: Choose the directory where the files will be created.
- **File Extension**: Specify the type of file to create (e.g., `.txt`, `.jpg`, `.log`). Default is `.log`.
- **Number of Files**: Define the number of files to create. Default is 10.
- **Random Extensions**: Option to create files with random extensions from a predefined list of common file types, overriding the specified extension.
- **Maximum Limit**: Hard-coded maximum limit of 10,000 files to prevent excessive file creation.

## Usage

### Command Line Arguments

- `-d --directory`: Directory to place the files. **(Required)**
- `-e --extension`: Type of file to create. Default is `.log`.
- `-n --number`: Number of files to create. Default is 10.
- `-r --rand`: If passed, produces files with randomized extensions and overrides the `-e` option.

### Example Commands

1. **Create 10 `.log` files in the `/var/log/logs` directory:**
   ```sh
   python3 ./nfile.py -d /var/log/logs
   ```

2. **Create 5 `.txt` files in the `/var/log/test` directory:**
   ```sh
   python3 ./nfile.py -d /var/log/test -e txt -n 5
   ```

3. **Create 20 files with random extensions in the `/var/log/random` directory:**
   ```sh
   python3 ./nfile.py -d /var/log/random -n 20 -r
   ```


### Additional Information

- If the specified directory does not exist, the script will create it.
- If the number of files specified exceeds the maximum limit of 10,000, the script will automatically adjust to create 10,000 files and inform the user.

## Requirements

- Python 3.x
