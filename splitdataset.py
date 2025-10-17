import pandas as pd
import os

def split_csv(input_file, output_folder, chunk_size=500000):
    """
    Splits a large CSV file into smaller chunks.

    Args:
        input_file (str): The path to the large CSV file.
        output_folder (str): The folder where the smaller CSVs will be saved.
        chunk_size (int): The number of rows per smaller CSV file.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    # Create an iterator to read the CSV in chunks
    chunk_iter = pd.read_csv(input_file, chunksize=chunk_size)
    
    file_number = 1
    print(f"Starting to split {input_file}...")

    # Loop through the chunks and save each as a new CSV
    for chunk in chunk_iter:
        output_file = os.path.join(output_folder, f"{file_number}.csv")
        chunk.to_csv(output_file, index=False)
        print(f"Saved {output_file} with {len(chunk)} rows.")
        file_number += 1
    
    print("\nSplitting complete! ✨")

# --- Configuration ---
# 1. Name of your large CSV file
large_csv_file = 'AirlineReviews.csv' 

# 2. Name of the folder for the split files
split_folder_name = 'split_dataset'

# 3. Number of rows per file
rows_per_file = 10000 

# --- Run the function ---
if __name__ == '__main__':
    # Check if the input file exists before running
    if os.path.exists(large_csv_file):
        split_csv(large_csv_file, split_folder_name, rows_per_file)
    else:
        print(f"Error: The file '{large_csv_file}' was not found. Please check the filename.")