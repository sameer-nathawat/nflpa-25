# Games Missed Distribution Test
# Cornell Football Fanatics - NFLPA Competition
# Appendix J

missed_games_consec_WR <- read.csv('/Users/duncanpark/Desktop/STSCI 4981/CSVs/WRs/WR_TABLE_4.csv')
tab2 <- xtabs(count ~ quartile + games_missed, data = missed_games_consec_WR)
tab2

chisq.test(tab2)
