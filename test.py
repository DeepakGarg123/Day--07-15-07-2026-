import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Calculate correlation matrix
corr = tips.corr(numeric_only=True)

# Create heatmap
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()