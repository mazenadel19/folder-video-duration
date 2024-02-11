# Video Duration Analyzer

## Overview
The Video Duration Analyzer is a Python script designed to calculate the total duration of videos within a specified folder and its subdirectories. It generates a report detailing the total duration of videos in each subdirectory, as well as the overall duration of videos in the main folder.

## Features
- Calculates the total duration of videos (.mp4, .avi, .mkv, .mov) within a specified folder and its subdirectories.
- Generates a report in a human-readable format, including the total duration of videos in each subdirectory and the overall duration of videos in the main folder.
- Provides progress bars for tracking the processing of directories and files, along with an estimate of the time remaining.

## Prerequisites
- [Python  3.x](https://www.python.org/downloads/) installed
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to the system PATH

## Installation
1. Clone this repository or download the script directly.
2. Install the required Python packages:
   ```
   pip install tqdm
   ```
3. Install FFmpeg from the official website and add it to your system PATH.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script by executing the following command:
   ```
   python video_duration_analyzer.py
   ```
4. Follow the prompts to enter the path to the folder containing your videos.
5. Once the script completes, it will generate a report file named `video_duration_report.txt` in the specified folder.

## Example
```
Enter the path to the folder containing videos: /path/to/your/videos
Report generated successfully in /path/to/your/videos.
```

## License
This project is licensed under the MIT License
---