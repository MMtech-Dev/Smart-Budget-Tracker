# Smart Budget Tracker

The **Smart Budget Tracker** is a Python-based command-line application that allows users to manage their budgets efficiently. This project showcases skills in Python programming, data visualization, file handling, and report generation.

---

## **Features**

- **View Budget and Expenses**: Get a detailed breakdown of budgets, total expenses, and remaining balances for each category.
- **Add Expenses Dynamically**: Add new categories or update existing ones with specific expenses.
- **Save to CSV**: Save the budget data in a structured `.csv` file for future use.
- **Data Visualization**: Generate bar and pie charts to visualize budget allocation and spending trends.
- **Generate Reports**: Create detailed textual summaries of budgets, expenses, and remaining balances in `.txt` format.

---

## **How to Use It**

1. Clone the repository:
   ```bash
   git clone https://github.com/MMtech-Dev/Smart-Budget-Tracker.git
   cd Smart-Budget-Tracker
   ```

2. Set Up the Virtual Environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. Follow the On-Screen Prompts
   * Choose a menu option:
     * View Budget
     * Add Expense
     * Save Budget to File
     * Analyze Budget
     * Generate Report
     * Exit
   * Input category names, expense amounts, or file names as prompted.

---


## **File Structure**

```
📂 smart-budget-tracker
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
├── main.py                # CLI entry point
├── budget_tracker.py      # Core functions for budget management
├── budget.csv             # Default file for saving budget
├── budget_report.txt      # Default file for saving generated report

```

---

## **Technologies Used**

* Programming Language: Python
* Libraries:
  * pandas: Data manipulation.
  * matplotlib: Data visualization.
  * csv: File handling for budget data.
  * os: File system interaction.


---

## **Example Output**
### CLI Menu

What would you like to do?
1. View Budget
2. Add Expense
3. Save Budget to File
4. Analyze Budget
5. Generate Report
6. Exit

---

## **Generated Report**
Budget Report
==============================
Category: Food
  Budget: £500
  Spent: £300
  Remaining: £200
------------------------------
Category: Transportation
  Budget: £200
  Spent: £50
  Remaining: £150
------------------------------
Overall Summary
  Total Budget: £700
  Total Spent: £350
  Total Remaining: £350
---

## **Future Enhancement**
* Add an API Integration for real-time budget tracking.
* Include date-specific expense tracking.
* Build a web-based version using Flask or Django.

---

## **License**
This project is licensed under the MIT License. Feel free to use and modify it.

---
## **Contact**

Feel free to reach out with any questions or suggestions:
- GitHub: MMtech-Dev https://github.com/MMtech-Dev
- Email: gables.05-cannier@icloud.com

