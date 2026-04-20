# Vendor-Performace-analysis
Analyzed vendors performance using Python and SQL to extract, clean, and aggregate data, identify top vendors, and uncover sales trends for decision-making.
Here’s a clean, professional **README.md** based on your project:

---

# Vendor Sales Performance Analysis

## Overview

This project analyzes vendor sales performance using **Python and SQL**. It focuses on extracting, transforming, and analyzing purchase, sales, and invoice data to generate meaningful business insights such as profitability, stock turnover, and vendor efficiency.

---

## Project Structure

```
├── data/                      # Raw CSV files
├── logs/                      # Log files
├── ingestion_db.py            # Data ingestion script
├── get_vendor_summary.py      # SQL-based vendor summary generation
├── Exploratory Data Analysis.ipynb
├── Vendor_performance_analysis.ipynb
├── inventory.db               # SQLite database
```

---

## Workflow

### 1. Data Ingestion

* Raw CSV files are loaded into a SQLite database.
* Uses **SQLAlchemy + Pandas**.
* Tables are automatically created from files.

### 2. Data Processing (SQL)

* Multiple tables are joined using **CTEs (Common Table Expressions)**:

  * Freight Summary
  * Purchase Summary
  * Sales Summary

### 3. Key Metrics Calculated

* **Gross Profit**
* **Profit Margin**
* **Stock Turnover**
* **Sales-to-Purchase Ratio**

### 4. Data Analysis & Visualization

* Performed using **Pandas, Matplotlib, Seaborn**
* Identifies:

  * Top-performing vendors
  * Sales trends
  * Inefficient vendors

---

## Key Files Explanation

### `ingestion_db.py`

* Loads all CSV files into SQLite database (`inventory.db`)
* Automates ingestion process
* Includes logging and execution time tracking

### `get_vendor_summary.py`

* Core logic of the project
* Uses SQL queries to:

  * Merge purchase, sales, and invoice data
  * Generate vendor-level summary
  * Compute performance metrics

---

## Tech Stack

* Python (Pandas, Logging)
* SQL (SQLite, CTEs, Aggregations)
* Data Visualization (Matplotlib, Seaborn)

---

## How to Run

```bash
# Step 1: Load data into database
python ingestion_db.py

# Step 2: Generate vendor summary
python get_vendor_summary.py

# Step 3: Run notebooks for analysis
```

---

## Output

* Clean vendor-level dataset with performance metrics
* Visual insights on vendor efficiency and profitability

---

## Use Case

Helps businesses:

* Identify high and low-performing vendors
* Optimize inventory and purchasing decisions
* Improve profit margins through data-driven insights

---

If you want, I can upgrade this into a **resume-level GitHub project (with badges, screenshots, and impact statements)** or make it **ATS-friendly project description**.
