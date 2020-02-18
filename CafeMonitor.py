import argparse
from ExtractData import ExtractData

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()
    ed = ExtractData(args.SheetName, args.Range)
    Last30Days = ed.downloadData()
    