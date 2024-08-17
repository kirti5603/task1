import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import os

# Print the current working directory to help locate the file
print("Current Working Directory:", os.getcwd())

# Load the dataset from CSV file
try:
    df = pd.read_csv('sales_dataset.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("File not found. Please ensure 'sales_dataset.csv' is in the correct directory.")
    exit()

# Check if the dataset was loaded correctly
print("\nDataset Preview:")
print(df.head())

# Verify column names
print("\nColumn Names:")
print(df.columns)

# Correct column names based on actual dataset
df.columns = df.columns.str.strip()  # Remove any leading/trailing whitespace
df.rename(columns={'marketing_budget(thousands)': 'Marketing_Budget_Thousands',
                   'actual_sales(millions)': 'Actual_Sales_Millions'}, inplace=True)

# Calculate correlation
correlation = df.corr().iloc[0, 1]

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(df['Marketing_Budget_Thousands'], df['Actual_Sales_Millions'])

# Create scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Budget_Thousands', y='Actual_Sales_Millions', data=df, color='blue', label='Data Points')
plt.plot(df['Marketing_Budget_Thousands'], intercept + slope * df['Marketing_Budget_Thousands'], color='red', label='Fit Line')
plt.xlabel('Marketing Budget (Thousands)')
plt.ylabel('Actual Sales (Millions)')
plt.title('Marketing Budget vs. Actual Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Display correlation and regression results
print("\nCorrelation between Marketing Budget and Actual Sales:", correlation)
print("Linear Regression Results:")
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R-squared: {r_value**2:.2f}")
print(f"P-value: {p_value:.2f}")
print(f"Standard Error: {std_err:.2f}")

# Recommendations (Example based on analysis)
if correlation > 0:
    print("\nThere is a positive correlation between marketing budget and actual sales.")
else:
    print("\nThere is a negative correlation between marketing budget and actual sales.")
