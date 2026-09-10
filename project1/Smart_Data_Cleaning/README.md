# Smart Data Cleaning Project

## Introduction

This project demonstrates the basic process of cleaning a raw dataset using Python and Pandas.

The raw dataset contains missing values, duplicate records, incorrect values, inconsistent text, different date formats, and invalid numeric values.

The purpose of this project is to prepare the dataset for further analysis.

## Objectives

The main objectives are:

1. Identify missing values.
2. Remove duplicate records.
3. Correct incorrect data.
4. Standardize dates.
5. Convert numbers into correct numeric formats.
6. Clean text values.
7. Generate a final cleaned dataset.

## Technologies Used

- Python
- Pandas
- CSV

## Dataset Fields

The dataset contains:

- Name
- Age
- Date
- Gender
- City
- Salary
- Email

## Data Cleaning Operations

### Missing Values

Missing values are identified using:

```python
df.isnull().sum()