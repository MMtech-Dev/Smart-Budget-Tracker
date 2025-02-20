import csv
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import os

# ✅ Budget Dictionary
budget = {
    "Food": {"budget": 200, "expenses": [15]},
    "Transportation": {"budget": 400, "expenses": [15]},
    "Entertainment": {"budget": 350, "expenses": [15, 20]},
    "Utilities": {"budget": 500, "expenses": [25]}
}

# ✅ View Budget
def budget_view():
    return budget  # Returning dictionary for API response

# ✅ Add Expense
def add_expense(category, expense):
    try:
        if category not in budget:
            return {"error": f"{category} not in budget. Add a budget first."}

        budget[category]["expenses"].append(expense)
        return {"message": f"Expense {expense} added to {category}", "budget": budget}

    except ValueError:
        return {"error": "Invalid input. Expense must be a number."}

# ✅ Save Budget to CSV
def save_to_csv(data, filename="budget.csv"):
    try:
        with open(filename, "w", newline="") as data_base:
            if not data:
                return {"error": "No data to save."}

            writer = csv.writer(data_base)
            writer.writerow(["Category", "Budget", "Expenses"])
            for category, details in data.items():
                writer.writerow([category, details["budget"], ",".join(map(str, details["expenses"]))])

        return {"message": f"✅ Successfully saved to {filename}"}

    except Exception as e:
        return {"error": str(e)}

# ✅ Data Analysis (Generate Chart)
def data_analysis(data, chart_choice=1):
    try:
        if not os.path.exists(data):
            return {"error": f"CSV file not found: {data}"}

        df = pd.read_csv(data)

        # Convert 'Expenses' column to 'Total Spent'
        df["Total Spent"] = df["Expenses"].apply(lambda x: sum(map(int, x.split(","))) if isinstance(x, str) and x else 0)

        df.drop(["Expenses"], axis=1, inplace=True)
        df.set_index("Category", inplace=True)

        img_path = os.path.join("static", "analysis_plot.png")

        # Generate Chart
        if chart_choice == 1:
            df.plot(kind='bar', figsize=(10, 6), title="Budget vs Total Expenses", rot=0)
        elif chart_choice == 2:
            df.plot.pie(y="Total Spent", labels=df.index, autopct="%1.1f%%", shadow=True, startangle=90, figsize=(8, 8),
                        title="Total Spent Distribution")
            plt.ylabel("")

        plt.savefig(img_path)
        plt.close()

        if os.path.exists(img_path):
            return img_path  # Return image path for API

        return {"error": "Image not found after saving!"}

    except Exception as e:
        return {"error": str(e)}

# ✅ Generate Budget Report
def generate_report(data, filename="static/budget_report.txt"):
    try:
        total_budget = sum(details["budget"] for details in budget.values())
        total_spent = sum(sum(details["expenses"]) for details in budget.values())
        remaining_budget = total_budget - total_spent

        report_lines = [
            "=== Budget Report ===\n",
            f"Total Budget: £{total_budget}\n",
            f"Total Spent: £{total_spent}\n",
            f"Remaining Budget: £{remaining_budget}\n",
            "=" * 30 + "\n"
        ]

        for category, details in budget.items():
            category_budget = details["budget"]
            category_expenses = sum(details["expenses"])
            category_remaining = category_budget - category_expenses

            report_lines.append(f"Category: {category}\n"
                                f"Budget: £{category_budget}\n"
                                f"Expenses: £{category_expenses}\n"
                                f"Remaining: £{category_remaining}\n"
                                f"{'-' * 30}\n")

        # Save report
        with open(filename, "w") as file:
            file.writelines(report_lines)

        return filename  # Return report file path for API

    except Exception as e:
        return {"error": str(e)}
