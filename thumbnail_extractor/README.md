# Thumbnail Extractor

## Summary

This script allows users to extract thumbnails from video files. It supports both a command-line interface for extracting thumbnails from single videos or batches of videos and a graphical user interface for interactively selecting thumbnails.

## Requirements

Ensure you have the following libraries installed:

```bash
pip install moviepy opencv-python-headless PyQt5
```

## CLI Usage Instructions

### Options

```
usage: vid2thumb.py [-h] [-v VIDEO] [-t TIMESTAMP] [-o OUTPUT] [-d DIRECTORY]

Extract thumbnails from video files.

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO, --video VIDEO
                        Path to the video file.
  -t TIMESTAMP, --timestamp TIMESTAMP
                        Timestamp in seconds for the thumbnail.
  -o OUTPUT, --output OUTPUT
                        Output path for the thumbnail.
  -d DIRECTORY, --directory DIRECTORY
                        Directory for batch processing.
```

### Extract a Thumbnail from a Single Video (CLI)

To extract a thumbnail from a single video, specify the video file path and optionally provide a timestamp (in seconds). If no timestamp is provided, a random thumbnail will be extracted.

```bash
python3 vid2tumb.py -v /path/to/video.mp4 -o /path/to/output_thumbnail.jpg #generate a random thumbnail

python3 vid2tumb.py -v /path/to/video.mp4 -o /path/to/output_thumbnail.jpg -t 37.5 #generate a thumbnail at 37.5 seconds
```

- `-v /path/to/video.mp4` Specifies the path to the video file.
- `-o /path/to/output_thumbnail.jpg` (Optional) Specifies the output path for the thumbnail. If omitted, the default is thumbnail.jpg in the current directory.
- `-t 37.5` (Optional) Specifies the timestamp in seconds to extract the thumbnail. If omitted, a random timestamp is used.

### Batch Extract Thumbnails from All Videos in a Directory (CLI)

To extract thumbnails from all video files in a directory, specify the directory path and optionally provide a timestamp. If no timestamp is provided, random thumbnails will be extracted for each video.

```bash
python3 vid2tumb.py -d /path/to/directory -t 37.5
```

- `-d /path/to/directory` Specifies the path to the directory containing video files.
- `-t 15.0` (Optional) Specifies the timestamp in seconds to extract the thumbnails. If omitted, a random timestamp is used for each video.

### Exmples

1) Extract a random thumbnail from a single video:

```bash
python3 vid2tumb.py -v /path/to/video.mp4
```

2) Extract a specific thumbnail from a single video at 10.5 seconds:

```bash
python3 vid2tumb.py -v /path/to/video.mp4 -t 10.5
```

3) Batch extract thumbnails from all videos in a directory:

```bash
python3 vid2thumb.py -d /path/to/directory
```

4) Batch extract thumbnails from all videos in a directory at 15.0 seconds:

```bash
python3 vid2thumb.py -d /path/to/directory -t 15.0
```

## GUI Usage Instructions

To use the GUI, simply run the script without any command-line arguments:

```bash
python3 vid2thumb.py
```

1) Click the "Open Video" button to select and load a video file.

2) Use the slider to scrub through the video. The displayed frame will update according to the slider's position.

3) Click the "Save Thumbnail" button to save the currently displayed frame as a thumbnail. You will be prompted to choose the save location and file name.
