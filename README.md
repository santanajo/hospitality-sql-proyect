# Hospitality SQL Project

## From Real Hospitality Tickets to Data Insights

This project is a real-world sales analysis based on hospitality data collected from daily operations in a hotel environment.
The goal was to take raw information from physical sales tickets, organize it into a structured dataset, clean and standardize the data, store it in a SQLite database, and analyze it using SQL and Python.

Repository:  
https://github.com/santanajo/hospitality-sql-proyect

---

## Project Overview

This project analyzes real sales data from two hospitality venues:
- **Lemuels** — hotel bar
- **Coburt** — breakfast venue

The dataset includes **787 real sales records** manually collected from physical tickets and transformed into a structured format for analysis.

The project focuses on identifying:
- Best-selling drinks
- Revenue by venue
- Sales patterns by hour
- Operational insights for hospitality planning
- Data cleaning and standardization issues

---

## Why This Project Matters

Hospitality operations change every day. Guest volume, time of day, venue type, weather, and service demand can all affect sales.

This project shows how operational data can be used to better understand demand patterns and support better business decisions, such as:
- Preparing the right amount of coffee stock
- Understanding peak service hours
- Identifying high-demand products
- Comparing sales performance across venues
- Turning daily operations into measurable insights

---

## Dataset

The dataset was created from real hospitality sales tickets.

### Dataset characteristics
- **787 sales records**
- Data collected manually from physical paper tickets
- Includes drinks, coffee, tea, soft drinks, alcoholic drinks, and other hospitality products
- Covers sales from **March 2026**
- Data cleaned and standardized before analysis

Files included:
- `Hotel_sales.csv` — original structured dataset
- `Hotel_sales_clean.csv` — cleaned dataset
- `HOSPITALITY_coffee.db` — SQLite database

---

## Tools and Technologies Used

- **Python 3**
- **SQLite3**
- **SQL**
- **Pandas**
- **Matplotlib**
- **VS Code**
- **Git / GitHub**

---

## Workflow

1. **Data Collection** — Sales data collected from real physical tickets
2. **Data Entry** — Ticket data manually entered and organized into CSV format
3. **Data Cleaning** — Product names, venues, dates standardized with Python & Pandas
4. **Database Creation** — SQLite database created to store the sales data
5. **SQL Analysis** — Queries used to analyze sales volume, revenue and time patterns
6. **Visualization** — Python and Matplotlib used to create visual charts
7. **Publishing** — Full project uploaded to GitHub as part of a data portfolio

---

## Key Insights

- 🏆 Top selling drink: **Americano — 257 units**
- 💰 Lemuels total revenue: **€630**
- 🕘 Busiest hour: **09:00 at Coburt — 193 sales**
- 📅 Busiest day: **25/03/2026 — 245 sales**
- 787 transactions analysed across both venues

---

## Project Structure

```text
hospitality-sql-proyect/
├── Hotel_sales.csv
├── Hotel_sales_clean.csv
├── HOSPITALITY_coffee.db
├── clean_data.py
├── create_database.py
├── create_sales_table.py
├── fix_dates.py
├── import_csv.py
├── insert_sales_data.py
├── query_sales.py
├── visualizations.py
├── top_drinks.png
├── sales_by_location.png
└── README.md
```

