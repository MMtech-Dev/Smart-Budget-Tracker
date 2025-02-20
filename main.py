import budget_tracker as br
import os
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)


### 🔹 Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Smart Budget Tracker API",
                    "usage": "Use /budget, /expenses, /add_expense, /data_analysis, or /report"}), 200


### 🔹 View Budget Route
@app.route("/budget")
def view_budget():
    return jsonify(br.budget) if br.budget else jsonify({"error": "No budget data available"}), 200


### 🔹 View Expenses Route
@app.route("/expenses", methods=["GET"])
def view_expenses():
    """Retrieve recorded expenses categorized by budget type."""
    recorded_expenses = {category: details["expenses"] for category, details in br.budget.items() if
                         "expenses" in details}

    return jsonify(recorded_expenses) if recorded_expenses else jsonify({"error": "No expense data available"}), 200


### 🔹 Add Expense Route
@app.route("/add_expense", methods=["POST"])
def create_expense():
    """API route to add a new expense"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        category = data.get("category")
        expense = data.get("expense")

        if not category or expense is None:
            return jsonify({"error": "Invalid input. Category and expense are required."}), 400
        if not isinstance(expense, int) or expense < 0:
            return jsonify({"error": "Expense must be a positive number."}), 400

        br.add_expense(category, expense)
        return jsonify({"message": "Expense added successfully!", "category": category, "expense": expense}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


### 🔹 Data Analysis Route (Generates Graphs)
@app.route("/data_analysis", methods=["GET"])
def data_analysis():
    """Run data analysis and return a download link to the generated image."""
    filename = request.args.get('file', 'budget.csv')  # Default file
    chart_type = int(request.args.get("chart", 1))  # Default to bar chart

    img_path = br.data_analysis(filename, chart_type)

    if img_path and os.path.exists(img_path):
        return jsonify({
            "message": "Data analysis completed!",
            "image_url": f"http://127.0.0.1:5000/static/analysis_plot.png"
        }), 200
    else:
        return jsonify({"error": f"File {filename} not found or failed to generate"}), 404


### 🔹 Report Generation Route (Generates Text Report)
@app.route("/report", methods=["GET"])
def report():
    """Generate a budget report and provide a download link."""
    data_file = request.args.get('file', 'budget.csv')  # Input data file
    report_filename = "static/budget_report.txt"  # Output report file

    report_path = br.generate_report(data_file, report_filename)

    if report_path and os.path.exists(report_filename):
        return jsonify({
            "message": "File successfully generated!",
            "file_url": f"http://127.0.0.1:5000/static/budget_report.txt"
        }), 200
    else:
        return jsonify({"error": f"Report generation failed for {report_filename}"}), 500


### 🔹 Direct Report Download Route
@app.route("/download_report", methods=["GET"])
def download_report():
    """Allow users to download the generated report."""
    report_filename = "static/budget_report.txt"

    if os.path.exists(report_filename):
        return send_file(report_filename, as_attachment=True)
    else:
        return jsonify({"error": "Report not found"}), 404


### 🔹 Run Flask App
if __name__ == '__main__':
    print("🚀 Starting Flask Web Application on http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)
