import mne
import csv
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: reader.py [filename]")
    else:
        file = sys.argv[1]
        name = file.split('.')[0]
        print(f"Name: {name}")
        print(file)
        data = mne.io.read_raw_bdf(sys.argv[1])
        channels = data.info['ch_names']
        print(channels)
        outfile = name + '.csv'
        with open(outfile, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Time'] + channels)
            values, time = data.get_data(return_times=True)
            print(values.shape)
            for n in range(len(time)):
                csvwriter.writerow([time[n]] + list(values[:,n]))

        

if __name__ == "__main__":
    main()