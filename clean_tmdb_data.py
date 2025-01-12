import pandas as pd
import ast

# Load the datasets
movies = pd.read_csv('dataset/tmdb_5000_movies.csv')


# Quick overview of the data
print("Movies Dataset Overview:")
print(movies.info())


'''
Step 1: Handle Missing Values
'''

# Drop rows with missing release_date or runtime
movies = movies.dropna(subset=['release_date', 'runtime'])

# Fill missing tagline with 'No tagline available'
movies['tagline'] = movies['tagline'].fillna('No tagline available')

# Confirm no missing values remain
print(movies.isnull().sum())


'''
Step 2: Parse JSON-Like Columns

'''


# Parse genres to convert from string to list of dictionaries
movies['genres'] = movies['genres'].apply(ast.literal_eval)

# Extract genre names into a new column
movies['genre_names'] = movies['genres'].apply(lambda x: [d['name'] for d in x])


'''
Step 3: Convert Columns to Appropriate Data Types

'''

# Convert release_date to datetime format
movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')

# Extract release year for easier analysis
movies['release_year'] = movies['release_date'].dt.year


'''
Step 4: Remove Unnecessary Columns
'''
# Drop columns that aren't needed
movies = movies.drop(['homepage', 'keywords', 'production_companies', 'production_countries', 'spoken_languages'], axis=1)



'''
Step 5: Save Cleaned Data

'''

# Save cleaned data to a new CSV file
movies.to_csv('dataset/cleaned_movies.csv', index=False)
print("Cleaned dataset saved as 'cleaned_movies.csv'.")
