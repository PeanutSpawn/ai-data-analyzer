import os
import pandas as pd
from google import genai


def analyze_sales(df):
    df["sales"] = df["quantity"] * df["unit_price"]
    total_orders = len(df)
    total_items = df["quantity"].sum()
    total_sales = df["sales"].sum()

    top_product = (
        df.groupby("product")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    product_sales = (
        df.groupby("product")[["sales", "quantity"]]
        .sum()
        .sort_values(by="sales", ascending=False)
        .reset_index()
    )
    product_sales["average_price"] = product_sales["sales"] / product_sales["quantity"]
   

    countries = df["country"].nunique()
    average_order_value = total_sales / total_orders
    
    sales_by_country = (
         df.groupby("country")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"quantity": "items_sold"})

    )

    sales_value_by_country = (
        df.groupby("country")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"sales": "sales_value"})
    )

    summary = f"""

Sales analysis:

Number of orders: {total_orders}
Total items sold: {total_items}
Total sales: {total_sales}
Number of countries: {countries}
Top-selling product: {top_product}
Sales by country: {sales_by_country.to_string(index=False)}
Sales value by country: {sales_value_by_country.to_string(index=False)}
Average order value: {average_order_value:.2f}
Product sales: {product_sales.to_string(index=False)}
"""

    return summary


df = pd.read_csv("data/sales.csv")

summary = analyze_sales(df)

#print(summary)

prompt = f"""
Analyze the following sales data and write a short summary for a non-technical person. Base your analysis on the provided data.
Do not invent trends, growth, causation, or information that is not supported by the data.
You may identify meaningful patterns and comparisons that are directly visible in the data.
Keep the analysis concise, clear, and useful for a non-technical business reader. Keep the response under 200 words.

{summary}
"""
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)


