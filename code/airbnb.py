# -*- coding: utf-8 -*-

#AirBNB
import pandas as pd 
import numpy as np 
from scipy import stats
import re
from decimal import Decimal 
import math

vancouver = pd.read_csv('listings.csv.gz')
osm = pd.read_csv('weighted_osm.csv')


def currency2float(x):
    return Decimal(re.sub(r'[^\d.]', '', x))

def distance(lat1, lon1, lat2, lon2):
    p = np.pi/180     
    a = 0.5 - np.cos((lat2 - lat1) * p)/2 + np.cos(lat1 * p) * np.cos(lat2 * p) * (1 - np.cos((lon2 - lon1) * p)) / 2
    return 12742 * np.arcsin(np.sqrt(a))

vancouver = vancouver[pd.notnull(vancouver['review_scores_rating'])]

vancouver = vancouver.dropna(axis=1)


vancouver['price'] = vancouver['price'].apply(currency2float)
vancouver['price'] = vancouver['price'].apply(float)


def test(lat, lon, row): #vancouver apply
    count = 0 
    score = 0

    dist = distance(lat, lon, osm['lat'], osm['lon'])
    count = (dist <= 1).sum()
    weights = osm['weight'].copy()
    weights[dist > 1] = 0
    score = weights.sum()
    print(score)
    
    return count, score

vancouver['values'] = vancouver.apply(lambda row: test(row['latitude'], row['longitude'], row), axis=1)
vancouver[['count_amenities', 'weight_score']] = pd.DataFrame(vancouver['values'].tolist(), index=vancouver.index)  

vancouver.to_csv("project.csv")


