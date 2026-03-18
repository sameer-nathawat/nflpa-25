# Efficiency Decline Test
# Cornell Football Fanatics - NFLPA Competition
# Appendix H

wr_2 <- read.csv('/Users/duncanpark/Desktop/STSCI 4981/CSVs/WRs/WR_TABLE_2.csv')

wr_2$week_num <- as.numeric(wr_2$week)

summary(lm(yards_per_reception ~ week_num, data = wr_2))
summary(lm(receiving_epa ~ week_num, data = wr_2))
