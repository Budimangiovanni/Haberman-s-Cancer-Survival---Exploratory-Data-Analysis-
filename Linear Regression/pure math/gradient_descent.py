from numpy import *
import pandas as pd

def run():
    print "run"
    points = pd.read_csv("ADRvsRating.csv")
    print points

if __name__ == '__main__':
    run()