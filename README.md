# Sports Car Similarity

This Python script provides an intuitive way to find cars similar to a target vehicle based on performance metrics. By analyzing a dataset of sports cars, the script calculates the Euclidean distance between the target car's specifications and those of other cars in the dataset, identifying the most similar cars based on engine size, horsepower, torque, and acceleration time.

## Complimentary Medium Post
Here is a link to my Medium post describing my processes and the insights that can be drawn from it: <br /> 
https://medium.com/inst414-data-science-tech/what-cars-are-most-similar-ba80049f0240

## Features

- **Data Cleaning and Formatting**: Prepares the dataset by removing duplicates and ensuring numerical data is correctly formatted.
- **Similarity Score Calculation**: Uses the Euclidean distance to quantify similarities between cars based on selected performance metrics.
- **Target Car Selection**: Allows users to choose a target car and find the top 10 most similar cars based on the similarity score.

## How It Works

1. **Data Preparation**: The script begins by loading and cleaning the dataset, ensuring that data is free of duplicates and formatted correctly for analysis.
2. **Selecting a Target Car**: Users can specify a target car by its index in the dataset. The script then retrieves this car's performance metrics.
3. **Calculating Similarity Scores**: The script computes the Euclidean distances between the target car and all other cars in the dataset based on the specified performance metrics.
4. **Identifying Similar Cars**: It then ranks all cars by their similarity scores and displays the top 10 most similar cars, along with their make, model, year, price, and similarity score.

## Prerequisites

To run this script, you'll need:

- Python 3.x
- Pandas library
- SciPy library

Make sure these are installed in your environment.

## Usage

1. Ensure your dataset is named `Sport car price.csv` and placed in the same directory as the script.
2. Run the script. The output will include the target car's details and the top 10 most similar cars by performance metrics for each target car specified in the script.
