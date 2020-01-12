import numpy as np
import pandas as pd

def add_weight(row):
    weight = pd.read_csv("weights.csv")
    weight = dict(sorted(weight.values.tolist()))
    return weight.get(row, 0)

def isinvancouver(lat1, lon1):
    return (-123.22496118 < lon1 < -123.02324196) & (49.19844515 < lat1 < 49.31617132)

def main():
    df = pd.read_json("amenities-vancouver.json.gz", lines=True).dropna()
    df['weight'] = df['amenity'].apply(add_weight)
    df['vancouver'] = df.apply(lambda row: isinvancouver(row['lat'], row['lon']), axis=1)
    df = df[df['vancouver'] != False]
    df.to_csv("weighted_osm.csv")

if __name__ == '__main__':
    main()
    
