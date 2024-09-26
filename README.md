# Multiple Disease Prediction System

## Overview

The Multiple Disease Prediction System is a machine learning project designed to predict whether a user has heart disease or diabetes. This system utilizes different algorithms to analyze user data and provide accurate predictions.

## Features

- **Heart Disease Prediction**: Utilizes Logistic Regression to determine if a user has heart disease.
- **Diabetes Prediction**: Employs Support Vector Machine (SVM) algorithm to assess the likelihood of diabetes in users.

## Technologies Used

- Python
- Streamlit (for building the web application interface)
- Scikit-learn (for machine learning algorithms)
- Pandas (for data manipulation)
- NumPy (for numerical operations)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/USERNAME/MULTIPLE_DISEASE_PREDICTION.git
   cd MULTIPLE_DISEASE_PREDICTION
   ```

2. **Install Required Packages**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

3. Enter the required data in the provided input fields for heart disease or diabetes prediction.

4. Click on the **Predict** button to see the results.

## How It Works

- **Heart Disease Prediction**: The model takes user input features such as age, cholesterol level, blood pressure, etc., and predicts the presence of heart disease using Logistic Regression.

- **Diabetes Prediction**: The model analyzes input features such as glucose level, body mass index (BMI), age, and other health metrics to predict the likelihood of diabetes using the SVM algorithm.

## Contributing

Contributions are welcome! If you want to improve this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to reach out to me at [shivampandeypbt007@gmail.com](mailto:shivampandeypbt007@gmail.com).
