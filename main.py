import matplotlib.pyplot as plt
import pandas as pd
#load the dataset
df=pd.read_csv("StudentsPerformance.csv")
#display the first five rows of the dataset
print("First Five Rows")
print(df.head())
#display number of rows and columns 
print("\n Dataset Shape")
print(df.shape)
#display the column names
print("\n Column Names")
print(df.columns)
#Display dataset information
print("\n Dataset Information")
print(df.info())
# Check for missing values
print("\nMISSING VALUES")
print(df.isnull().sum())
# Check for duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())
# Calculate each student's average score
df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

# Display selected columns for the first five students
print("\nSTUDENT AVERAGES")
print(
    df[["math score", "reading score",
        "writing score", "average_score"]].head())

# Calculate average marks by subject
subject_averages = df[
    ["math score", "reading score", "writing score"]
].mean()

# Use shorter labels for the chart
subject_averages.index = ["Math", "Reading", "Writing"]

# Create the bar chart
ax = subject_averages.plot(kind="bar", figsize=(8, 5))

# Add chart details
plt.title("Average Student Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)

# Display the exact average above each bar
ax.bar_label(ax.containers[0], fmt="%.2f", padding=3)

plt.tight_layout()
plt.savefig("average_scores.png", dpi=300, bbox_inches="tight")
plt.show()
