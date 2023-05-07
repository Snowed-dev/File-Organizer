import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog

class FileOrganizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.setStyleSheet("background-color: white;")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        # Create a QHBoxLayout for label positioning
        label_layout = QHBoxLayout()

        # Add stretchable space before the label
        label_layout.addStretch()

        self.label = QLabel("Select Source Folder")
        label_layout.addWidget(self.label)

        # Add stretchable space after the label
        label_layout.addStretch()

        self.button = QPushButton("Organize Files")
        self.button.setStyleSheet("QPushButton {background-color: black; color: white; border-radius: 10px; padding: 10px;}")
        self.button.clicked.connect(self.organize_files)

        # Add stretchable space above the label layout
        self.layout.addStretch()

        # Add the label layout to the main layout
        self.layout.addLayout(label_layout)

        self.layout.addWidget(self.button)

        # Add stretchable space below the button
        self.layout.addStretch()

        self.resize(400, 200)

    def organize_files(self):
        source_folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if source_folder:
            target_folder = os.path.join(source_folder, "Organized Files")
            os.makedirs(target_folder, exist_ok=True)
            music_folder = os.path.join(target_folder, "Music")
            pictures_folder = os.path.join(target_folder, "Pictures")
            videos_folder = os.path.join(target_folder, "Videos")
            os.makedirs(music_folder, exist_ok=True)
            os.makedirs(pictures_folder, exist_ok=True)
            os.makedirs(videos_folder, exist_ok=True)

            # Loop through files in the source folder and organize them into folders: Music, Pictures, and Videos
            for path, dir, files in os.walk(source_folder):
                if files:
                    for file in files:
                        if file.endswith((".mp3", ".wav", ".aac")):
                            if not os.path.isfile(os.path.join(music_folder, file)):
                                os.rename(os.path.join(path, file), os.path.join(music_folder, file))
                        elif file.endswith((".jpeg", ".jpg", ".png", ".gif", ".tiff", ".bmp", ".raw")):
                            if not os.path.isfile(os.path.join(pictures_folder, file)):
                                os.rename(os.path.join(path, file), os.path.join(pictures_folder, file))
                        elif file.endswith((".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf", ".mkv", ".webm")):
                            if not os.path.isfile(os.path.join(videos_folder, file)):
                                os.rename(os.path.join(path, file), os.path.join(videos_folder, file))

            self.label.setText("Files organized successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())
