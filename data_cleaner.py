import pandas as pd


def clean_data(data):
    """
    Cleans the sales dataset.
    """

    print("\n========== Data Cleaning Started ==========\n")

    # -------------------------------
    # Remove Duplicate Rows
    # -------------------------------
    duplicate_count = data.duplicated().sum()
    print(f"Duplicate Rows Found : {duplicate_count}")

    data = data.drop_duplicates()

    # -------------------------------
    # Handle Missing Values
    # -------------------------------
    print("\nMissing Values Before Cleaning")
    print(data.isnull().sum())

    data = data.dropna()

    print("\nMissing Values After Cleaning")
    print(data.isnull().sum())

    # -------------------------------
    # Convert Date Column
    # -------------------------------
    data["Date"] = pd.to_datetime(data["Date"])

    # -------------------------------
    # Convert Numeric Columns
    # -------------------------------
    data["Quantity"] = pd.to_numeric(data["Quantity"])
    data["Price"] = pd.to_numeric(data["Price"])

    # -------------------------------
    # Create Total Sales Column
    # -------------------------------
    data["Total_Sales"] = data["Quantity"] * data["Price"]

    print("\nNew Column 'Total_Sales' Created Successfully")

    print("\n========== Cleaning Completed ==========\n")

    return data


def save_clean_data(data, output_path):
    """
    Saves the cleaned dataset.
    """

    data.to_csv(output_path, index=False)

    print("\n===================================")
    print("Cleaned Dataset Saved Successfully")
    print(output_path)
    print("===================================\n")