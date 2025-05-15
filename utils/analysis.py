import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    
    # Convert 'Timestamp' to datetime and extract date
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df['date'] = df['Timestamp'].dt.date  # Create a 'date' column

    return df
