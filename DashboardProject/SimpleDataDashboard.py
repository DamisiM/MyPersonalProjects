import pandas as pd 
import matplotlib.pyplot as plt

#data = pd.read_csv('salesData.csv', encoding='latin1', on_bad_lines='skip')
data = pd.read_excel('salesData.csv')
print(data.head())

total_units_sold = data['Quantity'].sum()
total_revenue = (data['Quantity'] * data['Price per Unit']) . sum()
top_selling_product = data.groupby('Product Category')['Quantity'].sum().idxmax()
product_sales = data.groupby('Product Category')['Quantity'].sum()

# Group by 'Age Group' and sum the 'Quantity' sold
agegroup_slaes = data.groupby('Age Group')['Quantity'].sum()
# Find the age group with the highest sales
top_selling_agegroup =agegroup_slaes.idxmax()
# Get the total quantity sold for that age group
top_selling_agegroup_units_sold = agegroup_slaes[top_selling_agegroup]

print("======OUR SALES SUMMARY REPORT=======")
print(f"Total Units Sold: {total_units_sold}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Top-Selling Product: {top_selling_product}")
print(f"Age Group Of The Moment: {top_selling_agegroup}, Units Sold: {top_selling_agegroup_units_sold}")

plt.figure(figsize=(10, 8.5))
psplot = product_sales.plot(kind='bar', color='#4CAF50', edgecolor='black', linewidth=0.5)

plt.title('Units Sold per Product', fontsize=20, fontweight='bold', color='darkblue', pad=20)
plt.xlabel('Product', fontsize=16, fontweight='bold', color='black', labelpad=15)
plt.ylabel('Units Sold', fontsize=16, fontweight='bold', color='black', labelpad=15)
plt.xticks(rotation=45, ha='right', fontsize=12, fontweight='bold', color='black')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add labels on top of each bar to display the actual values
for a in psplot.patches:
    psplot.annotate(f'{a.get_height()}', (a.get_x() + a.get_width() / 2., a.get_height()),
                ha='center', va='center', fontsize=12, fontweight='bold', color='black', xytext=(0, 10),
                textcoords='offset points')
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()
