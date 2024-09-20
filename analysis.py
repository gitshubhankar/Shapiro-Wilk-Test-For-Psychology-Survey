# Load the data from the first sheet
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the first few rows of the dataframe to inspect the data
df.head()

from scipy import stats

# Selecting numerical columns for the Shapiro-Wilk test
numerical_columns = ['AGE', 'FAMILY TYPE SCORE', 'STRESS LEVEL SCORE', 'Unnamed: 5']

# Dropping rows with missing values in these columns
df_cleaned = df[numerical_columns].dropna()

# Performing the Shapiro-Wilk test for normality on each numerical column
shapiro_results = {}
for column in numerical_columns:
    stat, p_value = stats.shapiro(df_cleaned[column])
    shapiro_results[column] = {'W-statistic': stat, 'p-value': p_value}

shapiro_results

