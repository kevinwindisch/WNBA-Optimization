import numpy as np
import pandas as pd
import json
from geopy.distance import great_circle

# NBA teams and their respective cities with latitude and longitude
teams = {
    "Atlanta Dream": (33.6468, -84.459616),
    "Chicago Sky": (41.853611, -87.621389),
    "Connecticut Sun": (41.491111, -72.089722),
    "Indiana Fever": (39.763889, -86.155556),
    "New York Liberty": (40.682661, -73.975225),
    "Washington Mystics": (38.846972, -76.991444),
    "Dallas Wings": (32.730586, -97.107972),
    # "Golden State Valkyries": (37.768056, -122.3875),
    "Las Vegas Aces": (36.090678, -115.178981),
    "Los Angeles Sparks": (34.043056, -118.267222),
    "Minnesota Lynx": (44.979444, -93.276111),
    "Phoenix Mercury": (33.445833, -112.071389),
    "Seattle Storm": (47.622, -122.354)
}

# Create an empty distance matrix
team_list = list(teams.keys())
# print(json.dumps(team_list))
distance_matrix = np.zeros((12, 12))
distance_matrix = pd.DataFrame(distance_matrix, columns=team_list, index=team_list)


# Calculate distances between all pairs of teams
for i in range(12):
    for j in range(12):
        if i != j:
            loc_1 = teams[team_list[i]]
            loc_2 = teams[team_list[j]]
            team_1 = team_list[i]
            team_2 = team_list[j]
            # Use great-circle distance (Haversine formula) from geopy
            distance_matrix.loc[team_1, team_2] = great_circle(loc_1, loc_2).miles

# Display the distance matrix
distance_matrix.to_csv('wnba_distances.csv', index=True)