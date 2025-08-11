import pandas as pd
import matplotlib.pyplot as plt

# Merge Join Example visualization
# Sample DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'value_a': [10, 20, 30]
})

df2 = pd.DataFrame({
    'id': [3, 4, 5],
    'value_b': [30, 40, 50]
})

# Merge
merged_df = pd.merge(df1, df2, on='id', how='inner')
print(merged_df)

#Plot
plt.figure(figsize=(8, 5))
plt.bar(merged_df['id'], merged_df['value_a'], label='Value A', alpha=0.6)
plt.bar(merged_df['id'], merged_df['value_b'], label='Value B', alpha=0.6)
plt.xlabel('ID')
plt.ylabel('Values')
plt.title('Bar Plot of Merged Values')
plt.legend()
plt.show()

# Concatenation Example visualization
# Concatenate
concatenated_df = pd.concat([df1, df2], axis=0)  # By rows
print(concatenated_df)

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(concatenated_df.index, concatenated_df['value_a'], label='Value A')
plt.scatter(concatenated_df.index, concatenated_df['value_b'], label='Value B')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Scatter Plot of Concatenated Values')
plt.legend()
plt.show()
