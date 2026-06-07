import pandas as pd

# --- DATAFRAME CREATION ---
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'dept': ['CS', 'IT', 'CS', 'EC']
})

df2 = pd.DataFrame({
    'id': [1, 2, 5, 6],
    'salary': [50000, 60000, 45000, 55000],
    'dept': ['CS', 'IT', 'ME', 'CE']
}
inner = pd.merge(df1, df2, on='id', how='inner')
print("--- INNER MERGE ---")
print(inner)

left = pd.merge(df1, df2, on='id', how='left')
print("\n--- LEFT MERGE ---")
print(left)

right = pd.merge(df1, df2, on='id', how='right')
print("\n--- RIGHT MERGE ---")
print(right)

multi_col = pd.merge(df1, df2, on=['id', 'dept'], how='inner')
print("\n--- MULTI-COLUMN MERGE ---")
print(multi_col)

# --- PIVOT TABLE ---
sales = pd.DataFrame({
    'month': ['Jan', 'Jan', 'Feb', 'Feb'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 150, 120, 180]
})

print("\n--- PIVOT TABLE RESULT ---")
pivot1 = sales.pivot(index='month', columns='product', values='sales')
print(pivot1)
