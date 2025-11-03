import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set style for professional-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Dataset statistics - ONLY FOR HELMET, VEST, AND MASK
class_names = ['helmet', 'vest', 'mask']

# From the provided data (focusing only on 3 main PPE categories)
train_counts = [2231, 1797, 1050]  # helmet, vest, mask
valid_counts = [765, 580, 314]     # helmet, vest, mask  
test_counts = [300, 258, 162]      # helmet, vest, mask

# Calculate totals for 3 classes only
total_counts = [train_counts[i] + valid_counts[i] + test_counts[i] for i in range(3)]
total_annotations = sum(total_counts)

print("=== REFINED DATASET STATISTICS (3 MAIN PPE CLASSES) ===")
print(f"Total Annotations (3 classes): {total_annotations:,}")
print(f"Training Set: {sum(train_counts):,} ({sum(train_counts)/total_annotations*100:.1f}%)")
print(f"Validation Set: {sum(valid_counts):,} ({sum(valid_counts)/total_annotations*100:.1f}%)")
print(f"Test Set: {sum(test_counts):,} ({sum(test_counts)/total_annotations*100:.1f}%)")
print("\nClass Distribution:")
for i, name in enumerate(class_names):
    print(f"{name}: {total_counts[i]:,} ({total_counts[i]/total_annotations*100:.1f}%)")

# Create Figure 4.1: Technology Stack Diagram (Text-based representation)
fig1, ax1 = plt.subplots(figsize=(14, 10))
ax1.axis('off')

# Technology stack layers
layers = [
    "Development Environment\nPython 3.10 | VS Code | Git",
    "Web Framework\nFlask 2.3.3 | Flask-Login | Werkzeug",
    "Database & Auth\nPostgreSQL | bcrypt | python-dotenv",
    "ML & Computer Vision\nYOLOv8 | PyTorch | OpenCV | NumPy",
    "Data Processing\nPandas | Matplotlib | Seaborn | Pillow",
    "Cloud Training\nGoogle Colab | Roboflow | GPU",
    "Deployment\nFlask Dev Server | Google App Engine | Gunicorn"
]

colors = ['#E8F4FD', '#D1E7DD', '#FFF3CD', '#F8D7DA', '#E2E3F3', '#D3D3D4', '#FCF8E3']

