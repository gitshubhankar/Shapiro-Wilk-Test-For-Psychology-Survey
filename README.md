# Data Distribution Analysis Project

## Project Overview
This project aims to analyze the normality of a dataset using the **Shapiro-Wilk Test**. The dataset contains demographic and psychometric data such as age, family type score, and stress level score. The Shapiro-Wilk test is used to determine whether the numerical columns in the dataset follow a normal distribution, which is essential for many statistical analyses.

## Dataset

The dataset used for this project consists of the following columns:
- **NAME**: The participant's name (string).
- **AGE**: The age of the participant (numerical).
- **FAMILY TYPE SCORE**: A score representing the participant's family type (numerical).
- **STRESS LEVEL SCORE**: A score representing the participant's stress level (numerical).
- **FAMILY TYPE**: A categorical description of the family type (string).
- **Unnamed: 5**: An unnamed numerical column containing additional data.

## Objectives



To run this analysis, ensure you have the following packages installed in your Python environment:

```bash
pip install pandas scipy openpyxl
```

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/gitshubhankar/Shapiro-Wilk-Test-For-Psychology-Survey.git
   cd Shapiro-Wilk-Test-For-Psychology-Survey
   ```

2. Place your dataset (`mang research.xlsx`) in the project directory.

3. Run the analysis script:
   ```bash
   python shapiro_wilk_analysis.py
   ```

## Preprocessing

### Step 1: Data Loading
The dataset is loaded from an Excel file using `pandas` and inspected for its structure. The first sheet of the workbook contains the relevant data.

### Step 2: Data Cleaning
To prepare the data for the Shapiro-Wilk test, we selected the following numerical columns:
- **AGE**
- **FAMILY TYPE SCORE**
- **STRESS LEVEL SCORE**
- **Unnamed: 5**

Rows with missing values in these columns were removed.

### Step 3: Shapiro-Wilk Test
The Shapiro-Wilk test was applied to each of the numerical columns to test for normal distribution.

```python
from scipy import stats

# Example of Shapiro-Wilk Test for one column
stat, p_value = stats.shapiro(df['AGE'])
```

### Results

| Column                | W-Statistic | p-value  | Normal Distribution? |
|-----------------------|-------------|----------|----------------------|
| **AGE**               | 0.927       | 0.0043   | No                   |
| **FAMILY TYPE SCORE** | 0.965       | 0.1432   | Yes                  |
| **STRESS LEVEL SCORE**| 0.932       | 0.0068   | No                   |
| **Unnamed: 5**        | 0.927       | 0.0043   | No                   |

### Interpretation:
- Columns with a p-value **greater than 0.05** are considered to follow a normal distribution. In this case, **FAMILY TYPE SCORE** is normally distributed.
- Columns with a p-value **less than 0.05** do not follow a normal distribution. This includes **AGE**, **STRESS LEVEL SCORE**, and **Unnamed: 5**.

## Conclusion

Only the **FAMILY TYPE SCORE** data appears to be evenly distributed, while the rest of the variables do not follow a normal distribution. Further statistical analyses requiring normal distribution (e.g., parametric tests) should only use the "FAMILY TYPE SCORE" or apply transformations to the non-normal variables.

