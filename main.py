from src.preprocessing import load_and_preprocess
from src.model import train_model
from src.evaluation import evaluate
from src.predict import predict_disease

import matplotlib.pyplot as plt
import seaborn as sns

df = load_and_preprocess('data/disease_prediction.csv')

plt.figure()
sns.countplot(x='Disease', data=df)
plt.title("Disease Distribution")
plt.show()

plt.figure()
sns.boxplot(x='Disease', y='Age', data=df)
plt.title("Age vs Disease")
plt.show()

plt.figure()
sns.boxplot(x='Disease', y='Sugar_Level', data=df)
plt.title("Sugar Level vs Disease")
plt.show()

plt.figure(figsize=(10,6))
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

model, scaler, X_test, y_test = train_model(df)

evaluate(model, X_test, y_test)

sample = [25, 0, 1, 1, 1, 0, 120, 90, 180, 0]
print("\nPredicted Disease:", predict_disease(model, scaler, sample))