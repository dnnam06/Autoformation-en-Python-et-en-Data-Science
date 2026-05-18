import matplotlib.pyplot as plt
import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from students_analysis.functions_students import ranking

students = [
    {"id": "SV001", "name": "Nguyễn Văn An", "age": 20, "gpa": 16.23},
    {"id": "SV002", "name": "Trần Thị Bích Ngọc", "age": 21, "gpa": 17.12},
    {"id": "SV003", "name": "Lê Văn Hùng", "age": 22, "gpa": 14.67},
    {"id": "SV004", "name": "Phạm Minh Tuấn", "age": 20, "gpa": 11.43},
    {"id": "SV005", "name": "Vũ Thị Hòa", "age": 23, "gpa": 12.89},
    {"id": "SV006", "name": "Đỗ Quốc Khánh", "age": 19, "gpa": 8.79},
    {"id": "SV007", "name": "Nguyễn Thị Mai", "age": 21, "gpa": 9.99},
    {"id": "SV011", "name": "Dương Nhật Nam", "age": 19, "gpa": 15.99},
    {"id": "SV008", "name": "Bùi Văn Nam", "age": 22, "gpa": 12.45},
    {"id": "SV009", "name": "Hoàng Thị Thu Trang", "age": 20, "gpa": 4.08},
    {"id": "SV010", "name": "Trịnh Văn Cường", "age": 23, "gpa": 15.5},
]

df = pd.DataFrame(students)

# Create a new column
df["mention"] = df["gpa"].apply(ranking)

# Count students by ranking
mention_counts = df["mention"].value_counts()

print(mention_counts)

# =========================================================
# BAR CHART
# =========================================================

plt.figure(figsize=(8, 5))

plt.bar(
    mention_counts.index,
    mention_counts.values
)

plt.title("Répartition des étudiants par mention")

plt.xlabel("Mention")

plt.ylabel("Nombre d'étudiants")

plt.grid(axis='y')

plt.savefig('graph/column_chart.png', dpi=300, bbox_inches='tight')

plt.show()