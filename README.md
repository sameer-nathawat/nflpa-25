# Analyzing Impact of Workload on Injury Risk and Performance in the NFL

**2025–26 NFLPA Case Competition**
**Cornell Football Fanatics** — Duncan Park & Sameer Nathawat

---

## Overview

This project investigates how workload affects injury risk and performance for NFL 
wide receivers (WRs) and running backs (RBs) over the course of a season, using 
week-by-week data from the 2021–2024 NFL seasons.

We examined whether high-workload players (measured by touches for RBs and targets 
for WRs) experience greater performance decline or increased injury risk as the 
season progresses.

---

## Research Question

> *How does workload affect injury risk and performance for RBs and WRs over the 
> course of a season?*

---

## Key Findings

- **Performance** (yards/touch, EPA/play) remained stable across the season for both 
  RBs and WRs regardless of workload quartile
- **Injury risk** (next-week injury probability) did not differ significantly across 
  touch/target volume bins
- **Survival rates** declined for all quartiles but high-workload players showed no 
  steeper decline than low-workload players
- High-workload RBs and WRs actually showed a small *decrease* in games missed 
  late in the season, potentially reflecting survivor bias or durability effects

Our initial hypothesis was **rejected** — heavier workload does not straightforwardly 
lead to increased injury risk or performance decline.

---

## Methodology

### Data
- Source: [`nflreadpy`](https://nflreadpy.nflverse.com/) Python package
- Scope: All RBs and WRs, 2021–2024 seasons (the complete 18-week format era)

### Workload Definition
| Position | Workload Metric |
|----------|----------------|
| RB       | Touches (rushes + receptions) per game |
| WR       | Targets per game |

### Workload Quartiles
Players are binned into Q1 (Low) through Q4 (High) based on their **Weeks 1–4 
average** touches/targets.

### Visualizations
| # | Graph | Purpose |
|---|-------|---------|
| 1–2 | Survival Curve | % of players still active each week by quartile |
| 3–4 | Efficiency Decline | Weekly yards/touch and EPA for high-workload players |
| 5–6 | Injury Risk Heatmap | Next-week injury rate by workload bin and week |
| 7–8 | Games Missed Distribution | Consecutive games missed by quartile |
| 9–10 | Weekly Workload Trends | Average touches/targets per week by quartile |

### Statistical Tests (R)
| Graph | Test |
|-------|------|
| Survival Curve | Linear mixed-effects model (lme4) |
| Efficiency Decline | Linear regression |
| Injury Risk Heatmap | One-way ANOVA |
| Games Missed | Chi-square test |
| Weekly Workload Trends | Two-way ANOVA |

Significance threshold: **p < 0.05**

---

## Project Structure
```
├── src/            # Python visualization scripts
├── tests/          # R statistical test scripts
├── data/           # Raw and processed CSVs
├── figures/        # Output graphs
└── report/         # Full competition report PDF
```

---

## Setup & Usage

### Python (Visualizations)
```bash
pip install -r requirements.txt
python src/feature_engineering.py   # Build dataset
python src/survival_curve.py        # Generate Figure 1 & 2
# ... etc.
```

### R (Statistical Tests)
```r
# Install dependencies
install.packages(c("lme4", "tidyverse", "broom"))

# Run tests (update CSV paths in each script first)
source("tests/survival_curve_test.R")
```

---

## Requirements

Key Python dependencies found in `requirements.txt`:
- `nflreadpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`

---

## Report

The full competition report is available in [`report/`](report/).

---

## References

1. Mack et al. (2020). Incidence of Lower Extremity Injury in the NFL: 2015–2018. 
   *American Journal of Sports Medicine.*
2. [nflreadpy](https://nflreadpy.nflverse.com/)
3. [Matplotlib](https://matplotlib.org/)
4. [Seaborn](https://seaborn.pydata.org/)
5. [NFL CBA](https://overthecap.com/collective-bargaining-agreement)
```
