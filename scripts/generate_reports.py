from datetime import datetime

def generate_report():
    today = datetime.now().strftime("%Y-%m-%d")
    with open("report.html", "w") as f:
        f.write(f"<h1>Daily Report - {today}</h1>")
        f.write("<p>Processed 10 records.</p>")

generate_report()
