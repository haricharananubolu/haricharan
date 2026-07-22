import pandas as pd


def load_data(file_path):
    """
    Load sales data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """

    try:
        data = pd.read_csv(file_path)

        print("\n===================================")
        print("Sales Dataset Loaded Successfully")
        print("===================================\n")

        return data

    except FileNotFoundError:
        print("Error: CSV file not found.")
        return None

    except Exception as e:
        print("An error occurred while loading the dataset.")
        print(e)
        return None


def display_basic_info(data):
    """
    Display basic dataset information.
    """

    print("\n========== First 5 Rows ==========\n")
    print(data.head())

    print("\n========== Last 5 Rows ==========\n")
    print(data.tail())

    print("\n========== Dataset Information ==========\n")
    print(data.info())

    print("\n========== Dataset Shape ==========\n")
    print("Rows :", data.shape[0])
    print("Columns :", data.shape[1])

    print("\n========== Column Names ==========\n")
    print(data.columns.tolist())

    print("\n========== Data Types ==========\n")
    print(data.dtypes)

    print("\n========== Missing Values ==========\n")
    print(data.isnull().sum())

    print("\n========== Summary Statistics ==========\n")
    print(data.describe(include="all"))