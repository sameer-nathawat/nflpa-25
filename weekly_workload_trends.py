"""
Weekly Workload Trends Graph
Cornell Football Fanatics - NFLPA Competition
Appendix F
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assumes wr_stats is loaded from feature_engineering.py
# from feature_engineering import wr_stats

wr_stats_filtered = wr_stats[wr_stats['targets'] > 0]

target_avg_by_week = wr_stats_filtered.groupby(['week', 'quartile'])['targets'].mean().reset_index()

fig, ax = plt.subplots(figsize=(16, 7))
colors = ['#2ecc71', '#f39c12', '#e67e22', '#e74c3c']

for i, quartile in enumerate(['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)']):
    data = target_avg_by_week[target_avg_by_week['quartile'] == quartile]
    ax.plot(data['week'], data['targets'], marker='o', label=quartile, color=colors[i], linewidth=2)

ax.set_xlabel('Week')
ax.set_ylabel('Average Targets')
ax.set_title('Average Targets by Week: Target Quartiles')
ax.legend(title='Target Quartile')
ax.grid(True, alpha=0.3)
ax.set_xlim(1, 18)
ax.set_xticks(range(1, 19))

plt.tight_layout()
plt.show()
