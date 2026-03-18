"""
Feature Engineering
Cornell Football Fanatics - NFLPA Competition
Appendix A
"""

import pandas as pd
import numpy as np

wr_stats = pd.read_csv("/Users/sameer/Documents/Sports Analytics Club/NFLPA Project/wrs_2021_to_2024.csv")
bye_weeks = pd.read_csv("/Users/sameer/Documents/Sports Analytics Club/NFLPA Project/bye_weeks.csv")

week1_players = wr_stats[wr_stats['week'] == 1][['pfr_id', 'season']].drop_duplicates()
wr_stats = wr_stats.merge(week1_players, on=['pfr_id', 'season'])

early_season_workload = wr_stats[wr_stats['week'].isin([1, 2, 3, 4])].groupby(['pfr_id', 'season'])['targets'].mean().reset_index()
early_season_workload['quartile'] = pd.qcut(early_season_workload['targets'], q=4, labels=['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)'])

wr_stats = wr_stats.merge(early_season_workload[['pfr_id', 'season', 'quartile']], on=['pfr_id', 'season'])

all_combos = wr_stats[['pfr_id', 'season', 'quartile']].drop_duplicates()
all_weeks = pd.DataFrame({'week': range(1, 19)})
complete_data = all_combos.merge(all_weeks, how='cross')

complete_data = complete_data.merge(
    wr_stats[['pfr_id', 'season', 'week', 'targets']],
    on=['pfr_id', 'season', 'week'],
    how='left'
)

bye_weeks = bye_weeks.rename(columns={'year': 'season'})
complete_data = complete_data.merge(
    wr_stats[['pfr_id', 'season', 'team']].drop_duplicates(),
    on=['pfr_id', 'season']
)

complete_data = complete_data.merge(bye_weeks, on=['season', 'team'], how='left')

complete_data['is_bye'] = complete_data['week'] == complete_data['bye_week']
complete_data['played'] = ~complete_data['targets'].isna()
complete_data['is_injury'] = (complete_data['targets'].isna()) & (~complete_data['is_bye'])
