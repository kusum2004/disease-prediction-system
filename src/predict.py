import pandas as pd

def predict_disease(model, scaler, data):
    columns = [
        'Age','Gender','Fever','Cough','Headache','Chest_Pain',
        'Blood_Pressure','Sugar_Level','Cholesterol','Medical_History'
    ]

    df = pd.DataFrame([data], columns=columns)
    df = scaler.transform(df)

    prediction = model.predict(df)

    return prediction[0]