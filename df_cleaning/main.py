from pipeline import set_pipeline
from data import get_data


if __name__ == "__main__":
    # change the id here
    id = "20022492"

    print(f'Starting run:')
    df = get_data(id)
    print('Data acquired')
    clean_df = set_pipeline().fit_transform(df)
    print('Dataframe cleaned')
