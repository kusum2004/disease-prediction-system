import pandas as pd

def load_and_preprocess(path):
    df = pd.read_csv(path)

    df.ffill(inplace=True)

    df['Gender'] = df['Gender'].map({'Male':0, 'Female':1})

    df['Medical_History'] = df['Medical_History'].map({
        'None':0,
        'Diabetes':1,
        'Hypertension':2
    })

    return df