for i, (layer, color) in enumerate(zip(layers, colors)):
    rect = plt.Rectangle((0.1, 0.8 - i*0.12), 0.8, 0.1, 
                        facecolor=color, edgecolor='black', linewidth=1)
    ax1.add_patch(rect)
    ax1.text(0.5, 0.85 - i*0.12, layer, ha='center', va='center', 
            fontsize=10, fontweight='bold')

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_title('Figure 4.1: Development Environment and Technology Stack', 
              fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('Figure_4_1_Technology_Stack.png', dpi=300, bbox_inches='tight')
plt.show()

# Create Figure 4.2: Dataset Statistics for 3 PPE Classes
fig2, ((ax2, ax3), (ax4, ax5)) = plt.subplots(2, 2, figsize=(16, 12))

# Subplot 1: Overall class distribution (pie chart) - 3 classes only
colors_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # Red for helmet, Teal for vest, Blue for mask
wedges, texts, autotexts = ax2.pie(total_counts, labels=class_names, autopct='%1.1f%%', 
                                  colors=colors_pie, startangle=90)
ax2.set_title(f'PPE Class Distribution\n(Total: {total_annotations:,} annotations)', 
              fontsize=12, fontweight='bold')

# Subplot 2: Train/Valid/Test split
split_labels = ['Training', 'Validation', 'Test']
split_counts = [sum(train_counts), sum(valid_counts), sum(test_counts)]
split_percentages = [count/total_annotations*100 for count in split_counts]

bars2 = ax3.bar(split_labels, split_counts, color=['#3498db', '#f39c12', '#e74c3c'])
ax3.set_title('Dataset Split Distribution', fontsize=12, fontweight='bold')
ax3.set_ylabel('Number of Annotations')

# Add percentage labels on bars
for i, (count, pct) in enumerate(zip(split_counts, split_percentages)):
    ax3.text(i, count + 50, f'{count:,}\n({pct:.1f}%)', 
            ha='center', va='bottom', fontweight='bold')

# Subplot 3: Class distribution comparison across splits
x = np.arange(len(class_names))
width = 0.25

bars1 = ax4.bar(x - width, train_counts, width, label='Training', color='#3498db', alpha=0.8)
bars2 = ax4.bar(x, valid_counts, width, label='Validation', color='#f39c12', alpha=0.8)
bars3 = ax4.bar(x + width, test_counts, width, label='Test', color='#e74c3c', alpha=0.8)

ax4.set_xlabel('PPE Classes')
ax4.set_ylabel('Number of Annotations')
ax4.set_title('Class Distribution Across Dataset Splits', fontsize=12, fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(class_names)
ax4.legend()
ax4.grid(True, alpha=0.3)

# Add count labels on bars
for i, (train, valid, test) in enumerate(zip(train_counts, valid_counts, test_counts)):
    ax4.text(i-width, train + 30, str(train), ha='center', va='bottom', fontsize=9)
    ax4.text(i, valid + 15, str(valid), ha='center', va='bottom', fontsize=9)
    ax4.text(i+width, test + 10, str(test), ha='center', va='bottom', fontsize=9)

# Subplot 4: Class imbalance visualization
class_percentages = [count/total_annotations*100 for count in total_counts]
bars4 = ax5.barh(class_names, class_percentages, color=colors_pie)
ax5.set_xlabel('Percentage of Total Annotations (%)')
ax5.set_title('Class Distribution Analysis', fontsize=12, fontweight='bold')
ax5.grid(True, alpha=0.3)

# Add percentage labels
for i, (name, pct) in enumerate(zip(class_names, class_percentages)):
    ax5.text(pct + 0.5, i, f'{pct:.1f}%', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('Figure_4_2_Dataset_Statistics_3_Classes.png', dpi=300, bbox_inches='tight')
plt.show()

# Calculate and display key statistics
print(f"\n=== KEY DATASET METRICS (3 CLASSES) ===")
most_common = max(total_counts)
least_common = min(total_counts)
imbalance_ratio = most_common / least_common
print(f"Most Common Class: {class_names[total_counts.index(most_common)]} ({most_common:,} annotations)")
print(f"Least Common Class: {class_names[total_counts.index(least_common)]} ({least_common:,} annotations)")
print(f"Class Imbalance Ratio: {imbalance_ratio:.1f}:1")

# Create Figure 4.3: Flask Application Architecture
fig3, ax3 = plt.subplots(figsize=(14, 10))
ax3.axis('off')

# Architecture layers with Flask-specific components
layers = [
    ("Client Layer", ["Web Browser", "Video Upload UI", "Admin Dashboard"], '#E8F4FD'),
    ("Flask Routes", ["Authentication", "Video Processing", "Admin Panel"], '#D1E7DD'),
    ("Authentication", ["Flask-Login", "bcrypt", "Sessions"], '#FFF3CD'),
    ("Detection Layer", ["hubconfCustom.py", "tracker.py", "YOLOv8"], '#F8D7DA'),
    ("Database Layer", ["PostgreSQL", "users", "sessions", "results"], '#E2E3F3'),
    ("Storage", ["static/files/", "templates/"], '#FCF8E3')
]

y_positions = [0.85, 0.7, 0.55, 0.4, 0.25, 0.1]
for i, (layer_name, components, color) in enumerate(layers):
    y_pos = y_positions[i]
    
    # Draw layer background
    rect = plt.Rectangle((0.05, y_pos - 0.05), 0.9, 0.12, 
                        facecolor=color, edgecolor='black', linewidth=1, alpha=0.7)
    ax3.add_patch(rect)
    
    # Layer name
    ax3.text(0.1, y_pos + 0.03, layer_name, fontsize=12, fontweight='bold')
    
    # Components
    comp_text = " | ".join(components)
    ax3.text(0.1, y_pos - 0.02, comp_text, fontsize=10, style='italic')

ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.set_title('Figure 4.3: Flask Application Architecture with 3-PPE Detection', 
              fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('Figure_4_3_Flask_Architecture.png', dpi=300, bbox_inches='tight')
plt.show()

# Create Figure 4.4: Detection Pipeline Flow
fig4, ax4 = plt.subplots(figsize=(16, 8))
ax4.axis('off')

# Pipeline stages
stages = [
    "Video/Webcam\nInput",
    "Frame\nExtraction", 
    "YOLOv8\nDetection",
    "PPE Classification\n(Helmet/Vest/Mask)",
    "Object\nTracking",
    "Compliance\nEvaluation",
    "Visual\nOverlay",
    "Results &\nStorage"
]

# Stage positions
x_positions = np.linspace(0.05, 0.95, len(stages))
y_center = 0.5

# Draw pipeline stages
for i, (stage, x_pos) in enumerate(zip(stages, x_positions)):
    # Stage box
    rect = plt.Rectangle((x_pos - 0.05, y_center - 0.15), 0.1, 0.3, 
                        facecolor='lightblue', edgecolor='navy', linewidth=2)
    ax4.add_patch(rect)
    
    # Stage text
    ax4.text(x_pos, y_center, stage, ha='center', va='center', 
            fontsize=9, fontweight='bold')
    
    # Arrow to next stage
    if i < len(stages) - 1:
        ax4.arrow(x_pos + 0.05, y_center, 0.06, 0, head_width=0.02, 
                 head_length=0.01, fc='darkgreen', ec='darkgreen')

ax4.set_xlim(0, 1)
ax4.set_ylim(0, 1)
ax4.set_title('Figure 4.4: 3-PPE Detection Pipeline Flow', 
              fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('Figure_4_4_Detection_Pipeline_3_Classes.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n=== ARCHITECTURE SUMMARY ===")
print("Figure 4.1: Development Environment and Technology Stack")
print("- Multi-layer technology stack with cloud training capabilities")
print("- Production-ready deployment options")

print("\nFigure 4.2: Dataset Statistics (3 Main PPE Classes)")
print(f"- Total annotations: {total_annotations:,}")
print(f"- Focus on helmet ({total_counts[0]:,}), vest ({total_counts[1]:,}), mask ({total_counts[2]:,})")
print(f"- Training/Validation/Test: {sum(train_counts):,}/{sum(valid_counts):,}/{sum(test_counts):,}")

print("\nFigure 4.3: Flask Application Architecture")
print("- Client Layer: Web interfaces for 3-PPE detection")
print("- Flask Routes: Authentication and detection endpoints") 
print("- Authentication: Secure user management")
print("- Detection Layer: YOLOv8 integration for helmet/vest/mask detection")
print("- Database Layer: PostgreSQL with user and session management")
print("- Storage: File system for uploads and templates")

print("\nFigure 4.4: 3-PPE Detection Pipeline")
print("- Input: Video/webcam capture")
print("- Processing: YOLOv8 detection focused on helmet, vest, mask")
print("- Output: Compliance evaluation and visual feedback")

print("\n=== ALL FIGURES GENERATED FOR 3-PPE CLASSES ===")
print("Files created:")
print("- Figure_4_1_Technology_Stack.png")
print("- Figure_4_2_Dataset_Statistics_3_Classes.png") 
print("- Figure_4_3_Flask_Architecture.png")
print("- Figure_4_4_Detection_Pipeline_3_Classes.png")
