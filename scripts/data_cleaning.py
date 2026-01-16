import pandas as pd
import numpy as np
import os
import data_visualization as dv

def read_data(file_path):

    if not os.path.exists(file_path):
        print(f"Nie znaleziono pliku: {file_path}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("Plik nie zawiera danych.")
            return pd.DataFrame()
        return df
        
    except Exception as e:
        print(f"Problem z odczytaniem pliku: {e}")
        return pd.DataFrame()
    

def clean_data(df):
    if df.empty:
        return df
    if 'Day' in df.columns and 'date' not in df.columns:
        df = df.rename(columns={'Day': 'date'})
    if 'Entity' in df.columns and 'location' not in df.columns:
        df = df.rename(columns={'Entity': 'location'})
    if 'Total confirmed deaths due to COVID-19 per 100,000 people' in df.columns and 'total_deaths' not in df.columns:
        df = df.rename(columns={'Total confirmed deaths due to COVID-19 per 100,000 people': 'total_deaths'})
    # ensure total_cases exists (may be missing in this dataset)
    if 'total_cases' not in df.columns:
        df['total_cases'] = np.nan
    df = df.drop_duplicates()
    # require at least date and total_deaths
    df = df.dropna(subset=['date', 'total_deaths'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df['total_deaths'] = pd.to_numeric(df['total_deaths'], errors='coerce')
    df = df.dropna(subset=['total_deaths'])
    df = df[df['total_deaths'] >= 0]
    return df

def top_death(df, n=10):
    latest_date = df['date'].max()
    latest_data = df[df['date'] == latest_date]
    top_countries = latest_data.nlargest(n, 'total_deaths') [['location', 'total_deaths']]
    return top_countries

def avarge_death(df):
    avg_deaths = df.groupby('location') ['total_deaths'].mean().reset_index()
    avg_deaths = avg_deaths.rename(columns={'total_deaths': 'avarge_deaths'})
    np.mean(avg_deaths['avarge_deaths'])
    return avg_deaths

def main():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'covid_data.csv'))
    df = read_data(file_path)
    cleaned_df = clean_data(df)
    top_countries = top_death(cleaned_df, n=10)
    top_countries['total_deaths'] = top_countries['total_deaths'].round(0).astype(int)
    if not cleaned_df.empty:
        print(f"Top 10 państw według liczby zgonów na dzień {cleaned_df['date'].max().date()}:")
        print(top_countries)
    else:
        print("Brak oczyszczonych danych do wyświetlenia.")


if __name__ == "__main__":
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'covid_data.csv'))
    df = read_data(file_path)
    cleaned_df = clean_data(df)
    top_countries = top_death(cleaned_df, n=10)
    dv.visualization(cleaned_df)
    # format total_deaths for display as integers
    if not top_countries.empty:
        top_countries['total_deaths'] = top_countries['total_deaths'].round(0).astype(int)
    if not cleaned_df.empty:
        print(f"Top 10 państw według liczby zgonów na dzień {cleaned_df['date'].max().date()}:")
        print(top_countries)
    else:
        print("Brak oczyszczonych danych do wyświetlenia.")
    
