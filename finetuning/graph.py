import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('output.csv')  # Replace with your actual filename

# Drop columns with all NaN values (optional, useful if some metrics were never recorded)
df = df.dropna(axis=1, how='all')

df = df.groupby(df.index // 30).mean().reset_index(drop=True)

x = df.index * 30

for column in df.columns:
        if column != 'step':
            plt.plot(x, df[column], label=column)

# Add labels and legend
plt.xlabel('Step')
plt.ylabel('Value')
plt.title('Training Metrics Over Steps')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()