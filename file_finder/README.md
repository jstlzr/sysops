# Interactive CLI File Search Utility

A command-line tool to search for files in a directory with options for filtering by filename pattern and modification date. The results are displayed in an interactive, curses-based UI allowing navigation and directory change.

## Features

- Search for files by filename pattern.
- Filter files by modification date (e.g., today, yesterday, specific date).
- Display results in an interactive UI.
- Change to the directory of the selected file.

## Requirements

- Python 3.x
- curses (usually included in the Python standard library)

## Usage

```python find_file.py -d <directory> -f <filename_pattern> [-t <date_filter>]```

`-d, --directory` Directory to search. If not specified, the current directory is used.

`-f, --filename` Filename pattern to search for (required).

`-t, --date` Date filter for file modification (optional). Supported values are "today", "yesterday", "this week", "last week", and specific dates in "yyyy-mm-dd" format.
