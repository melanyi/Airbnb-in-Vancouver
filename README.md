# Airbnb-in-Vancouver

Libraries Required:

Numpy
Pandas
Scipy
Matplotlib
Seaborn
Statsmodels
Gmaps


How to run our project:

Run "python3 osm.py":
This returns "weighted_osm.csv", which is comprised of osm amenities in vancouver, and a weighted score to each amenity


Run "python3 airbnb.py"
This returns "project.csv" which includes the number of amenities nearby, and the total score of those amenities


Running "python3 stats.py" will give the following:

Scatterplot - "pricevsamenity.png" (Price Vs Number of Amenities)
Scatterplot - "ratevsamenity.png" (Review Rating Vs Number of Amenities)
OLS Summary - Text in Terminal (Price Vs [Number of Amenities, Number of people the Airbnb accommodates])


Run heatmap.ipynb in Jupyter Notebook
This will display the heatmaps in separate cells
Note: This uses a google maps api key, and it is possible that it may no longer work.

Sources:
Data
Airbnb: http://insideairbnb.com/get-the-data.html
