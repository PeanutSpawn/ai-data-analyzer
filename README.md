# AI Data Analyzer

A small Python project that combines **Pandas** and **Google Gemini API** to analyze sales data and generate a concise business-oriented summary.

The project demonstrates a simple workflow:

**CSV → Pandas → Data Analysis → Gemini API → Business Summary**

## Project Overview

The application reads sales data from a CSV file, calculates key sales metrics using Pandas, and sends the results to Google Gemini.

Gemini then transforms the calculated data into a short, easy-to-understand summary for a non-technical business reader.

The goal is not to let the AI calculate everything from raw data, but to use Python for reliable calculations and AI for communicating the results.

## What the Project Does

The analyzer calculates:

* total number of orders
* total number of items sold
* total sales value
* average order value
* number of countries
* top-selling product by quantity
* sales by country
* sales value by country
* product sales and quantities
* average selling price per product

The calculated results are then provided to Gemini, which generates a concise business summary.

## Technologies

* **Python**
* **Pandas**
* **Google Gemini API**
* **CSV**
* **Git / GitHub**

## Project Structure

```text
ai-data-analyzer/
│
├── data/
│   └── sales.csv
│
├── src/
│   └── analyzer.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

The `.venv` directory is used for the local Python virtual environment and is excluded from Git.

## Example Data

The project uses a small sales dataset containing:

* order information
* customer names
* products
* product categories
* quantities
* unit prices
* countries

A calculated `sales` value is created from:

```text
quantity × unit_price
```

## Example Output

The application produces a business-oriented summary such as:

> Across 10 orders, total sales reached 10,100 with 18 items sold, resulting in an average order value of 1,010.

The generated summary can highlight differences between countries, products, sales volume and sales value.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/PeanutSpawn/ai-data-analyzer.git
cd ai-data-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set the Gemini API key

The application expects the API key to be available as an environment variable.

In Git Bash:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

The API key is intentionally not stored in the project source code or repository.

### 5. Run the analyzer

From the project root:

```bash
python src/analyzer.py
```

The generated AI summary will be printed in the terminal.

## Architecture

```text
sales.csv
    │
    ▼
  Pandas
    │
    ▼
Calculated metrics
    │
    ▼
   Prompt
    │
    ▼
Gemini API
    │
    ▼
Business summary
```

## Why This Approach?

The project separates **data processing** from **AI-generated communication**.

Pandas is responsible for calculations such as totals, averages and grouping.

The Gemini API receives these calculated results and turns them into a readable business summary.

This makes the workflow more controlled than simply sending raw data to an LLM and asking it to perform the entire analysis.

## Possible Future Improvements

* support larger CSV datasets
* add data validation
* detect unusual values or potential anomalies
* generate reports as `.txt` or `.html`
* add charts and visualizations
* allow users to ask questions about the dataset
* add automated tests
* improve error handling for API failures
* build a simple web interface

## Project Purpose

This project was created as a practical demonstration of combining **Python data analysis, APIs and LLMs** to solve a small business-oriented problem.
