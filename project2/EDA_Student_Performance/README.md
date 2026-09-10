Exploratory Data Analysis – Student Performance
Project Overview

This project performs Exploratory Data Analysis (EDA) on a Student Performance dataset.

The purpose of this project is to understand patterns, trends, distributions, relationships, and possible outliers in student academic performance.

Dataset

The dataset contains information about 15 students.

Variables
Student – Student name
Math – Mathematics marks
English – English marks
Science – Science marks
Attendance – Attendance percentage
Objectives

The main objectives are:

Calculate basic statistics.
Calculate mean and median.
Identify missing values.
Identify duplicate records.
Analyze distributions.
Identify possible outliers.
Analyze relationships between variables.
Identify trends.
Compare student performance.
Summarize important observations.
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
How to Run
Step 1

Install the required libraries:

pip install -r requirements.txt

Step 2

Make sure the project has this structure:

EDA_Student_Performance/
│
├── data/
│   └── student_performance.csv
│
├── output/
│
├── EDA_Student_Performance.py
├── requirements.txt
└── README.md

Step 3

Run the Python program:

python EDA_Student_Performance.py

Analysis Performed

The program performs:

Dataset inspection
Data type checking
Missing-value analysis
Duplicate-value analysis
Data validation
Mean calculation
Median calculation
Minimum and maximum calculation
Average marks calculation
Performance categorization
Correlation analysis
IQR-based outlier detection
Data visualization
Visualizations

The project generates:

Mathematics marks distribution
Subject-wise box plot
Average marks by subject
Average marks by student
Attendance vs average marks
Correlation heatmap
Subject-wise marks distribution
Output

All generated graphs and analysis files are saved in the output folder.

Conclusion

The EDA provides a clear overview of student academic performance and attendance. It helps identify distributions, relationships, performance differences, and potential outliers in the dataset.