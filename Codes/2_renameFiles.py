import os

def rename_files():
    # get filenames from a folder
    file_list = os.listdir(r'C:\Users\Suvro\OneDrive\Suvro Banerjee_Personal\Profession\Udacity\Nanodegree\Full Stack Web Developer Nanodegree\Lesson -5\prank\prank')  # raw path
    print(file_list)  # the output is a list

    saved_path = os.getcwd()  # get the current working directory... where this code exists, renameFiles.py
    print('Previous working directory is ', saved_path)

    os.chdir(r'C:\Users\Suvro\OneDrive\Suvro Banerjee_Personal\Profession\Udacity\Nanodegree\Full Stack Web Developer Nanodegree\Lesson -5\prank\prank')  # it changes the directory where the files are.
    print('Current working directory is ', os.getcwd())

    # to rename files
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate({ord(c): None for c in '0123456789'}))
        os.rename(file_name, file_name.translate({ord(c): None for c in '0123456789'})) # translate will remove the numbers to None. It's Python 2.x syntax is different

    os.chdir(saved_path) # reseting the working directory

rename_files()
