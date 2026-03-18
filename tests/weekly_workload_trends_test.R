# Weekly Workload Trends Test
# Cornell Football Fanatics - NFLPA Competition
# Appendix K

library(tidyverse)

wr_wkly_targets <- read.csv('/Users/duncanpark/Desktop/STSCI 4981/CSVs/WRs/WR_TABLE_5.csv')

wr_wkly_targets$week <- as.numeric(wr_wkly_targets$week)
wr_wkly_targets$quartile <- factor(wr_wkly_targets$quartile)

model <- aov(targets ~ quartile * week, data = wr_wkly_targets)
summary(model)

library(broom)

wr_wkly_targets %>%
  group_by(quartile) %>%
  do(tidy(lm(targets ~ week, data = .)))
