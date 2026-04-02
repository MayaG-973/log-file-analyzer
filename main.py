import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

non_errors = ['200 OK', 'User Login', 'File Uploaded']

# Load the log data
data = pd.read_csv('data/logs.csv', parse_dates=['timestamp'])

# Extract data from timestamp
data['date'] = data['timestamp'].dt.date

# Count errors by type
errors_only = data[~data['error_type'].isin(non_errors)]
error_counts = errors_only['error_type'].value_counts()
print("Error counts by type:\n", error_counts)

# Count errors per day
daily_errors = errors_only.groupby('date').size()
print("Errors per day:\n", daily_errors)

# Plot errors by type using bar plot
plt.figure(figsize=(6,4))
sns.barplot(x=error_counts.index, y=error_counts.values)
plt.title("Errors by Type")
plt.ylabel("Counts")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/error_types.png")
plt.show()

# Plot errors per day using line chart
plt.figure(figsize=(6,4))
daily_errors.plot(kind='line', marker='o')
plt.title("Errors per day")
plt.xlabel("Date")
plt.ylabel("# of Errors")
plt.tight_layout()

plt.savefig("images/error_per_day.png")
plt.show()
