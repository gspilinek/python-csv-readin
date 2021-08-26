# run with "py csv-readin.py <csv file name> <num of records> <num of fields>"
# if there is an initial line in the csv to indicate the fields add 1 to num of records

# written by Gerald Spilinek
# code snippet to reuse that allows csv files to be read in

import sys


def main():
    num_of_records = int(sys.argv[2])
    num_of_fields = int(sys.argv[3])

    record = [[""] * num_of_fields for x in range(num_of_records)]

    with open(str(sys.argv[1]), 'r') as f:

        for x in range(0, num_of_records):
            line = f.readline()
            length = len(line)
            start = 0
            end = 0
            y = 0
            for spot in line:
                if spot == "," or spot == "\n":
                    #print("x: " + str(x) + "\t" + "y: "+str(y))
                    record[x][y] = line[start:end]
                    start = end+1
                    y += 1
                    end = start
                else:
                    end += 1

                if y == num_of_fields:
                    break


    for x in record:
        print(x)


if __name__ == '__main__':
    main()
