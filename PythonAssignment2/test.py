# Site used for learning pandas: https://www.w3schools.com/python/pandas/default.asp
# Site used for learning matplotlib.pyplot: https://www.w3schools.com/python/matplotlib_intro.asp

import pandas as pd
import matplotlib.pyplot as plt

# Read data from the file
data = pd.read_csv("GrowLocations.csv") # Creates data frame from the input file

# Remove any rows with null values
data = data.dropna() # Creates new data frame with any rows with null values removed

# Swap headings of latitude and longitude columns, through a bit of testing I noticed they were the wrong way round
data = data.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})

# Defining the bounding box
longitudeMax = 1.6848
longitudeMin = -10.592
latitudeMax = 57.985
latitudeMin = 50.681

# Filter the values and create a data frame that only keeps the rows whose values are within the bounding box
filteredData = data[(data['Latitude'] >= latitudeMin) & (data['Latitude'] <= latitudeMax) & (data['Longitude'] >= longitudeMin) & (data['Longitude'] <= longitudeMax)]

# Load the map image
map = plt.imread("map7.png")

# Plot points on the map
plt.figure(figsize=(8, 8)) # Creates a new figure and sets its size
plt.imshow(map, extent=[longitudeMin, longitudeMax, latitudeMin, latitudeMax]) # Specifies the boundaries of the image to be the same as the bounding box limits given
plt.scatter(filteredData['Longitude'], filteredData['Latitude'], c='blue', s=10) # Creates a scatter plot of all the points contained in the data frame
plt.show() # Displays the map