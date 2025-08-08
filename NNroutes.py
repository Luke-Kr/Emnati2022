import os
import sys
import csv
import argparse
import pandas as pd
import numpy as np

"""
Script: NNroutes.py

This script generates a routes.csv file where each location is connected to its k nearest neighbors
based on Euclidean distance. The input locations.csv must include columns:
  - name
  - latitude
  - longitude

Usage:
    python NNroutes.py <country_dir> [--k K]

Arguments:
    country_dir   Name of the directory containing locations.csv
    --k           Number of nearest neighbors per location (default: 3)

Output:
    routes.csv in the specified country_dir with columns:
    name1, name2, distance, force_redirection
"""

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the Euclidean distance between two geographic coordinates (in km), then convert to meters.
    """
    return np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2) * 1000


def extract_routes_csv(country_dir, k):
    # Build file paths
    current_dir = os.getcwd()
    locations_file = os.path.join(current_dir, country_dir, "locations.csv")

    # Load locations
    try:
        df = pd.read_csv(locations_file)
    except FileNotFoundError:
        print(f"Error: '{locations_file}' not found.")
        sys.exit(1)

    # Validate necessary columns
    for col in ['name', 'latitude', 'longitude']:
        if col not in df.columns:
            print(f"Error: Column '{col}' not found in locations.csv.")
            sys.exit(1)

    # Keep camps separate from other locations


    # camps = df[df['location_type'] == 'camp']
    # df = df[df['location_type'] != 'camp']

    routes = []
    n = len(df)

    # Compute k nearest neighbors for each location
    for i in range(n):
        lat_i, lon_i = df.iloc[i]['latitude'], df.iloc[i]['longitude']
        distances = []
        for j in range(n):
            if i == j:
                continue
            lat_j, lon_j = df.iloc[j]['latitude'], df.iloc[j]['longitude']
            dist = calculate_distance(lat_i, lon_i, lat_j, lon_j)
            distances.append((j, dist))

        # Sort by distance and select top-k
        distances.sort(key=lambda x: x[1])
        for idx, dist in distances[:k]:
            routes.append([
                df.iloc[i]['name'],
                df.iloc[idx]['name'],
                round(dist, 2),
                0  # force_redirection placeholder
            ])

    # Write output CSV
    output_file = os.path.join(current_dir, country_dir, "routes.csv")
    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name1', 'name2', 'distance', 'force_redirection'])
        writer.writerows(routes)

    print(f"Created '{output_file}' with {k} nearest neighbors per location.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate routes.csv connecting each location to its k nearest neighbors'
    )
    parser.add_argument('country_dir', help='Directory containing locations.csv')
    parser.add_argument('--k', type=int, default=3,
                        help='Number of nearest neighbors per location (default: 3)')
    args = parser.parse_args()

    extract_routes_csv(args.country_dir, args.k)
