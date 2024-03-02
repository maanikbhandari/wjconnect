import pandas as pd
import os

def update_status(csv_file, check_file):
    # Read the CSV files into pandas DataFrames
    df_main = pd.read_csv(csv_file)
    df_check = pd.read_csv(check_file)

    # Extract values from column 1 of both DataFrames
    values_to_check_col1 = set(df_main.iloc[:, 0])
    values_to_compare_col1 = set(df_check.iloc[:, 0])
    values_to_compare_col2 = set(df_check.iloc[:, 1])
    values_to_compare_col3 = set(df_check.iloc[:, 2])
    values_to_compare_col4 = set(df_check.iloc[:, 3])

    # Find common values in column 1 of the main file and column 3 of the check file
    common_values_col1 = values_to_check_col1.intersection(values_to_compare_col3)

    # Filter the main DataFrame to include only rows where column 1 values exist in the check file
    common_values_df_main = df_main[df_main.iloc[:, 0].isin(common_values_col1)]

    # Extract values from column 2 of the common rows in the main file
    values_to_check_col2 = set(common_values_df_main.iloc[:, 1])

    # Check if values in column 2 of the main file exist in column 1 of the check file
    common_values_col2 = values_to_check_col2.intersection(values_to_compare_col1)

    # Set all values in column 4 to "Inactive"
    df_main.iloc[:, 3] = 'Inactive'

    # Update values in the actual column 4 to "Active" for corresponding values in column 1 and column 2
    df_main.loc[(df_main.iloc[:, 0].isin(common_values_col1)) & (df_main.iloc[:, 1].isin(common_values_col2)), df_main.columns[3]] = 'Active'

    # Create 'outputs' directory if it doesn't exist
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the updated DataFrame to a new CSV file
    output_file_path = os.path.join(output_dir, "WestJet-CityPairs-Q2-2024-tb-dom.csv")
    df_main.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # Specify the file paths for your CSV files
    csv_file_path = "WestJet-CityPairs-Q2-2024.csv"
    check_file_path = "check.csv"

    # Call the function to update values in column 4 and save to a new file
    update_status(csv_file_path, check_file_path)
