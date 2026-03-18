"""
Games Missed Distribution Graph
Cornell Football Fanatics - NFLPA Competition
Appendix E
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assumes complete_data is loaded from feature_engineering.py
# from feature_engineering import complete_data

q3_data = complete_data[complete_data['quartile'] == 'Q3']
q4_data = complete_data[complete_data['quartile'] == 'Q4 (High)']

# --- Q4 injury stretches ---
q4_data = q4_data.sort_values(['pfr_id', 'season', 'week'])
q4_injury_stretches = []

for (pfr_id, season), group in q4_data.groupby(['pfr_id', 'season']):
    consecutive = 0
    for _, row in group.iterrows():
        if row['is_injury']:
            consecutive += 1
        else:
            if consecutive > 0:
                q4_injury_stretches.append(consecutive)
            consecutive = 0
    if consecutive > 0:
        q4_injury_stretches.append(consecutive)

# --- Q3 injury stretches ---
q3_data = q3_data.sort_values(['pfr_id', 'season', 'week'])
q3_injury_stretches = []

for (pfr_id, season), group in q3_data.groupby(['pfr_id', 'season']):
    consecutive = 0
    for _, row in group.iterrows():
        if row['is_injury']:
            consecutive += 1
        else:
            if consecutive > 0:
                q3_injury_stretches.append(consecutive)
            consecutive = 0
    if consecutive > 0:
        q3_injury_stretches.append(consecutive)

fig, ax = plt.subplots(figsize=(12, 7))

if len(q4_injury_stretches) > 0 and len(q3_injury_stretches) > 0:
    max_stretch = max(max(q4_injury_stretches), max(q3_injury_stretches))
    bins = range(1, max_stretch + 2)

    ax.hist([q4_injury_stretches, q3_injury_stretches], bins=bins,
            label=['Q4 (High)', 'Q3'],
            color=['#e74c3c', '#e67e22'], alpha=0.7, edgecolor='black')

    ax.set_xlabel('Consecutive Games Missed')
    ax.set_ylabel('Number of Injury Instances')
    ax.set_title('Games Missed Distribution: Q4 vs Q3 Target WRs')
    ax.legend()

plt.tight_layout()
plt.show()
