
# # import OS module
# import os
 
# # Get the list of all files and directories
source_folder = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files" + '\\'
target_folder = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Music" + '\\'
# dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# # prints all files
# print(dir_list)



# import OS
import os
import shutil
# os.mkdir(r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Pictures", mode = 0o777,  dir_fd = None)
# os.mkdir(r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Videos", mode = 0o777,  dir_fd = None)
# os.mkdir(r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Music", mode = 0o777,  dir_fd = None)
 
# os.walk(path, topdown=True, onerror=None, followlinks=False)
        # shutil.move(files, r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer")
for path, dir, files in os.walk(source_folder):
    if files:
        for file in files:
            if file.endswith(".wav"):
                if not os.path.isfile(target_folder + file):
                    os.rename(path + '\\' + file, target_folder + file)