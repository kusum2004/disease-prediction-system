Disease Prediction System using Machine Learning
📌 Project Overview

This project focuses on building a Machine Learning-based Disease Prediction System that analyzes patient health parameters and predicts possible diseases using classification algorithms. The system performs data preprocessing, model training, evaluation, and prediction using a modular Python-based architecture.

The project demonstrates the practical implementation of Machine Learning concepts in the healthcare domain and helps in understanding predictive analytics using patient data.

📊 Dataset Information

The dataset used in this project contains patient medical information such as:

Patient ID
Age
Gender
Fever
Cough
Headache
Chest Pain
Blood Pressure
Sugar Level
Cholesterol
Medical History
Disease

The dataset is preprocessed and cleaned before model training.

⚙️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
VS Code
🧠 Machine Learning Workflow
1. Data Preprocessing
Loaded dataset using Pandas
Handled missing values
Converted categorical values into numerical format
Prepared features and target variables
2. Exploratory Data Analysis (EDA)
Disease distribution analysis
Age vs Disease visualization
Sugar Level vs Disease analysis
Correlation Heatmap
3. Model Training
Applied Random Forest Classifier
Performed train-test split
Applied feature scaling using StandardScaler
4. Model Evaluation
Accuracy Score
Classification Report
Confusion Matrix
5. Prediction System
Predicts disease based on patient input parameters
Uses trained Machine Learning model for predictions
📁 Project Structure
Disease-Prediction-System
│
├── data
│   └── disease_prediction.csv
│
├── src
│   ├── preprocessing.py
│   ├── model.py
│   ├── evaluation.py
│   └── predict.py
│
├── main.py
├── README.md
📈 Visualizations Included
Disease Distribution Graph
Age vs Disease Boxplot
Sugar Level vs Disease Boxplot
Correlation Heatmap
🚀 How to Run the Project
1. Clone Repository
git clone <repository-url>
2. Install Required Libraries
pip install pandas numpy matplotlib seaborn scikit-learn
3. Run the Project
python main.py
🎯 Project Outcome

The project successfully predicts diseases using patient medical data and demonstrates the practical workflow of Machine Learning in healthcare analytics.

This project helps in:

Understanding healthcare prediction systems
Applying Machine Learning in real-world datasets
Learning data preprocessing and model evaluation
Building modular ML project architecture
🔮 Future Improvements
Add Deep Learning models
Build Streamlit web application
Improve prediction accuracy
Deploy project on cloud platforms
Add real-time patient input interface
👨‍💻 Author

Kusuma
Machine Learning & AI Enthusiast
