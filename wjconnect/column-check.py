import pandas as pd

def find_column_number(csv_file, target_column):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Check if the target column exists in the DataFrame
    if target_column in df.columns:
        column_number = df.columns.get_loc(target_column) + 1  # Adding 1 to make it 1-indexed
        print(f"The column number of '{target_column}' is: {column_number}")
    else:
        print(f"Column '{target_column}' not found in the CSV file.")

if __name__ == "__main__":
    # Specify the file path for your CSV file
    csv_file_path = "C:/Users/maani/Downloads/wjconnect/WestJet-CityPairs-Q2-2024.csv"

    # Specify the target column name
    target_column_name = "Status"

    # Call the function to find the column number
    find_column_number(csv_file_path, target_column_name)
