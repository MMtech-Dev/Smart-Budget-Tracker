import budget_tracker as br
import os

if __name__ == '__main__':

    def display_menu():
        print("\nWhat would you like to do?")
        print("1. View Budget")
        print("2. Add Expense")
        print("3. Save Budget to File")
        print("4. Analyse Budget")
        print("5. Generate Summary Report")
        print("6. Exit")

    while True:
        display_menu()

        # Handle menu choice input
        try:
            display_menu_choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("⚠️Invalid input. Please enter a number between 1 and 6.")
            continue

        try:
            if display_menu_choice == 1:
                print("\n📊 Viewing the current budget...\n")
                br.budget_view(br.budget)

            elif display_menu_choice == 2:
                category = input("Enter category: ")
                try:
                    expenses = int(input("Enter expenses: "))
                except ValueError:
                    print("⚠️ Invalid expense amount, Please enter a number.")
                    continue
                print("\n💸 Adding a new expense...\n")
                br.add_expense(category, expenses)

            elif display_menu_choice == 3:
                filename = input("Enter filename (default: budget.csv): ") or "budget.csv"
                print("\n💾 Saving budget to file...\n")
                br.save_to_csv(br.budget, filename=filename)
                print(f"Saved budget to file: {filename}")

            elif display_menu_choice == 4:
                filename = input("Enter filename (default: budget.csv): ") or "budget.csv"
                if not os.path.exists(filename):
                    print(f"File {filename} doesn't exist.")
                    continue
                print("\n📊 Analysing budget...\n")
                br.data_analysis(filename)

            elif display_menu_choice == 5:
                filename = input("Enter filename (default: budget_report.txt): ") or "budget_report.txt"
                if not os.path.exists(filename):
                    print(f"File {filename} doesn't exist.")
                    continue
                print("\nGenerating summary report...\n")
                br.generate_report(br.budget, filename)

            elif display_menu_choice == 6:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")





