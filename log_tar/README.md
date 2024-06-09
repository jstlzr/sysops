# tarlog.py

`tarlog.py` is a Python script that creates a tarball of all `.log` files in a specified directory and saves it to a specified output directory. Optionally, it can also delete the original `.log` files after creating the archive. Files are prepended with a timestamp.

## Usage

### Requirements

- Python 3.x

### How to Run

Save the script as `tarlog.py` and run it from the command line with the required arguments.

#### Command Line Arguments

- `-d`, `--directory` (required): Specifies the directory containing the `.log` files.
- `-o`, `--output`: Specifies the directory to save the tarball. If not provided, the tarball is saved in the input directory.
- `-p`, `--purge`: If provided, the original `.log` files are deleted after the tarball is created.

#### Examples

1. **Create a tarball of all `.log` files in `/path/to/logs` and save it to `/path/to/output`**:
   ```bash
   python3 ./tarlog.py -d /path/to/logs -o /path/to/output
   ```

2. **Create a tarball of all .log files in /path/to/logs and save it in the same directory**:
   ```bash
   python3 ./tarlog.py -d /path/to/logs
   ```

3. **Create a tarball and delete the original log files after saving the tarball**:
   ```bash
   python3 ./tarlog.py -d /path/to/logs -o /path/to/output -p
   ```
