from flask import Flask, request, render_template
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Define routes
@app.route('/')
def home():
    return render_template('index.html', prediction=None) 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Numeric Variables
        JoiningYear = float(request.form['JoiningYear'])
        Age = float(request.form['Age'])
        DailyRate = float(request.form['DailyRate'])
        DistanceFromHome = float(request.form['DistanceFromHome'])
        HourlyRate = float(request.form['HourlyRate'])
        MonthlyIncome = float(request.form['MonthlyIncome'])
        MonthlyRate = float(request.form['MonthlyRate'])
        PercentSalaryHike = float(request.form['PercentSalaryHike'])
        TotalWorkingYears = float(request.form['TotalWorkingYears'])
        YearsInCurrentRole = float(request.form['YearsInCurrentRole'])
        YearsSinceLastPromotion = float(request.form['YearsSinceLastPromotion'])
        YearsWithCurrManager = float(request.form['YearsWithCurrManager'])
        YearsAtCompany = float(request.form['YearsAtCompany'])
        NumCompaniesWorked = float(request.form['NumCompaniesWorked'])

        # Categorical Variables
        BusinessTravel = int(request.form['BusinessTravel'])
        Department = int(request.form['Department'])
        EducationField = int(request.form['EducationField'])
        EnvironmentSatisfaction = int(request.form['EnvironmentSatisfaction'])
        Gender = int(request.form['Gender'])
        JobInvolvement = int(request.form['JobInvolvement'])
        JobSatisfaction = int(request.form['JobSatisfaction'])
        MaritalStatus = int(request.form['MaritalStatus'])
        OverTime = int(request.form['OverTime'])
        PerformanceRating = int(request.form['PerformanceRating'])
        RelationshipSatisfaction = int(request.form['RelationshipSatisfaction'])
        StockOptionLevel = int(request.form['StockOptionLevel'])
        TrainingTimesLastYear = int(request.form['TrainingTimesLastYear'])
        WorkLifeBalance = int(request.form['WorkLifeBalance'])
        office_code = int(request.form['office_code'])
        JobLevel_updated = int(request.form['JobLevel_updated'])

        # Input the Data
        input_data = {
            'JoiningYear': [JoiningYear],
            'Age': [Age],
            'BusinessTravel': [BusinessTravel],
            'DailyRate': [DailyRate],
            'Department': [Department],
            'DistanceFromHome': [DistanceFromHome],
            'EducationField': [EducationField],
            'EnvironmentSatisfaction': [EnvironmentSatisfaction],
            'Gender': [Gender],
            'HourlyRate': [HourlyRate],
            'JobInvolvement': [JobInvolvement],
            'JobSatisfaction': [JobSatisfaction],
            'MaritalStatus': [MaritalStatus],
            'MonthlyIncome': [MonthlyIncome],
            'MonthlyRate': [MonthlyRate],
            'NumCompaniesWorked': [NumCompaniesWorked],
            'OverTime': [OverTime],
            'PercentSalaryHike': [PercentSalaryHike],
            'PerformanceRating': [PerformanceRating],
            'RelationshipSatisfaction': [RelationshipSatisfaction],
            'StockOptionLevel': [StockOptionLevel],
            'TotalWorkingYears': [TotalWorkingYears],
            'TrainingTimesLastYear': [TrainingTimesLastYear],
            'WorkLifeBalance': [WorkLifeBalance],
            'YearsAtCompany': [YearsAtCompany],
            'YearsInCurrentRole': [YearsInCurrentRole],
            'YearsSinceLastPromotion': [YearsSinceLastPromotion],
            'YearsWithCurrManager': [YearsWithCurrManager],
            'office_code': [office_code],
            'JobLevel_updated': [JobLevel_updated]
        }

        # Create a pandas DataFrame
        input_df = pd.DataFrame(input_data)

        # Make prediction using the loaded model
        prediction = model.predict(input_df)[0]

        # Convert prediction to a user-friendly message
        result = "Employee won't leave the firm" if prediction == 1 else "Employee will leave the firm"

    except Exception as e:
        result = f"Error: {e}"

    # Render the HTML template with the prediction result
    return render_template('index.html', prediction=result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
