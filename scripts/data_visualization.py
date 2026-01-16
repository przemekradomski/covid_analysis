import matplotlib.pyplot as plt

def visualization(df):
    if df.empty:
        print("Brak danych do wizualizacji.")
        return
    latest_date = df['date'].max()
    latest_date_data = df[df['date'] == latest_date_data]
    plt.figure(figsize=(10,6))
    plt.bar(latest_date_data['location'], latest_date_data['total_deaths'])
    plt.xlabel('Kraje')
    plt.ylabel('Liczba zgonów')
    plt.title(f'Liczba zgonów na dzien {latest_date.date()}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()