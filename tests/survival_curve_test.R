# Survival Curve Test
# Cornell Football Fanatics - NFLPA Competition
# Appendix G

wr_survival <- read.csv('/Users/duncanpark/Desktop/STSCI 4981/CSVs/WRs/WR_TABLE_1.csv')

library(lme4)

wr_surv_model <- lmer(pct ~ week * quartile + (1 | quartile), data = wr_survival)
summary(wr_surv_model)
