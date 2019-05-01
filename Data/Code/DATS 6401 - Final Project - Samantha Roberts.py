# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:08:38 2019

@author: samro
"""

# Import packages
import csv
import json
import pandas as pd


# Read in the data
data = pd.read_csv('active-satellites.csv', header=0)

# Check Basics
print(data.head(5))
print(data.columns)

# Check for NaN's
print(data.isna().sum())

# Drop columns and then rows with NaN's
data.drop(['Detailed_Purpose', 'Type_of_Orbit', 'Launch_Mass_Kilograms', 'Dry_Mass_Kilograms', 'Power_Watts', 'Expected_Lifetime_Years'], axis=1, inplace=True)
data.dropna(inplace=True)

print(data.shape) # 1398 x 20

# Convert to JSON output text file
data.to_json('satellites.json', orient='records')

