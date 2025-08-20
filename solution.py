def insertion_sort(array: list[int]) -> list[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def find_missing_ranges(frames: list[int]) -> dict:
    if not frames:
        return {"gaps": [], "longest_gap": None, "missing_count": 0}
    
    frames = insertion_sort(frames)
    
    gaps = []
    missing_count = 0
    longest_gap = None
    longest_len = 0
    
    for i in range(len(frames) - 1):
        current = frames[i]
        next_frame = frames[i + 1]
        
        if next_frame - current > 1:
            start = current + 1
            end = next_frame - 1
            gaps.append([start, end])
            
            gap_len = end - start + 1
            missing_count += gap_len
            
            if gap_len > longest_len:
                longest_len = gap_len
                longest_gap = [start, end]
    
    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }


if __name__ == "__main__":
    frames = [1, 2, 3, 5, 6, 10, 11, 16]
    print("Input:", frames)
    print("Output:", find_missing_ranges(frames))
    print()

    frames = [5, 3, 1, 2, 6]
    print("Input:", frames)
    print("Output:", find_missing_ranges(frames))
    print()

    frames = []
    print("Input:", frames)
    print("Output:", find_missing_ranges(frames))