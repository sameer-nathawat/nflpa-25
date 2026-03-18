"""
Efficiency Decline Graph
Cornell Football Fanatics - NFLPA Competition
Appendix C
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assumes wr_stats is loaded from feature_engineering.py
# from feature_engineering import wr_stats

wr_stats['yards_per_reception'] = wr_stats['receiving_yards'] / wr_stats['receptions'].replace(0, np.nan)

player_workload = wr_stats.groupby('pfr_id')['targets'].mean().reset_index()
median_workload = player_workload['targets'].median()
high_workload_players = player_workload[player_workload['targets'] >= median_workload]['pfr_id']

wr_stats = wr_stats[wr_stats['pfr_id'].isin(high_workload_players)]

efficiency = wr_stats.groupby('week').agg({
    'yards_per_reception': 'mean',
    'receiving_epa': 'mean'
}).reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(efficiency['week'], efficiency['yards_per_reception'], marker='o', color='#e74c3c')
ax2.plot(efficiency['week'], efficiency['receiving_epa'], marker='o', color='#e74c3c')

ax1.set_xlabel('Week')
ax1.set_ylabel('Yards per Reception')
ax1.set_title('High Target WRs: Yards per Reception by Week')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(1, 18)

ax2.set_xlabel('Week')
ax2.set_ylabel('EPA per Play')
ax2.set_title('High Target WRs: EPA by Week')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1, 18)

plt.tight_layout()
plt.show()
