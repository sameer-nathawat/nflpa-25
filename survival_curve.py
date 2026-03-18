"""
Survival Curve Graph
Cornell Football Fanatics - NFLPA Competition
Appendix B
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assumes complete_data is loaded from feature_engineering.py
# from feature_engineering import complete_data

survival_rates = []

for quartile in ['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)']:
    q_data = complete_data[complete_data['quartile'] == quartile]
    total = q_data[['pfr_id', 'season']].drop_duplicates().shape[0]

    for week in range(1, 19):
        still_playing = q_data[(q_data['week'] == week) & (q_data['played'] == True)]
        count = still_playing[['pfr_id', 'season']].drop_duplicates().shape[0]
        survival_rates.append({
            'week': week,
            'quartile': quartile,
            'pct': (count / total) * 100
        })

survival_df = pd.DataFrame(survival_rates)

# Plot
fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#2ecc71', '#f39c12', '#e67e22', '#e74c3c']

for i, quartile in enumerate(['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)']):
    data = survival_df[survival_df['quartile'] == quartile]
    ax.plot(data['week'], data['pct'], marker='o', label=quartile, color=colors[i])

ax.set_xlabel('Week')
ax.set_ylabel('% Still Playing')
ax.set_title('WR Survival Curve by Target Workload')
ax.legend(title='Target Quartile')
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 100)
ax.set_xlim(1, 18)
ax.set_xticks(range(1, 19))

plt.tight_layout()
plt.show()
