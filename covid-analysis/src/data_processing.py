def load_data(file_path):
    """Load raw data from a specified file path."""
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the raw data by handling missing values and duplicates."""
    data = data.dropna()
    data = data.drop_duplicates()
    return data

def transform_data(data):
    """Transform the data for analysis, such as normalizing or encoding."""
    # Example transformation: normalize a specific column
    data['normalized_column'] = (data['column_name'] - data['column_name'].mean()) / data['column_name'].std()
    return data

def save_processed_data(data, output_path):
    """Save the processed data to a specified output path."""
    data.to_csv(output_path, index=False)

def process_data(file_path, output_path):
    """Main function to load, clean, transform, and save data."""
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    transformed_data = transform_data(cleaned_data)
    save_processed_data(transformed_data, output_path)