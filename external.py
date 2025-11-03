import matplotlib.pyplot as plt

# Labels and accuracy data
labels = ['Helmet', 'Vest', 'Mask']
accuracy = [98.4, 94.1, 97.4]

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(labels, accuracy, color='skyblue', edgecolor='navy')

# Adding data labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval}%', ha='center', va='bottom')

# Formatting the chart
plt.ylim(0, 100)
plt.ylabel('Accuracy (%)')
plt.title('PPE Detection Accuracy')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
