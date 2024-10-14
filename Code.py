import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data and export as CSV
data = {
    'Genome': ['Genome1', 'Genome2', 'Genome3', 'Genome4', 'Genome5', 'Genome6'],
    'Total_Genes': [5000, 6000, 5500, 7000, 6200, 5900],
    'R_Genes': [2200, 3250, 4300, 5280, 5320, 3260]
}

# Read the CSV file
df = pd.read_csv('genome_data.csv')

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Total genes on the left side (using negative values to plot from the middle)
bars_total = ax.barh(df['Genome'], -df['Total_Genes'], color='skyblue', label='Total Genes')

# R genes on the right side (positive values)
bars_r = ax.barh(df['Genome'], df['R_Genes'], color='orange', label='R Genes')

# Add labels and title
ax.set_xlabel('Number of Genes')
ax.set_title('Total Genes and R Genes in Six Genomes')

# Customize x-axis to show from 0 on both sides (0 to 10000 on left and right)
ax.set_xlim([-10000, 10000])

# Custom x-axis tick labels (showing positive values on both sides)
ticks = np.linspace(-10000, 10000, 11)
ax.set_xticks(ticks)
ax.set_xticklabels([int(abs(x)) for x in ticks])

# Add a vertical line at x=0 to serve as the y-axis
ax.axvline(0, color='black', linewidth=1)

# Add grid lines for clarity
ax.grid(True, axis='x', linestyle='--', alpha=0.7)

# Show numbers on bars (for total genes)
for bar in bars_total:
    ax.text(bar.get_width() - 200, bar.get_y() + bar.get_height()/2,  # Position adjustment
            f'{-int(bar.get_width())}', va='center', ha='right', color='black')

# Show numbers on bars (for R genes)
for bar in bars_r:
    ax.text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2,  # Position adjustment
            f'{int(bar.get_width())}', va='center', ha='left', color='black')

# Show legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()

