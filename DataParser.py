import csv

def parseData(file_to_open):
    points = {}
    with open(file_to_open) as f:
        for name, x, y in csv.reader(f, delimiter=" "):
            points[name] = (x,y)
    return points

if __name__ == '__main__':
    parseData("data/pb005.txt")
