import pandas as pd
import glob
import os

def merge_csvs(input_folder, output_file):
    """
    Merges all CSV files from a folder into a single CSV file.

    Args:
        input_folder (str): The folder containing the split CSV files.
        output_file (str): The path for the final merged CSV file.
    """
    # Find all CSV files in the input folder
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    
    # Sort files numerically (e.g., 1.csv, 2.csv, 10.csv) to maintain order
    csv_files.sort(key=lambda f: int(os.path.splitext(os.path.basename(f))[0]))

    if not csv_files:
        print(f"No CSV files found in the folder: {input_folder}")
        return

    print("Files to be merged:")
    for f in csv_files:
        print(f"  - {f}")
        
    # Read each CSV and store it in a list of DataFrames
    df_list = [pd.read_csv(file) for file in csv_files]
    
    # Concatenate all DataFrames in the list into a single one
    merged_df = pd.concat(df_list, ignore_index=True)
    
    # Save the merged DataFrame to the output file
    merged_df.to_csv(output_file, index=False)
    
    print(f"\nMerge complete! ✅\nFinal file '{output_file}' created with {len(merged_df)} rows.")


# --- Configuration ---
# 1. Folder where the split CSV files are located
split_folder_name = 'split_dataset'

# 2. Name of the final merged file
merged_file_name = 'AirlineReviews.csv'

# --- Run the function ---
if __name__ == '__main__':
    if os.path.exists(split_folder_name):
        merge_csvs(split_folder_name, merged_file_name)
    else:
        print(f"Error: The folder '{split_folder_name}' was not found.")