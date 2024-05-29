import os
import shutil
import time
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Create directories if they don't exist
def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create a timestamped filename
def get_timestamped_filename(filename):
    timestamp = time.strftime("%Y-%m-%d:%H-%M-%S")
    base, ext = os.path.splitext(filename)
    return f"{timestamp}_{base}{ext}"

class BackupEventHandler(FileSystemEventHandler):
    def __init__(self, watched_dir, backup_dir, exclude_patterns=None):
        self.watched_dir = watched_dir
        self.backup_dir = backup_dir
        self.exclude_patterns = exclude_patterns if exclude_patterns else []

    def should_exclude(self, file_path):
        # Check if the file should be excluded based on name or regex
        for pattern in self.exclude_patterns:
            if re.search(pattern, file_path):
                return True
        return False

    def on_any_event(self, event):
        # Handle created and modified events
        if event.is_directory:
            return

        if event.event_type in ('created', 'modified'):
            self.backup_file(event.src_path)

    def backup_file(self, src_path):
        try:
            # Check if the file should be excluded
            if self.should_exclude(src_path):
                return

            # Determine relative path and backup path and make sure backup directory exists
            relative_path = os.path.relpath(src_path, self.watched_dir)
            backup_path = os.path.join(self.backup_dir, relative_path)
            backup_dir = os.path.dirname(backup_path)
            ensure_dir_exists(backup_dir)

            # Create timestamped backup filename
            backup_file_path = os.path.join(backup_dir, get_timestamped_filename(os.path.basename(src_path)))

            # Copy file to backup location
            shutil.copy2(src_path, backup_file_path)
            print(f"Backed up {src_path} to {backup_file_path}")

        except Exception as e:
            print(f"Error backing up {src_path}: {e}")

def main(watched_dir, backup_dir, exclude_patterns=None):
    ensure_dir_exists(watched_dir)
    ensure_dir_exists(backup_dir)

    # Set up the event handler and observer
    event_handler = BackupEventHandler(watched_dir, backup_dir, exclude_patterns)
    observer = Observer()
    observer.schedule(event_handler, watched_dir, recursive=True)
    observer.start()
    print(f"Started watching directory: {watched_dir}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped watching directory")
    observer.join()

if __name__ == "__main__":
    print("Monitoring")
    # Example usage
    watched_directory = "/path/to/watched_directory"
    backup_directory = "/path/to/backup_directory"
    # List of files to exclude by name or regex
    exclude_files = ["exclude_this_file.txt", ".*\.log"]

    main(watched_directory, backup_directory, exclude_files)
