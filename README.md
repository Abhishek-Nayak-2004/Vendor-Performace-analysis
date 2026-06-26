# Vendor Performance Analysis

A data analysis project that examines vendor and inventory performance for a retail/wholesale business using SQL, Python, and statistical analysis. The project spans two notebooks — one for data preparation (EDA) and one for in-depth performance analysis.

---

## Project Overview

This project analyzes an inventory database (`inventory.db`) containing purchase records, sales data, vendor invoices, and pricing information. The goal is to uncover actionable business insights around vendor profitability, inventory efficiency, and procurement strategy.

---

## Project Structure

```
├── Exploratory_Data_Analysis.ipynb   # Data extraction, cleaning & feature engineering
├── Vender_performace_analysis.ipynb  # Business analysis, visualizations & statistics
├── inventory.db                      # SQLite database (purchases, sales, vendor invoices)
└── README.md
```

---

## Notebooks

### 1. `Exploratory_Data_Analysis.ipynb`
- Connects to the SQLite database and explores all available tables
- Joins `purchases`, `purchase_prices`, `sales`, and `vendor_invoice` tables using multi-CTE SQL queries
- Engineers key business metrics:
  - **Gross Profit** = Total Sales Dollars − Total Purchase Dollars
  - **Profit Margin** = (Gross Profit / Total Sales Dollars) × 100
  - **Stock Turnover** = Total Sales Quantity / Total Purchase Quantity
  - **Sales-to-Purchase Ratio**
- Saves the final enriched summary table back to the database as `vendor_sales_summary`

### 2. `Vender_performace_analysis.ipynb`
- Loads `vendor_sales_summary` and performs full EDA (distributions, box plots, correlation heatmap)
- Answers key business questions:
  - Which vendors and brands have the highest sales performance?
  - Which vendors contribute most to total procurement spend (Pareto analysis)?
  - Does bulk purchasing reduce unit price?
  - Which vendors have low inventory turnover (slow-moving stock)?
  - How much capital is locked in unsold inventory per vendor?
  - Is there a statistically significant difference in profit margins between top and low-performing vendors?

---

## Key Analyses & Visualizations

| Analysis | Method |
|---|---|
| Distribution & outlier detection | Histograms, KDE plots, Box plots |
| Feature correlation | Heatmap (Seaborn) |
| Top vendors & brands by sales | Horizontal bar charts |
| Procurement concentration | Pareto chart + Donut chart |
| Brands needing pricing attention | Scatter plot (low sales, high margin quadrant) |
| Bulk purchase price effect | Order size segmentation (`pd.qcut`) |
| Profit margin comparison | 95% Confidence Intervals + Two-sample T-test |

---

## Statistical Analysis

- **Confidence Intervals (95%)** computed for profit margins of top vs. low-performing vendors using the t-distribution
- **Welch's Two-Sample T-Test** to determine if the difference in profit margins is statistically significant

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| SQLite3 | Database connectivity |
| Matplotlib & Seaborn | Data visualization |
| SciPy | Statistical testing |


## Business Insights Uncovered

- Some products had **negative gross profit**, indicating they were sold below purchase cost
- A **strong correlation (0.999)** was found between purchase quantity and sales quantity, confirming efficient inventory turnover overall
- A small group of vendors accounted for the **majority of procurement spend** (Pareto principle in action)
- Brands with **low sales but high profit margins** were flagged as opportunities for targeted promotions
- Statistical testing revealed a **significant difference** in profit margins between high and low-performing vendors

---

## Scrrenshots
<img width="1169" height="765" alt="image" src="https://github.com/user-attachments/assets/efc9a506-0bfd-4407-966d-e673cae6c3d2" />

<img width="1166" height="458" alt="image" src="https://github.com/user-attachments/assets/e7f0f7cd-d2c5-49ab-a1aa-f3a1137d0500" />

<img width="893" height="671" alt="image" src="https://github.com/user-attachments/assets/b0d3ec47-388e-4dd9-9e3d-3b58eafe1d7d" />

<img width="760" height="449" alt="image" src="https://github.com/user-attachments/assets/58ec779a-4535-48ba-990b-538101bc47e4" />

<img width="1337" height="405" alt="image" src="https://github.com/user-attachments/assets/d91ce590-2cef-44ca-990f-a6086256a1e4" />

<img width="857" height="503" alt="image" src="https://github.com/user-attachments/assets/eddb388b-536d-4f77-93c9-5b7c45dac2f3" />

<img width="909" height="438" alt="image" src="https://github.com/user-attachments/assets/89f9414c-2d92-4086-aae9-8073cdce7d08" />



##  Author

**Abhishek Nayak**  
GitHub: [github.com/Abhishek-Nayak-2004](https://github.com/Abhishek-Nayak-2004)
