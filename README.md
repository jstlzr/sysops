# sysops
Utilities and automation scripts for system administration

[empty_file_generator](empty_file_generator) - `nfile.py` creates multiple empty files in a given directory. It allows you to customize the file extension, number of files, and directory. It can create files with randomized extensions from a list of common file types.

[file_finder](file_finder) - `find_file.py` is an __interactive__ command-line tool to search for files in a directory with options for filtering by filename pattern and modification date. The results are displayed in an interactive, curses-based UI allowing navigation and directory change to the selected found file.

[log_tar](log_tar) - `tarlog.py` creates a tarball of all .log files in a specified directory and saves it to a specified output directory. It can optionally delete the original files after creating the archive. Files are prepended with a timestamp.

[recursive_backup](recursive_backup) - `bu_dir_recursive.py` watches a directory recursively for changes and backs them up with timestamped filenames.

[thumbnail_extractor](thumbnail_extractor) - `vid2thumb.py` This script allows you to extract thumbnails from video files. It supports both a command-line interface for extracting thumbnails from single videos or batches of videos and a graphical user interface for interactively selecting thumbnails.


