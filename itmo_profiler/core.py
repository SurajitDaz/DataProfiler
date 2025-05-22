
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pdfkit

def generate_report_from_excel(excel_path, output_html="report.html", output_pdf="report.pdf"):
    df = pd.read_excel(excel_path)
    numeric_cols = df.select_dtypes(include='number').columns
    summary_stats = df[numeric_cols].describe().transpose().round(2)
    summary_html = summary_stats.to_html(classes="summary", border=0)

    def create_html(plots):
        return f"""<!DOCTYPE html>
<html>
<head>
<title>Data Report</title>
<meta charset="utf-8">
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<style>
body {{
    font-family: Arial;
    padding: 20px;
    max-width: 1000px;
    margin: auto;
}}
body::before {{
    content: "ITMO InfoChemistry";
    font-size: 80px;
    color: rgba(150, 150, 150, 0.08);
    position: fixed;
    top: 40%;
    left: 10%;
    transform: rotate(-30deg);
    z-index: -1;
    white-space: nowrap;
}}
</style>
</head>
<body>
<h1>ITMO InfoChemistry Report</h1>
<h2>Summary</h2>
{summary_html}
{"".join(plots)}
</body>
</html>"""

    figs = []
    for col in numeric_cols:
        figs.append(px.histogram(df, x=col, nbins=30).to_html(full_html=False, include_plotlyjs='cdn'))
    html = create_html(figs)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)

    try:
        pdfkit.from_file(output_html, output_pdf)
        print(f"PDF saved to: {output_pdf}")
    except Exception as e:
        print("PDF generation failed:", e)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("excel_path", help="Path to Excel file")
    parser.add_argument("--out_html", default="report.html")
    parser.add_argument("--out_pdf", default="report.pdf")
    args = parser.parse_args()
    generate_report_from_excel(args.excel_path, args.out_html, args.out_pdf)
