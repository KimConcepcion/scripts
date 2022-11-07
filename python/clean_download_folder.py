from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

# folders to track
downloads_dir      = "C://Users//Kim//Downloads"
dest_dir_audio     = "D://Music"
dest_dir_video     = "D://Videoer"
dest_dir_image     = "D://Billeder"
dest_dir_document  = "D://Dokumenter"

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry.path, dest)

def check_audio_files(entry, name):  # * Checks all Audio Files
    moved_cnt = 0
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            move_file(dest_dir_music, entry, name)
            logging.debug(f"Moved audio file: {name}")
            moved_cnt += 1
    return moved_cnt

def check_video_files(entry, name):  # * Checks all Video Files
    moved_cnt = 0
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(dest_dir_video, entry, name)
            logging.debug(f"Moved video file: {name}")
            moved_cnt += 1
    return moved_cnt

def check_image_files(entry, name):  # * Checks all Image Files
    moved_cnt = 0
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(dest_dir_image, entry, name)
            logging.debug(f"Moved image file: {name}")
            moved_cnt += 1
    return moved_cnt

def check_document_files(entry, name):  # * Checks all Document Files
    moved_cnt = 0
    for documents_extension in document_extensions:
        if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
            move_file(dest_dir_documents, entry, name)
            logging.debug(f"Moved document file: {name}")
            moved_cnt += 1
    return moved_cnt

def clean_downloads_folder():
    logging.info(f"Cleaning of: {downloads_dir} STARTED!")
    
    # count files moved
    audio_cnt    = 0
    video_cnt    = 0
    image_cnt    = 0
    document_cnt = 0
    
    with scandir(downloads_dir) as entries:
        for entry in entries:
            name = entry.name
            audio_cnt    += check_audio_files(entry, name)
            video_cnt    += check_video_files(entry, name)
            image_cnt    += check_image_files(entry, name)
            document_cnt += check_document_files(entry, name)
    
    total_cnt = audio_cnt + video_cnt + image_cnt + document_cnt
    logging.info(f"Files moved to [{dest_dir_audio}]: {audio_cnt}")
    logging.info(f"Files moved to [{dest_dir_video}]: {video_cnt}")
    logging.info(f"Files moved to [{dest_dir_image}]: {image_cnt}")
    logging.info(f"Files moved to [{dest_dir_document}]: {document_cnt}")
    logging.info(f"Total files moved: {total_cnt}")

# Main
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Clean downloads folder
    clean_downloads_folder()
    