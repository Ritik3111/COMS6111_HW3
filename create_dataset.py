from sodapy import Socrata
import pandas as pd

def get_data():
    client = Socrata("data.cityofnewyork.us", None)
    results = client.get("43nn-pn8j", limit=50000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df

def create_integrated_dataset(df):

    cols_to_keep = ["dba", "boro", "critical_flag", "cuisine_description", "grade"]
    df = df[cols_to_keep]
    df.dropna(subset=['grade'], inplace=True)
    df.to_csv('INTEGRATED-DATASET.csv',index=False)

def main():
    res = get_data()
    create_integrated_dataset(res)

if __name__ == '__main__':
    main()