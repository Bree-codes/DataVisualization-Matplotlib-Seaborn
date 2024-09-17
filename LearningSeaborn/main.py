import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create a DataFrame
data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    'Region': ['North', 'North', 'North', 'North', 'North', 'South', 'South', 'South', 'South', 'South'],
    'Sales': [100, 150, 200, 130, 170, 120, 160, 210, 140, 180],
    'Profit': [20, 30, 40, 25, 35, 22, 32, 42, 28, 38]
}

df = pd.DataFrame(data)

# Step 2: Bar plot for average sales per product
plt.figure()
sns.barplot(x='Product', y='Sales', data=df)
plt.title('Average Sales per Product')
plt.savefig('barplot_sales_per_product.png')
plt.show()

# Step 3: Box plot to show sales distribution by region
plt.figure()
sns.boxplot(x='Region', y='Sales', data=df)
plt.title('Sales Distribution by Region')
plt.savefig('boxplot_sales_distribution.png')
plt.show()

# Step 4: Scatter plot to visualize Sales vs Profit
plt.figure()
sns.scatterplot(x='Sales', y='Profit', hue='Region', style='Product', data=df)
plt.title('Sales vs Profit by Region and Product')
plt.savefig('scatterplot_sales_vs_profit.png')
plt.show()

# Step 5: Correlation matrix heatmap
plt.figure()
corr = df[['Sales', 'Profit']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Between Sales and Profit')
plt.savefig('heatmap_correlation_sales_profit.png')
plt.show()

# Step 6: Customize with Seaborn Themes and save scatter plot with theme
plt.figure()
sns.set_theme(style='whitegrid')
sns.scatterplot(x='Sales', y='Profit', hue='Region', style='Product', data=df)
plt.title('Sales vs Profit (Themed)')
plt.savefig('scatterplot_sales_vs_profit_themed.png')
plt.show()

