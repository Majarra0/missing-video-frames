# missing-video-frames
Detecting Missing Video Frames
Overview

This project provides a Python function to detect missing video frames from an unordered list of frame numbers. It is designed for smart surveillance platforms or any system that processes video streams where frames may be dropped due to network or hardware issues.

The function:

Detects missing frame ranges.

Identifies the longest missing range.

Counts the total number of missing frames.

This implementation does not use Python built-in sorting functions and instead includes a custom Insertion Sort to order frames.

Features

Works with unordered lists of positive frame numbers starting from 1.

Returns missing ranges in a clear [start, end] format.

Identifies the longest gap and total missing frames.

Simple, easy-to-understand code suitable for hackathons or educational purposes.

Usage

Clone or download the repository.

Run the Python file:

python missing_frames.py


Example:

from missing_frames import find_missing_ranges

frames = [1, 2, 3, 5, 6, 10, 11, 16]
result = find_missing_ranges(frames)
print(result)


Output:

{
  'gaps': [[4, 4], [7, 9], [12, 15]],
  'longest_gap': [12, 15],
  'missing_count': 8
}

Functions
find_missing_ranges(frames: list[int]) -> dict

Input:
frames — a list of integers representing received frame numbers.

Output:
Dictionary with keys:

"gaps": List of [start, end] missing ranges.

"longest_gap": The missing range with the most frames.

"missing_count": Total number of missing frames.

insertion_sort(arr: list[int]) -> list[int]

Sorts a list of integers in ascending order using Insertion Sort.

Used internally by find_missing_ranges.

Example Usage
frames = [5, 3, 1, 2, 6]
print(find_missing_ranges(frames))
# Output: {'gaps': [], 'longest_gap': None, 'missing_count': 0}

frames = [1, 50]
print(find_missing_ranges(frames))
# Output: {'gaps': [[2, 49]], 'longest_gap': [2, 49], 'missing_count': 48}

Requirements

Python 3.x

No third-party libraries required.
