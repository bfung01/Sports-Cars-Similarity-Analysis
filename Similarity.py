import pandas as pd
import scipy.spatial.distance

# Clean and Format Data
df = pd.read_csv('Sport car price.csv')
df = df.drop_duplicates(subset=['Car Make', 'Car Model', 'Year'], keep='first')
columns = ['Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)']

for col in columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna(subset=columns)
df.reset_index(inplace = True, drop=True)

names = df[['Car Make', 'Car Model', 'Year', 'Price (in USD)']].values.tolist()

cleaned_df = df.drop(['Car Make', 'Car Model', 'Year', 'Price (in USD)'], axis =1)
cleaned_df.reset_index(inplace = True, drop=True)

# pd.set_option('display.max_rows', None)
# print(df)

# *****************************************************************************************************************

# Get First Target Car
target_car = df.loc[0, columns].astype(float)

# Get Distances
distances = scipy.spatial.distance.cdist(cleaned_df, [target_car], metric="euclidean")[:,0]
query_distances = list(zip(cleaned_df.index, distances))

# Print Most Similar Cars
count = False
for idx, similarity_score in sorted(query_distances, key=lambda x: x[1], reverse=False)[:10]:
    if count == False:
        print('Car to Compare:')
        print(names[idx][0], names[idx][1], names[idx][2], '$' + str(names[idx][3]))
        print('\nMost Similar Cars by Performance')
        count = True
    else:
        print(names[idx][0], names[idx][1], names[idx][2], similarity_score, '$' + str(names[idx][3]))

# *****************************************************************************************************************
        
# Get Second Target Car
target_car = df.loc[1, columns].astype(float)

# Get Distances
distances = scipy.spatial.distance.cdist(cleaned_df, [target_car], metric="euclidean")[:,0]
query_distances = list(zip(cleaned_df.index, distances))

# Print Most Similar Cars
count = False
for idx, similarity_score in sorted(query_distances, key=lambda x: x[1], reverse=False)[:10]:
    if count == False:
        print('\nCar to Compare:')
        print(names[idx][0], names[idx][1], names[idx][2], '$' + str(names[idx][3]))
        print('\nMost Similar Cars by Performance')
        count = True
    else:
        print(names[idx][0], names[idx][1], names[idx][2], similarity_score, '$' + str(names[idx][3]))

# *****************************************************************************************************************
    
# Get Third Target Car
target_car = df.loc[202, columns].astype(float)

# Get Distances
distances = scipy.spatial.distance.cdist(cleaned_df, [target_car], metric="euclidean")[:,0]
query_distances = list(zip(cleaned_df.index, distances))

# Print Most Similar Cars
count = False
for idx, similarity_score in sorted(query_distances, key=lambda x: x[1], reverse=False)[:10]:
    if count == False:
        print('\nCar to Compare:')
        print(names[idx][0], names[idx][1], names[idx][2], '$' + str(names[idx][3]))
        print('\nMost Similar Cars by Performance')
        count = True
    else:
        print(names[idx][0], names[idx][1], names[idx][2], similarity_score, '$' + str(names[idx][3]))