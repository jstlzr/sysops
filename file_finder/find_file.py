import argparse
import os
import glob
import curses
import datetime
import time


def parse_args():
    """
    Parse command-line arguments.
    -d, --directory: Directory to search.
    -f, --filename: Filename pattern to search for. (Required)
    -t, --date: Date filter for file modification (e.g., "today", "yesterday", "yyyy-mm-dd").
    """
    parser = argparse.ArgumentParser(description='Search for files in a directory.')
    parser.add_argument('-d', '--directory', help='Directory to search')
    parser.add_argument('-f', '--filename', required=True, help='Filename pattern to search for')
    parser.add_argument('-t', '--date', help='Date filter for file modification (e.g., "today", "yesterday", "yyyy-mm-dd")')
    return parser.parse_args()


def parse_date(date_str):
    """
    Convert a date string into a datetime.date object.
    Supports specific dates and relative dates like "today", "yesterday", "this week", "last week".
    """
    today = datetime.date.today()
    if date_str == 'today':
        return today
    elif date_str == 'yesterday':
        return today - datetime.timedelta(days=1)
    elif date_str == 'this week':
        start = today - datetime.timedelta(days=today.weekday())
        return start
    elif date_str == 'last week':
        start = today - datetime.timedelta(days=today.weekday() + 7)
        return start
    elif 'week' in date_str:
        weeks_ago = int(date_str.split()[0])
        start = today - datetime.timedelta(days=today.weekday() + 7 * weeks_ago)
        return start
    else:
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Expected format: yyyy-mm-dd")


def search_files(directory, filename_pattern, date_filter=None):
    """
    Search for files matching the filename pattern in the specified directory.
    If a date filter is provided, filter files modified on or after that date.
    """
    if directory:
        search_path = os.path.join(directory, '**', filename_pattern)
    else:
        print("Searching current directory. To search a different directory, use the -d argument.")
        search_path = os.path.join(os.getcwd(), '**', filename_pattern)

    # Use glob to find files matching the pattern recursively
    files = glob.glob(search_path, recursive=True)
    results = []

    # If a date filter is provided, filter the files by their modification date
    if date_filter:
        date_threshold = time.mktime(date_filter.timetuple())
        files = [f for f in files if os.path.getmtime(f) >= date_threshold]

    for f in files:
        try:
            stats = os.stat(f)
            size = stats.st_size
            mtime = datetime.datetime.fromtimestamp(stats.st_mtime)
            results.append((f, mtime, size))
        except FileNotFoundError as e:
            print(f"Error: {e} - File not found: {f}")

    return results


def display_results(stdscr, results):
    """
    Display the search results in a curses-based UI, allowing the user to navigate with arrow keys
    and change directory upon selecting an entry.
    """
    curses.curs_set(0)  # Hide the cursor
    current_row = 0

    def print_menu(stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(results):
            x = 0
            y = idx
            filename, mtime, size = row
            line = f"{filename} - {mtime.strftime('%Y-%m-%d %H:%M:%S')} - {size} bytes"
            if len(line) > w:
                line = line[:w-1]  # Truncate the line if it's too long
            try:
                if idx == selected_row_idx:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, line)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, line)
            except curses.error as e:
                # Print the error and line for debugging
                stdscr.addstr(0, 0, f"Error: {str(e)}")
                stdscr.addstr(1, 0, f"Line: {line}")
        stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(results) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return results[current_row][0]  # Return the selected file path
        print_menu(stdscr, current_row)


def main():
    """
    Main function to parse arguments, search for files, and display results for navigation.
    """
    args = parse_args()  # Parse command-line arguments
    directory = args.directory
    filename = args.filename
    date_filter = None

    # Parse the date filter if provided
    if args.date:
        try:
            date_filter = parse_date(args.date)
        except argparse.ArgumentTypeError as e:
            print(e)
            return

    # Search for files matching the filename pattern and date filter
    results = search_files(directory, filename, date_filter)
    if not results:
        print("No files found.")
        return

    # Display the results in a curses-based UI for navigation
    selected_file = curses.wrapper(display_results, results)

    # Change the directory to the parent directory of the selected file
    if selected_file:
        parent_directory = os.path.dirname(selected_file)
        os.chdir(parent_directory)
        print(f"Changed directory to {parent_directory}")

        # Start a new shell in the new directory
        os.system('bash')  # This can be 'sh', 'bash', 'zsh', etc., depending on the user's shell preference


if __name__ == "__main__":
    main()
