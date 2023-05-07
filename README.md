# File Organizer

File Organizer is a Python application with a PyQt5-based GUI that allows you to organize files in a specified source folder into separate folders based on their file types. It provides a user-friendly interface to select the source folder and automatically move files into corresponding destination folders based on their extensions.

## Features

- Select the source folder containing files to be organized.
- Automatically create separate folders for different file types.
- Move files into respective folders based on their extensions.
- Supported file types for organization include:
  - Music files (mp3, wav, aac)
  - Picture files (jpeg, jpg, png, gif, tiff, bmp, raw)
  - Video files (mp4, mov, wmv, avi, avchd, flv, f4v, swf, mkv, webm)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/file-organizer.git
   ```
   
2. Navigate to the project directory:
   ```
   cd file-organizer
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python file_organizer.py
   ```

2. The File Organizer GUI will appear.

3. Click the "Select Source Folder" button and choose the folder containing the files you want to organize.

4. Click the "Organize Files" button to start the file organization process.

5. The files will be automatically moved into respective folders based on their extensions.

## Customization

- You can customize the destination folders by modifying the `music_folder`, `pictures_folder`, and `videos_folder` variables in the code.
- To customize the GUI, you can modify the layout, stylesheets, and widget properties in the `FileOrganizerApp` class.

## Dependencies

- Python 3.x
- PyQt5



## Contributing

Contributions to the File Organizer project are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## Acknowledgments

This project was created for me to be more fluent with the Python language.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact me.

- GitHub: [your-username](https://github.com/your-username)