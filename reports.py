from collections import defaultdict

def generate_monthly_summary(manager):
    summary = defaultdict(float)
    for e in manager.expenses:
        month = e.date[:7]
        summary[month] += e.amount
    
    print("\n--- Monthly Summary ---")
    for month, total in sorted(summary.items()):
        print(f"{month}: ${total:.2f}")

def generate_category_breakdown(manager):
    breakdown = defaultdict(float)
    total_all = 0
    for e in manager.expenses:
        breakdown[e.category] += e.amount
        total_all += e.amount

    print("\n--- Category Breakdown ---")
    if not total_all:
        print("No data available.")
        return

    for cat, total in breakdown.items():
        percentage = (total / total_all) * 100
        bar = "#" * int(percentage // 5)
        budget_str = ""
        if cat in manager.budgets:
            budget_str = f" / Budget: ${manager.budgets[cat]:.2f}"
            if total > manager.budgets[cat]:
                budget_str += " [OVER BUDGET!]"
        
        print(f"{cat:<15}: ${total:<8.2f} ({percentage:>5.1f}%) {bar} {budget_str}")

def generate_trend_analysis(manager):
    print("\n--- Trend & Predictions ---")
    if len(manager.expenses) < 2:
        print("Insufficient historical data to calculate trends.")
        return

    sorted_expenses = sorted(manager.expenses, key=lambda x: x.date)
    summary = defaultdict(float)
    for e in sorted_expenses:
        month = e.date[:7]
        summary[month] += e.amount

    months = sorted(list(summary.keys()))
    totals = [summary[m] for m in months]

    print(f"Tracked Period: {months[0]} to {months[-1]}")
    print(f"Average Monthly Spend: ${sum(totals)/len(totals):.2f}")
    
    recent_months = totals[-3:]
    predicted = sum(recent_months) / len(recent_months)
    print(f"Predicted Next Month's Spending: ${predicted:.2f}")