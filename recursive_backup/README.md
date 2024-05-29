# Recursive Directory Backup

This script watches a directory recursively for changes and backs them up with timestamped filenames.

## Requires

* watchdog


```
pip install -r requirements.txt
```

## To use

Replace `/path/to/watched_directory` and `/path/to/backup_directory` with the actual paths. Customize the `exclude_files` list with filenames or regex patterns to exclude specific files.
