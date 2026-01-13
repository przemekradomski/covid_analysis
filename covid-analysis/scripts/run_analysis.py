# run_analysis.py

import pandas as pd
from src.data_processing import load_data, clean_data
from src.analysis import perform_analysis, visualize_results

def main():
    # Load raw data
    raw_data = load_data('data/raw')
    
    # Clean the data
    cleaned_data = clean_data(raw_data)
    
    # Perform analysis
    results = perform_analysis(cleaned_data)
    
    # Visualize results
    visualize_results(results)

if __name__ == "__main__":
    main()