"""
Injury Risk Heatmap Graph
Cornell Football Fanatics - NFLPA Competition
Appendix D
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assumes wr_stats and complete_data are loaded from feature_engineering.py
# from feature_engineering import wr_stats, complete_data

target_bins = [5, 8, 11, 100]
target_labels = ['5-8', '8-11', '11+']
wr_stats['target_bin'] = pd.cut(wr_stats['targets'], bins=target_bins, labels=target_labels, include_lowest=True)

next_week = complete_data[['pfr_id', 'season', 'week', 'is_injury']].copy()
next_week['prev_week'] = next_week['week'] - 1
next_week = next_week.rename(columns={'is_injury': 'injured_next_week'})

heatmap_data = wr_stats.merge(
    next_week[['pfr_id', 'season', 'prev_week', 'injured_next_week']],
    left_on=['pfr_id', 'season', 'week'],
    right_on=['pfr_id', 'season', 'prev_week'],
    how='left'
)

rates = heatmap_data.groupby(['week', 'target_bin']).agg({
    'injured_next_week': ['sum', 'count']
}).reset_index()

rates.columns = ['week', 'target_bin', 'injured', 'total']
rates['rate'] = rates.apply(
    lambda row: (row['injured'] / row['total']) * 100 if row['total'] > 0 else np.nan,
    axis=1
)

heatmap_pivot = rates.pivot(index='target_bin', columns='week', values='rate')
heatmap_pivot = heatmap_pivot.reindex(target_labels)

fig, ax = plt.subplots(figsize=(16, 6))
sns.heatmap(heatmap_pivot, annot=True, fmt='.1f', cmap='YlOrRd',
            cbar_kws={'label': 'Injury Rate (%)'}, ax=ax)

ax.set_xlabel('Week')
ax.set_ylabel('Weekly Targets')
ax.set_title('% of WRs Injured Following Week')

plt.tight_layout()
plt.show()
