import mne
import os
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: reader.py [filename]")
    else:
        file = sys.argv[1]
        print(file)
        data = mne.io.read_raw_bdf(sys.argv[1])
        for d in data.info:
            print(f"{d}: {data.info[d]}")
        print(f"number of electrodes: {len(data.info.ch_names)}")

if __name__ == "__main__":
    main()