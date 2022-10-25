import os
import sys
import time

# Get current working dir & amount of files in dir
def organizer(folder_name):
    CWD = os.getcwd()
    FOLDER = CWD + '\\' + folder_name
    FILES = os.listdir(FOLDER)
    print('@CWD: [%s]' % FOLDER)
    print('@Files to be organized: %d' % len(FILES))

    # Print old file names in dir
    print('--------- OLD FILES ---------')
    for idx, file_name in enumerate(FILES):
        print("%d File: %s" %(idx, file_name))

        old_name = FOLDER + '\\' + file_name

        # Get Last modification of file:
        epochs = os.path.getmtime(old_name)
        last_modification = time.strftime('%Y%m%d', time.localtime(epochs))
        new_name = FOLDER + '\\' + last_modification + '_' + 'Image_' + str(idx)

        # Make sure path is a file and not directory:
        if os.path.isfile(old_name) is True:
            # Get file extension
            extension = ''
            file_name = file_name.split('.')
            if len(file_name) > 1:
                extension = file_name[1]
                new_name = FOLDER + '\\' + last_modification + '_' + 'Image_' + str(idx) + '.' + extension

            # Rename
            os.rename(old_name, new_name)

    # Print new file names in dir
    FILES = os.listdir(FOLDER)
    print('--------- NEW FILES ---------')
    for idx, file_name in enumerate(FILES):
        print("%d File: %s" %(idx, file_name))

# --------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------- #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please specify folder name...')
    else:
        folder_name = sys.argv[1]
        organizer(folder_name)
