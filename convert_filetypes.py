"""Convert one filetype to another using ffmpeg. Rename the corresponding json.
"""
import os
import sys
from tqdm import tqdm

FILETYPES_IMAGE = ["jpg", "jpeg", "png"]
FILETYPES_VIDEO = ["3gp", "asf", "avi", "m4v", "mov", "mp4", "mpg", "wmv"]


def convert_pic_command(filename, source_filetype, target_filetype):
    """Convert picture format to jpg or rename."""
    if source_filetype.lower() == target_filetype.lower():
        command_list = [
            "mv",
            f'"{filename}.{source_filetype}"',
            f'"{filename}.{target_filetype}"',
        ]
    else:
        command_list = [
            "ffmpeg",
            "-i", f'"{filename}.{source_filetype}"',
            "-q:v 1",
            "-pix_fmt yuvj420p",
            "-y",
            f'"{filename}.{target_filetype}"',
        ]
    return " ".join(command_list)


def convert_vid_command(filename, source_filetype, target_filetype):
    """Convert video format to mp4 or rename."""
    if source_filetype.lower() == target_filetype.lower():
        command_list = [
            "mv",
            f'"{filename}.{source_filetype}"',
            f'"{filename}.{target_filetype}"',
        ]
    else:
        command_list = [
            "ffmpeg",
            "-i", f'"{filename}.{source_filetype}"',
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-c:a", "aac",
            "-strict", "experimental",
            "-b:a", "192k",
            "-y",
            f'"{filename}.{target_filetype}"',
        ]
    return " ".join(command_list)


def convert_file(filepath, source_filetype, target_filetype):
    """Convert file from one filetype to another."""
    filename, _ = os.path.splitext(filepath)

    if source_filetype.lower() in FILETYPES_IMAGE:
        command = convert_pic_command(filename, source_filetype, target_filetype)
    if source_filetype.lower() in FILETYPES_VIDEO:
        command = convert_vid_command(filename, source_filetype, target_filetype)

    # Convert file.
    status = os.system(command)
    if status == 0:
        # Rename json. Truncate long filenames to match naming.
        json_filename = os.path.join(os.path.dirname(
            filepath), f"{os.path.basename(filepath)[0:46]}.json")
        if os.path.exists(json_filename):
            os.rename(json_filename, f"{filename}.{target_filetype}.json")

        # Delete original file.
        if target_filetype.lower() != source_filetype.lower():
            os.remove(filepath)


if __name__ == "__main__":
    path = sys.argv[1]
    source_filetype = sys.argv[2]
    target_filetype = sys.argv[3]
    for root, dirs, files in os.walk(path):
        print(f"Processing {root}")
        for file in tqdm(files):
            if file.endswith(f".{source_filetype}"):
                filepath = os.path.join(root, file)
                convert_file(filepath, source_filetype, target_filetype)
