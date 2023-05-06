
# # import OS module
# import os
 
# # Get the list of all files and directories
path = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files"
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
 
for files in (path):
    if files.endswith(".png"):
        # Prints only text file present in My Folder
        shutil.move(files, r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer")
