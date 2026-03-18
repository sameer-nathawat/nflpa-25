# Injury Risk Heatmap Test
# Cornell Football Fanatics - NFLPA Competition
# Appendix I

df_injured_next_week_wr <- read.csv('/Users/duncanpark/Desktop/STSCI 4981/CSVs/WRs/WR_TABLE_3.csv')
library(tidyverse)

long_2 <- df_injured_next_week_wr %>%
  pivot_longer(-target_bin, names_to = "week", values_to = "value") %>%
  mutate(week = as.numeric(week))

# ANOVA Model Summary
summary(aov(value ~ target_bin, data = long_2))
