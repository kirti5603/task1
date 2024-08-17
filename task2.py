import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = 'Financial Statements.csv'
df = pd.read_csv(file_path)

# Step 2: Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())


# Step 3: Define a function to calculate financial ratios
def calculate_ratios(df):
    # Liquidity Ratios
    df['Current Ratio'] = df['Current Ratio']

    # Solvency Ratios
    df['Debt to Equity Ratio'] = df['Debt/Equity Ratio']

    # Profitability Ratios
    df['Return on Equity (ROE)'] = df['ROE']
    df['Return on Assets (ROA)'] = df['ROA']
    df['Net Profit Margin'] = df['Net Profit Margin']
    df['Earnings per Share (EPS)'] = df['Earning Per Share']

    # Efficiency Ratios (e.g., Return on Investment)
    df['Return on Investment (ROI)'] = df['ROI']

    return df


# Calculate financial ratios
df = calculate_ratios(df)


# Step 4: Analyze trends over the years
def plot_trends(df, column_name, title):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df[column_name], marker='o')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel(column_name)
    plt.grid(True)
    plt.show()


# Plot trends for key financial metrics
plot_trends(df, 'Market Cap(in B USD)', 'Market Cap Trend')
plot_trends(df, 'Revenue', 'Revenue Trend')
plot_trends(df, 'Net Income', 'Net Income Trend')
plot_trends(df, 'Earnings per Share (EPS)', 'Earnings per Share Trend')

# Step 5: Conduct SWOT Analysis
swot_analysis = {
    'Strengths': ['High Market Cap', 'Strong Revenue Growth', 'Consistent Profitability'],
    'Weaknesses': ['High Debt to Equity Ratio', 'Volatile Cash Flow'],
    'Opportunities': ['Expansion into new markets', 'Investment in R&D'],
    'Threats': ['Market Volatility', 'Economic Downturn', 'Increased Competition']
}

print("\nSWOT Analysis:")
for key, value in swot_analysis.items():
    print(f"{key}: {', '.join(value)}")

# Step 6: Identify Internal and External Factors
internal_factors = ['Strong brand equity', 'Effective cost management']
external_factors = ['Changing market trends', 'Economic conditions']

print("\nInternal Factors Impacting Financial Health:")
for factor in internal_factors:
    print(f"- {factor}")

print("\nExternal Factors Impacting Financial Health:")
for factor in external_factors:
    print(f"- {factor}")

# Step 7: Evaluate Potential Financial Risks
risks = ['Market Volatility', 'Credit Risk', 'Operational Risks']
print("\nPotential Financial Risks:")
for risk in risks:
    print(f"- {risk}")

# Step 8: Suggest Risk Mitigation Strategies
mitigation_strategies = {
    'Market Volatility': 'Diversify investment portfolio and hedge against currency risks.',
    'Credit Risk': 'Strengthen credit evaluation processes and increase liquidity reserves.',
    'Operational Risks': 'Implement robust operational controls and invest in technology.'
}

print("\nRisk Mitigation Strategies:")
for key, value in mitigation_strategies.items():
    print(f"{key}: {value}")

# Step 9: Develop Strategic Recommendations
recommendations = {
    'Cost Management': 'Optimize operating expenses and reduce non-essential costs.',
    'Revenue Enhancement': 'Diversify revenue streams and explore new markets.',
    'Investment Opportunities': 'Invest in technology and innovation to stay competitive.'
}

print("\nStrategic Recommendations:")
for key, value in recommendations.items():
    print(f"{key}: {value}")

# Step 10: Save the enhanced dataset with calculated ratios
output_file_path = 'Financial_Statements_Enhanced.csv'
df.to_csv(output_file_path, index=False)
print(f"\nEnhanced dataset saved to: {output_file_path}")

# Additional Step: Prepare presentation (This would typically involve creating a PowerPoint or similar)
# The presentation would include the visualizations, SWOT analysis, financial risks, and strategic recommendations.
