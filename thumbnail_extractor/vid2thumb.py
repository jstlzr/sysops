import sys
import os
import random
from moviepy.editor import VideoFileClip
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSlider, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap

# CLI functionality
def extract_thumbnail(video_path, timestamp=None, output_path="thumbnail.jpg"):
    """Extracts a thumbnail from a video at a given timestamp or randomly."""
    clip = VideoFileClip(video_path)
    duration = clip.duration

    if timestamp is None:
        timestamp = random.uniform(0, duration)

    frame = clip.get_frame(timestamp)
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, frame_bgr)
    print(f"Thumbnail saved to {output_path} at {timestamp:.2f} seconds.")

def batch_extract_thumbnails(directory, timestamp=None):
    """Batch extracts thumbnails from all video files in a directory."""
    for filename in os.listdir(directory):
        if filename.endswith((".mp4", ".avi", ".mov")):
            video_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"thumbnail_{filename}.jpg")
            extract_thumbnail(video_path, timestamp, output_path)

# GUI functionality
class ThumbnailExtractorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Thumbnail Extractor')
        self.setGeometry(100, 100, 800, 600)

        self.video_path = None
        self.clip = None

        self.layout = QVBoxLayout()

        self.open_button = QPushButton('Open Video')
        self.open_button.clicked.connect(self.open_video)
        self.layout.addWidget(self.open_button)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 1000)
        self.slider.setTickInterval(10)
        self.slider.setEnabled(False)
        self.slider.valueChanged.connect(self.update_frame)
        self.layout.addWidget(self.slider)

        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.save_button = QPushButton('Save Thumbnail')
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_thumbnail)
        self.layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def open_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.video_path, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Videos (*.mp4 *.avi *.mov);;All Files (*)", options=options)
        if self.video_path:
            self.clip = VideoFileClip(self.video_path)
            self.slider.setEnabled(True)
            self.save_button.setEnabled(True)
            self.update_frame(0)

    def update_frame(self, value):
        if self.clip:
            timestamp = (value / 1000) * self.clip.duration
            frame = self.clip.get_frame(timestamp)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)

    def save_thumbnail(self):
        if self.clip:
            value = self.slider.value()
            timestamp = (value / 1000) * self.clip.duration
            frame = self.clip.get_frame(timestamp)
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Thumbnail", "", "JPEG (*.jpg);;PNG (*.png);;All Files (*)")
            if output_path:
                # Ensure the output path has an image file extension
                if not (output_path.endswith('.jpg') or output_path.endswith('.png')):
                    output_path += '.jpg'  # Default to .jpg if no valid extension is provided
                cv2.imwrite(output_path, frame_bgr)
                print(f"Thumbnail saved to {output_path} at {timestamp:.2f} seconds.")

# CLI entry point
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract thumbnails from video files.")
    parser.add_argument("-v", "--video", type=str, help="Path to the video file.")
    parser.add_argument("-t", "--timestamp", type=float, help="Timestamp in seconds for the thumbnail.")
    parser.add_argument("-o", "--output", type=str, help="Output path for the thumbnail.", default="thumbnail.jpg")
    parser.add_argument("-d", "--directory", type=str, help="Directory for batch processing.")

    args = parser.parse_args()

    if args.directory:
        batch_extract_thumbnails(args.directory, args.timestamp)
    elif args.video:
        extract_thumbnail(args.video, args.timestamp, args.output)
    else:
        app = QApplication(sys.argv)
        ex = ThumbnailExtractorGUI()
        ex.show()
        sys.exit(app.exec_())
