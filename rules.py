
class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3
    WHITE = 4

def latest_financial_index(data: dict):
    """
    Determine the index of the latest standalone financial entry in the data.
    """
    for index, financial in enumerate(data.get("financials", [])):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0

def total_revenue(data: dict, financial_index: int):
    """
    Calculate the total revenue from the financial data at the given index.
    """
    try:
        return data['financials'][financial_index]['pnl']['lineItems']['netRevenue']
    except (KeyError, IndexError):
        return 0.0

def total_borrowing(data: dict, financial_index: int):
    """
    Calculate the ratio of total borrowings to total revenue for the financial data at the given index.
    """
    try:
        total_revenue_value = total_revenue(data, financial_index)
        total_borrowings = (
            data['financials'][financial_index]['bs']['lineItems']['longTermBorrowings'] +
            data['financials'][financial_index]['bs']['lineItems']['shortTermBorrowings']
        )
        return total_borrowings / total_revenue_value if total_revenue_value else 0
    except (KeyError, IndexError):
        return 0.0

def iscr(data: dict, financial_index: int):
    """
    Calculate the ISCR (Interest Service Coverage Ratio) value.
    """
    try:
        ebit = data['financials'][financial_index]['pnl']['lineItems']['ebit']
        finance_costs = data['financials'][financial_index]['pnl']['lineItems']['financeCosts']
        return ebit / finance_costs if finance_costs else 0.0
    except (KeyError, IndexError):
        return 0.0

def total_revenue_5cr_flag(data: dict, financial_index: int):
    """
    Determine the flag color based on the total revenue.
    """
    return FLAGS.GREEN if total_revenue(data, financial_index) >= 50000000 else FLAGS.RED

def get_iscr_flag(data: dict, financial_index: int):
    """
    Determine the flag color based on the ISCR value.
    """
    return FLAGS.GREEN if iscr(data, financial_index) >= 1.5 else FLAGS.RED

def borrowing_to_revenue_flag(data: dict, financial_index: int):
    """
    Determine the flag color based on the ratio of total borrowings to total revenue.
    """
    return FLAGS.GREEN if total_borrowing(data, financial_index) <= 0.25 else FLAGS.AMBER
