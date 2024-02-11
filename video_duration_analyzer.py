import os
import subprocess
from tqdm import tqdm

def get_video_duration(file_path):
    try:
        result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        duration = float(result.stdout)
        return duration
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return 0

def format_time(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def aggregate_folder_video_duration(folder_path):
    total_duration = 0
    subdirectories = []
    _, dirs, _ = next(os.walk(folder_path))  # Get immediate subdirectories
    if dirs:  # If there are subdirectories
        for dir in tqdm(dirs, desc="Processing directories", unit="directory"):
            dir_path = os.path.join(folder_path, dir)
            sub_duration = aggregate_subfolder_video_duration(dir_path)
            total_duration += sub_duration
            subdirectories.append((dir, sub_duration))
    else:  # If there are no subdirectories
        total_duration = aggregate_subfolder_video_duration(folder_path)
    return total_duration, subdirectories

def aggregate_subfolder_video_duration(folder_path):
    total_duration = 0
    for root, _, files in os.walk(folder_path):
        for file in tqdm(files, desc="Processing files", unit="file"):
            if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
                file_path = os.path.join(root, file)
                duration = get_video_duration(file_path)
                total_duration += duration
    return total_duration

def create_report(folder_path, total_duration, subdirectories):
    report_file = os.path.join(folder_path, "video_duration_report.txt")
    with open(report_file, "w") as f:
        f.write(f"Total duration of videos in {folder_path}: {format_time(total_duration)}\n\n")
        if subdirectories:
            f.write("Subdirectories:\n")
            for dir, duration in subdirectories:
                f.write(f"- {dir}: {format_time(duration)}\n")
    print(f"Report generated successfully in {folder_path}.")

def main():
    folder_path = input("Enter the path to the folder containing videos: ")
    total_duration, subdirectories = aggregate_folder_video_duration(folder_path)
    create_report(folder_path, total_duration, subdirectories)

if __name__ == "__main__":
    main()
