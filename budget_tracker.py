import csv
import matplotlib.pyplot as plt
import pandas as pd

budget = dict(Food=dict(budget=200, expenses=[15]), Transportation=dict(budget=400, expenses=[15]),
              Entertainment=dict(budget=350, expenses=[15, 20]), Utilities=dict(budget=500, expenses=[25]))

def budget_view(budget):
    print("\nCurrent Budget and Expenses:\n")
    print(f"{'Category':<15}{'Budget':<10}{'Expenses':<20}{'Total Spent':<15}")
    print("-" * 60)

    total_budget = 0
    total_spent = 0

    for category, details in budget.items():
        total_budget += details["budget"]
        total_spent += sum(details["expenses"])
        print(f"{category:<15}{details['budget']:<10}{', '.join(map(str, details['expenses'])):<20}{sum(details['expenses']):<15}")

    print("-" * 60)
    print(f"{'Total':<15}{total_budget:<10}{'':<20}{total_spent:<15}\n")


def add_expense(cat, expense):
    try:
        if cat not in budget:
            choice = input(f"{cat} not in budget. Do you want to add {cat}? (y/n): ").lower()
            if choice == "y":
                add_budget = int(input("Enter budget: "))
                budget[cat] = {"budget": add_budget, "expenses": [expense]}
                print(f"Added new category: {cat} | Budget: {add_budget}, Expense: {expense}")
            else:
                print(f"{cat} was not added.")
                return
        else:
            amend_choice = input(f"Do you want to amend the budget for {cat}? (y/n): ").lower()
            if amend_choice == "y":
                new_budget = int(input("Enter new budget: "))
                budget[cat]["budget"] = new_budget
                print(f"Updated budget for {cat}: {new_budget}")

            # Add expense
            budget[cat]["expenses"].append(expense)
            print(f"Added expense to {cat}: {expense}")

    except ValueError:
        print("Invalid input. Please try again.")


def save_to_csv(data, filename='budget.csv'):
    try:
        with open(filename, "w", newline="") as data_base:
            if not data:
                print(f"⚠️ No data to save.")
                return

            writer = csv.writer(data_base)
            writer.writerow(['Category', 'Budget', 'Expenses'])
            for k, v in data.items():
                writer.writerow([k, v["budget"], ",".join(map(str, v["expenses"]))])
            print(f"✅ Successfully saved to {filename}")
    except Exception as e:
        print(f"⚠️ An error occurred while saving to {filename}: {e}")

def data_analysis(data):
    try:
        # Load the file
        df = pd.read_csv(data)

        # Convert 'Expenses' to 'Total Expenses'
        df["Total Spent"] = df["Expenses"].apply(lambda x: sum(map(int, x.split(","))) if isinstance(x, str) and x else 0)

        # Drop the original 'Expenses' column
        df.drop(["Expenses"], axis=1, inplace=True)

        # Set index to 'Category'
        df.set_index("Category", inplace=True)

        # Plot Budget vs. Total Expenses
        chart_list = {1:"bar", 2:"pie"}
        print("\n Available Charts:\n")
        for k, v in chart_list.items():
            print(f"{k}. {v.capitalize()} Chart")

        while True:
            try:
                chart_choice = int(input(f"Choose a chart from the list (1-3): ").lower())
                if chart_choice == 1:
                    df.plot(kind='bar', figsize=(10, 6), title="Budget vs Total Expenses", rot=0)
                    plt.xlabel("Category")
                    plt.ylabel("Amount £")
                    plt.tight_layout()
                    plt.grid(axis="y", linestyle="--", alpha=0.7)
                    plt.legend(["Budget", "Total Spent"])
                    plt.show()
                    break

                elif chart_choice == 2:
                    df.plot.pie(y="Total Spent",
                                labels=df.index,
                                autopct="%1.1f%%",
                                shadow=True,
                                startangle=90,
                                figsize=(8, 8),
                                title="Total Spent Distribution")
                    plt.ylabel("")
                    plt.show()
                    break
                else:
                    print("Invalid input. Please enter 1 or 2.")

            except ValueError:
                print("Invalid input. Please try again.")
                continue



    except FileNotFoundError:
        print(f"Error: File {data} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


#save_to_csv(budget)
print(data_analysis('budget.csv'))