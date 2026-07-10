# YouTube Views Predictor

A Machine Learning project built using Python, Pandas, and Scikit-learn to predict YouTube video views based on video characteristics.

## Features

* Load and analyze CSV datasets
* Train a Linear Regression model
* Predict YouTube video views
* Split data into training and testing sets
* Evaluate model performance using R² Score
* Work with a dataset containing 200 records

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

## Dataset

The dataset contains the following features:

| Column      | Description          |
| ----------- | -------------------- |
| VideoLength | Length of the video  |
| UploadTime  | Video upload time    |
| TagsCount   | Number of tags used  |
| Views       | Total views received |

## Machine Learning Workflow

1. Load the dataset using Pandas
2. Select features and target variable
3. Split data into training and testing sets
4. Train a Linear Regression model
5. Generate predictions
6. Evaluate performance using R² Score

## Project Structure

Youtube-Views-Predictor/

├── youtube_views_200.csv

├── Views_predictor.py

└── README.md

## Model Performance

* Algorithm: Linear Regression
* Dataset Size: 200 Records
* R² Score: 0.9821

The model explains approximately 98.21% of the variation in video views.

## How to Run

Install required libraries:

pip install pandas scikit-learn matplotlib

Run the project:

python Views_predictor.py

## Learning Outcomes

* Data preprocessing using Pandas
* Train-Test Split
* Linear Regression
* Model evaluation using R² Score
* Working with larger datasets
* Building Machine Learning projects using Scikit-learn

## Future Improvements

* Add more video-related features
* Compare multiple regression algorithms
* Visualize predictions and trends
* Deploy the model as a web application

## Author

Navadeep

Built as part of my Machine Learning learning journey.
