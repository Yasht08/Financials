from rules import latest_financial_index, get_iscr_flag, total_revenue_5cr_flag, borrowing_to_revenue_flag
import json

def probe_model_5l_profit(data):
    """
    Evaluate financial flags for the latest financial entry.
    """
    # Get the index of the latest financial entry
    index = latest_financial_index(data)

    # Evaluate the flags
    total_revenue_flag_value = total_revenue_5cr_flag(data, index)
    borrowing_to_revenue_flag_value = borrowing_to_revenue_flag(data, index)
    iscr_flag_value = get_iscr_flag(data, index)

    # Prepare the output in the required format
    output = {
        "Rule 1": "TOTAL_REVENUE_5CR_FLAG: " + ("GREEN" if total_revenue_flag_value == 1 else "RED"),
        "Rule 2": "BORROWING_TO_REVENUE_FLAG: " + ("GREEN" if borrowing_to_revenue_flag_value == 1 else "AMBER"),
        "Rule 3": "ISCR_FLAG: " + ("GREEN" if iscr_flag_value == 1 else "RED"),
    }

    return output

if __name__ == "__main__":
    # Load the financial data from the provided data.json file
    with open("data.json", "r") as file:
        content = file.read()
        # Convert content to JSON
        data = json.loads(content)
        # Call the probe_model_5l_profit function and print the results
        results = probe_model_5l_profit(data["data"])

        # Print the results in the desired format
        for rule, value in results.items():
            print(f"{rule}: {value}")
    