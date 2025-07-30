import pandas as pd
from fpdf import FPDF

# Step 1: Load data
data = pd.read_csv("C:/Users/misba/OneDrive/Desktop/sales_data.csv")
data.columns = data.columns.str.strip()

# Step 2: Analyze data
total_revenue = data["Revenue"].sum()
average_revenue = data["Revenue"].mean()
max_revenue = data["Revenue"].max()
top_product = data.loc[data["Revenue"].idxmax(), "Product"]

# Step 3: Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(200, 10, f"Total Revenue: Rs{total_revenue}", ln=True)
pdf.cell(200, 10, f"Average Revenue: Rs{average_revenue:.2f}", ln=True)
pdf.cell(200, 10, f"Maximum Revenue: Rs{max_revenue}", ln=True)
pdf.cell(200, 10, f"Top Selling Product: {top_product}", ln=True)

# Step 4: Save PDF
pdf.output("sales_report.pdf")

print("PDF report generated: sales_report.pdf")
